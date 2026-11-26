"""Converte uma imagem gerada por IA em pixel art de verdade, na grade e na paleta do jogo.

Uso:
  python tools/pixelize.py entrada.png saida.png --largura 32 [--altura 32] [--fundo FF00FF]

- --largura/--altura: tamanho FINAL em pixels do jogo (ex.: 16 para um tile, 32 para um quadro).
- --fundo: cor do fundo chapado que o prompt pediu; vira transparente. Padrao FF00FF (magenta).
- Reduz com media por bloco, prende cada pixel a cor mais proxima de art/paleta.hex (sem dithering)
  e deixa a transparencia so 0 ou 255.
Depois rode tools/check_art.py.
"""
import argparse
from pathlib import Path
from PIL import Image

RAIZ = Path(__file__).resolve().parent.parent


def ler_paleta():
    cores = []
    for linha in (RAIZ / "art" / "paleta.hex").read_text().split():
        cores.append(tuple(int(linha[i:i + 2], 16) for i in (0, 2, 4)))
    return cores


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("entrada")
    ap.add_argument("saida")
    ap.add_argument("--largura", type=int, required=True)
    ap.add_argument("--altura", type=int)
    ap.add_argument("--fundo", default="FF00FF")
    ap.add_argument("--tolerancia", type=int, default=90, help="distancia RGB ate a cor de fundo")
    a = ap.parse_args()

    im = Image.open(a.entrada).convert("RGBA")
    altura = a.altura or round(im.height * a.largura / im.width)
    fr, fg, fb = (int(a.fundo[i:i + 2], 16) for i in (0, 2, 4))

    # 1) fundo chapado -> transparente, antes de reduzir (evita borda rosa)
    px = im.load()
    for y in range(im.height):
        for x in range(im.width):
            r, g, b, al = px[x, y]
            if abs(r - fr) + abs(g - fg) + abs(b - fb) < a.tolerancia:
                px[x, y] = (0, 0, 0, 0)

    # 2) reduz para a grade do jogo
    pequeno = im.resize((a.largura, altura), Image.BOX)

    # 3) paleta + alfa binario
    paleta = ler_paleta()
    out = Image.new("RGBA", pequeno.size, (0, 0, 0, 0))
    po, pp = out.load(), pequeno.load()
    for y in range(altura):
        for x in range(a.largura):
            r, g, b, al = pp[x, y]
            if al < 128:
                continue
            c = min(paleta, key=lambda p: (p[0] - r) ** 2 + (p[1] - g) ** 2 + (p[2] - b) ** 2)
            po[x, y] = (*c, 255)
    Path(a.saida).parent.mkdir(parents=True, exist_ok=True)
    out.save(a.saida)
    out.resize((a.largura * 8, altura * 8), Image.NEAREST).save(Path(a.saida).with_suffix(".preview8x.png"))
    print(f"ok {a.saida} {a.largura}x{altura} (preview 8x ao lado, nao e asset do jogo)")


if __name__ == "__main__":
    main()
