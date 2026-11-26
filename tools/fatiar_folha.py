"""Converte uma folha de animação gerada por IA (grade de quadros) para sprites de 32x32 do jogo.

    python tools/fatiar_folha.py art/referencia/campones-simples.png campones --colunas 6 --linhas 4 \
        --animacao parado:0-1 --animacao andar:2-5

- Linhas na ordem do AGENTS.md: baixo, esquerda, direita, cima.
- O fundo (chapado ou em degradê) é removido a partir das bordas de cada quadro.
- **Todos os quadros usam a mesma escala**: o mais alto vira 24 px e os outros encolhem na mesma
  proporção. Por isso o personagem não "pulsa" de tamanho durante o passo, como aconteceria com
  `pixelize.py --corpo` quadro a quadro.
- Pés na linha y=30 e cabeça centralizada em x=16 em todos os quadros.

Saídas: art/personagens/<nome>-<animacao>.png (folhas), quadros soltos em art/rascunho/quadros/<nome>/
e uma prévia animada 8x em art/rascunho/<nome>-<animacao>-8x.gif (não é asset do jogo).
"""
import argparse
import sys
from collections import deque
from pathlib import Path

from PIL import Image

sys.path.insert(0, str(Path(__file__).parent))
from pixelize import ler_paleta  # noqa: E402

QUADRO, CORPO, BASE_PES = 32, 24, 30


def tirar_fundo(celula, passo, limite, alfa):
    """Folha com transparência: corta pelo alfa (brilho e sombra semitransparentes somem).
    Folha opaca: cresce o fundo a partir das bordas enquanto a cor muda pouco entre vizinhos."""
    im = celula.convert("RGBA")
    if im.split()[3].getextrema()[0] < 255:
        im.putalpha(im.split()[3].point(lambda v: 255 if v >= alfa else 0))
        return im
    px = im.load()
    w, h = im.size
    fundo = [[False] * w for _ in range(h)]
    fila = deque()
    for x in range(w):
        fila.extend(((x, 0), (x, h - 1)))
    for y in range(h):
        fila.extend(((0, y), (w - 1, y)))
    for x, y in fila:
        fundo[y][x] = True
    ref = px[0, 0]
    while fila:
        x, y = fila.popleft()
        r, g, b, _ = px[x, y]
        for nx, ny in ((x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)):
            if 0 <= nx < w and 0 <= ny < h and not fundo[ny][nx]:
                r2, g2, b2, _ = px[nx, ny]
                perto = abs(r - r2) + abs(g - g2) + abs(b - b2) < passo
                parecido = abs(ref[0] - r2) + abs(ref[1] - g2) + abs(ref[2] - b2) < limite
                if perto and parecido:
                    fundo[ny][nx] = True
                    fila.append((nx, ny))
    for y in range(h):
        for x in range(w):
            if fundo[y][x]:
                px[x, y] = (0, 0, 0, 0)
    return im


def reduzir_por_moda(im, k, paleta):
    """Cada pixel do jogo recebe a cor da paleta mais comum no bloco de origem (sem média de cores,
    que mistura contorno com preenchimento e cria pontos de cor errada)."""
    w, h = max(1, round(im.width * k)), max(1, round(im.height * k))
    src = im.load()
    cache = {}

    def mais_perto(rgb):
        if rgb not in cache:
            cache[rgb] = min(paleta, key=lambda p: (p[0] - rgb[0]) ** 2 + (p[1] - rgb[1]) ** 2 + (p[2] - rgb[2]) ** 2)
        return cache[rgb]

    out = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    po = out.load()
    for y in range(h):
        y0, y1 = int(y * im.height / h), max(int(y * im.height / h) + 1, int((y + 1) * im.height / h))
        for x in range(w):
            x0, x1 = int(x * im.width / w), max(int(x * im.width / w) + 1, int((x + 1) * im.width / w))
            votos, opacos, total = {}, 0, 0
            for yy in range(y0, y1):
                for xx in range(x0, x1):
                    r, g, b, al = src[xx, yy]
                    total += 1
                    if al:
                        opacos += 1
                        c = mais_perto((r, g, b))
                        votos[c] = votos.get(c, 0) + 1
            if opacos * 2 >= total:
                po[x, y] = (*max(votos, key=votos.get), 255)
    return out


