"""Junta quadros 32x32 (ou outro tamanho igual) numa folha de animacao.

Uso:
  python tools/montar_folha.py saida.png --colunas 4 baixo1.png baixo2.png ... cima4.png

Os quadros entram na ordem dada, da esquerda para a direita e linha por linha
(linhas: baixo, esquerda, direita, cima). Use "espelho:arquivo.png" para virar um quadro na horizontal
(ex.: a linha direita feita do espelho da esquerda). Depois rode tools/check_art.py.
"""
import argparse
from pathlib import Path
from PIL import Image, ImageOps


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("saida")
    ap.add_argument("quadros", nargs="+")
    ap.add_argument("--colunas", type=int, required=True)
    a = ap.parse_args()

    imgs = []
    for q in a.quadros:
        espelho = q.startswith("espelho:")
        im = Image.open(q.removeprefix("espelho:")).convert("RGBA")
        imgs.append(ImageOps.mirror(im) if espelho else im)
    w, h = imgs[0].size
    if any(i.size != (w, h) for i in imgs):
        raise SystemExit("ERRO: quadros com tamanhos diferentes. Converta todos com tools/pixelize.py no mesmo --largura/--altura.")
    linhas = -(-len(imgs) // a.colunas)
    folha = Image.new("RGBA", (w * a.colunas, h * linhas), (0, 0, 0, 0))
    for n, im in enumerate(imgs):
        folha.paste(im, ((n % a.colunas) * w, (n // a.colunas) * h))
    Path(a.saida).parent.mkdir(parents=True, exist_ok=True)
    folha.save(a.saida)
    print(f"ok {a.saida} {folha.width}x{folha.height} ({len(imgs)} quadros)")


if __name__ == "__main__":
    main()
