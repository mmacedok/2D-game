"""Confere se os PNGs do jogo seguem as regras de arte. Sai com codigo 1 se algum falhar.

Uso: python tools/check_art.py            (confere art/ inteira)
     python tools/check_art.py arquivo.png
"""
import sys
from pathlib import Path
from PIL import Image

RAIZ = Path(__file__).resolve().parent.parent
def _ler(nome):
    return {tuple(int(h[i:i + 2], 16) for i in (0, 2, 4)) for h in (RAIZ / "art" / nome).read_text().split()}


PALETA_VILA = _ler("paleta.hex")
PALETA_MASMORRA = PALETA_VILA | _ler("paleta-masmorra.hex")  # masmorra pode usar as duas

# Personagens jogaveis, skins, icones e UI usam so a paleta da vila: o jogador continua colorido
# e facil de ver tambem na masmorra. Tiles, objetos, monstros e chefes dentro de art/masmorra/
# podem usar a paleta escura.
# pasta -> (multiplo de largura, multiplo de altura, tamanho maximo)
REGRAS = {
    "tiles": (16, 16, 256),
    "objetos": (16, 16, 128),
    "personagens": (32, 32, 512),
    "monstros": (32, 32, 512),
    "chefes": (64, 64, 1024),
    "icones": (16, 16, 16),
    "ui": (1, 1, 640),
}
IGNORAR = ("referencia", "rascunho", "rejeitadas", "conceitos")
SO_VILA = ("personagens", "icones", "ui")


def conferir(p: Path):
    erros = []
    if any(parte in IGNORAR for parte in p.parts) or p.name.endswith(".preview8x.png") or p.name.startswith("paleta"):
        return erros
    pasta = next((k for k in REGRAS if k in p.parts), None)
    if pasta is None:
        return [f"{p}: fora de uma pasta conhecida ({', '.join(REGRAS)}). Mova para a pasta do tipo do asset."]
    if "masmorra" in p.parts and pasta in SO_VILA:
        return [f"{p}: '{pasta}' nao vai dentro de art/masmorra/. Personagens, icones e UI ficam em art/{pasta}/ com a paleta da vila."]
    paleta = PALETA_MASMORRA if "masmorra" in p.parts else PALETA_VILA
    im = Image.open(p)
    mw, mh, mx = REGRAS[pasta]
    w, h = im.size
    if w % mw or h % mh:
        erros.append(f"{p}: {w}x{h} nao e multiplo de {mw}x{mh}. Gere de novo com tools/pixelize.py --largura/--altura certos.")
    if max(w, h) > mx:
        erros.append(f"{p}: {w}x{h} passa do maximo {mx}px para '{pasta}'. A imagem ainda esta em escala de IA; rode tools/pixelize.py.")
    im = im.convert("RGBA")
    fora, semi = set(), 0
    for r, g, b, a in (im.get_flattened_data() if hasattr(im, "get_flattened_data") else im.getdata()):
        if a == 0:
            continue
        if a != 255:
            semi += 1
        elif (r, g, b) not in paleta:
            fora.add((r, g, b))
    if semi:
        erros.append(f"{p}: {semi} pixels semitransparentes (anti-aliasing). Passe por tools/pixelize.py, que deixa o alfa so 0/255.")
    if fora:
        amostra = ", ".join("%02X%02X%02X" % c for c in list(fora)[:5])
        erros.append(f"{p}: {len(fora)} cores fora da paleta da zona (ex.: {amostra}). Passe por tools/pixelize.py (a pasta de destino escolhe a paleta; asset de masmorra vai em art/masmorra/). Nao acrescente cor na paleta sem aprovar.")
    return erros


def main():
    alvos = [Path(a) for a in sys.argv[1:]] or sorted((RAIZ / "art").rglob("*.png"))
    erros = [e for p in alvos for e in conferir(p)]
    for e in erros:
        print("ERRO", e)
    print(f"{len(alvos)} arquivo(s), {len(erros)} erro(s)")
    sys.exit(1 if erros else 0)


if __name__ == "__main__":
    main()