def centro_cabeca(im, caixa):
    x0, y0, x1, y1 = caixa
    topo = im.crop((x0, y0, x1, y0 + max(1, (y1 - y0) * 35 // 100)))
    cx0, _, cx1, _ = topo.getbbox() or (0, 0, x1 - x0, 0)
    return x0 + (cx0 + cx1) / 2


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("folha")
    ap.add_argument("nome")
    ap.add_argument("--colunas", type=int, required=True)
    ap.add_argument("--linhas", type=int, required=True)
    ap.add_argument("--animacao", action="append", required=True, help="nome:coluna_ini-coluna_fim")
    ap.add_argument("--passo", type=int, default=40, help="diferença máxima entre vizinhos no fundo")
    ap.add_argument("--limite", type=int, default=140, help="diferença máxima até a cor do canto")
    ap.add_argument("--alfa", type=int, default=200, help="folha com transparência: alfa mínimo do personagem")
    ap.add_argument("--ms", type=int, default=150, help="duração de cada quadro na prévia")
    a = ap.parse_args()

    folha = Image.open(a.folha).convert("RGBA")
    cw, ch = folha.width // a.colunas, folha.height // a.linhas
    limpos = {}
    for lin in range(a.linhas):
        for col in range(a.colunas):
            cel = folha.crop((col * cw, lin * ch, (col + 1) * cw, (lin + 1) * ch))
            im = tirar_fundo(cel, a.passo, a.limite, a.alfa)
            if im.getbbox() is None:
                raise SystemExit(f"ERRO: quadro linha {lin} coluna {col} ficou vazio. Diminua --limite.")
            limpos[lin, col] = im

    alturas = [im.getbbox()[3] - im.getbbox()[1] for im in limpos.values()]
    k = CORPO / max(alturas)
    paleta = ler_paleta("vila")
    raiz = Path(__file__).resolve().parent.parent
    pasta_q = raiz / "art" / "rascunho" / "quadros" / a.nome
    pasta_q.mkdir(parents=True, exist_ok=True)

    pequenos = {}
    for (lin, col), im in limpos.items():
        caixa = im.getbbox()
        cx = centro_cabeca(im, caixa)
        sub = reduzir_por_moda(im.crop(caixa), k, paleta)
        out = Image.new("RGBA", (QUADRO, QUADRO), (0, 0, 0, 0))
        x = round(QUADRO / 2 - (cx - caixa[0]) * k)
        out.alpha_composite(sub, (x, BASE_PES - sub.height))
        out.save(pasta_q / f"l{lin}-c{col}.png")
        pequenos[lin, col] = out

    for spec in a.animacao:
        nome_anim, faixa = spec.split(":")
        c0, c1 = (int(v) for v in faixa.split("-"))
        cols = list(range(c0, c1 + 1))
        f = Image.new("RGBA", (QUADRO * len(cols), QUADRO * a.linhas), (0, 0, 0, 0))
        for lin in range(a.linhas):
            for i, col in enumerate(cols):
                f.paste(pequenos[lin, col], (i * QUADRO, lin * QUADRO))
        destino = raiz / "art" / "personagens" / f"{a.nome}-{nome_anim}.png"
        f.save(destino)
        f.resize((f.width * 8, f.height * 8), Image.NEAREST).save(destino.with_suffix(".preview8x.png"))

        quadros_gif = []
        for col in cols:
            tela = Image.new("RGBA", (QUADRO * a.linhas, QUADRO), (120, 170, 80, 255))
            for lin in range(a.linhas):
                tela.alpha_composite(pequenos[lin, col], (lin * QUADRO, 0))
            quadros_gif.append(tela.resize((tela.width * 8, tela.height * 8), Image.NEAREST).convert("RGB"))
        gif = raiz / "art" / "rascunho" / f"{a.nome}-{nome_anim}-8x.gif"
        quadros_gif[0].save(gif, save_all=True, append_images=quadros_gif[1:], duration=a.ms, loop=0)
        print(f"ok {destino.relative_to(raiz)} e prévia {gif.relative_to(raiz)}")


if __name__ == "__main__":
    main()
