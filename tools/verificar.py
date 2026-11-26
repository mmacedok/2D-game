"""Checagem obrigatória antes de qualquer commit ou PR.

    python tools/verificar.py            # arte + configuração + jogo roda sem erro
    python tools/verificar.py --captura  # também grava build/captura.png do jogo rodando

Só entregue quando terminar com "TUDO CERTO". O Godot é procurado na variável GODOT, no PATH
(godot, godot4) e nas pastas comuns do Windows.
"""
import argparse
import glob
import os
import re
import shutil
import subprocess
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

CONFIG_OBRIGATORIA = {
    "display/window/size/viewport_width": "640",
    "display/window/size/viewport_height": "360",
    "display/window/stretch/mode": '"viewport"',
    "display/window/stretch/scale_mode": '"integer"',
    "rendering/textures/canvas_textures/default_texture_filter": "0",
    "rendering/2d/snap/snap_2d_transforms_to_pixel": "true",
}

PADROES_DE_ERRO = re.compile(r"(SCRIPT ERROR|Parse Error|ERROR:|Failed to load|Cannot open file)")


def achar_godot():
    if os.environ.get("GODOT"):
        return os.environ["GODOT"]
    for nome in ("godot", "godot4"):
        caminho = shutil.which(nome)
        if caminho:
            return caminho
    candidatos = []
    for base in ("C:/Program Files/Godot", "D:/AI Workshop/Jogos/Godot", os.path.expanduser("~/Godot"),
                 os.path.expanduser("~/Downloads"), os.path.expanduser("~/Desktop")):
        candidatos += glob.glob(os.path.join(base, "**", "Godot_v4*.exe"), recursive=True)
    candidatos = [c for c in candidatos if "console" not in c.lower()]
    return sorted(candidatos)[-1] if candidatos else None


def ler_config():
    secao, valores = "", {}
    with open(os.path.join(RAIZ, "project.godot"), encoding="utf-8") as f:
        for linha in f:
            linha = linha.strip()
            if linha.startswith("[") and linha.endswith("]"):
                secao = linha[1:-1]
            elif "=" in linha and not linha.startswith(";"):
                chave, valor = linha.split("=", 1)
                valores[f"{secao}/{chave}"] = valor
    return valores


def checar_config():
    valores = ler_config()
    erros = []
    for chave, esperado in CONFIG_OBRIGATORIA.items():
        if valores.get(chave) != esperado:
            erros.append(f"project.godot: {chave} deve ser {esperado} (está {valores.get(chave, 'ausente')}). "
                         "Ver AGENTS.md seção 8.")
    return erros


def rodar(cmd, timeout):
    r = subprocess.run(cmd, cwd=RAIZ, capture_output=True, text=True, timeout=timeout,
                       encoding="utf-8", errors="replace")
    return r.returncode, r.stdout + r.stderr


def checar_godot(godot):
    erros = []
    _, saida = rodar([godot, "--headless", "--path", RAIZ, "--import"], 600)
    saida_jogo_cod, saida_jogo = rodar([godot, "--headless", "--path", RAIZ, "--quit-after", "180"], 300)
    for linha in (saida + "\n" + saida_jogo).splitlines():
        if PADROES_DE_ERRO.search(linha):
            msg = f"Godot: {linha.strip()}"
            if msg not in erros:
                erros.append(msg)
    if saida_jogo_cod != 0 and not erros:
        erros.append(f"Godot terminou com código {saida_jogo_cod}. Saída:\n{saida_jogo[-2000:]}")
    return erros


def capturar(godot):
    pasta = os.path.join(RAIZ, "build", "captura-quadros")
    shutil.rmtree(pasta, ignore_errors=True)
    os.makedirs(pasta)
    rodar([godot, "--path", RAIZ, "--write-movie", os.path.join(pasta, "q.png"),
           "--fixed-fps", "30", "--quit-after", "90"], 300)
    quadros = sorted(glob.glob(os.path.join(pasta, "q*.png")))
    if not quadros:
        return None
    destino = os.path.join(RAIZ, "build", "captura.png")
    shutil.copy(quadros[-1], destino)
    shutil.rmtree(pasta, ignore_errors=True)
    return destino


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    ap = argparse.ArgumentParser()
    ap.add_argument("--captura", action="store_true", help="grava build/captura.png do jogo rodando")
    ap.add_argument("--sem-godot", action="store_true", help="só arte e configuração (CI sem Godot)")
    args = ap.parse_args()

    erros = []
    print("1/3 Arte (check_art.py)...")
    if subprocess.run([sys.executable, os.path.join(RAIZ, "tools", "check_art.py")], cwd=RAIZ).returncode != 0:
        erros.append("check_art.py reprovou a arte: corrija pelo texto acima.")

    print("2/3 Configuração de pixel art (project.godot)...")
    erros += checar_config()

    if args.sem_godot:
        print("3/3 Godot pulado (--sem-godot).")
    else:
        godot = achar_godot()
        if not godot:
            erros.append("Godot 4 não encontrado. Defina a variável GODOT com o caminho do executável.")
        else:
            print(f"3/3 Jogo roda sem erro ({godot})...")
            erros += checar_godot(godot)
            if args.captura and not erros:
                destino = capturar(godot)
                if destino:
                    print(f"Captura: {destino}  <- abra e confira com os próprios olhos.")
                else:
                    erros.append("A captura não gerou imagem (precisa de tela; não funciona em --headless).")

    if erros:
        print(f"\nREPROVADO: {len(erros)} problema(s)")
        for e in erros:
            print(f"- {e}")
        sys.exit(1)
    print("\nTUDO CERTO")


if __name__ == "__main__":
    main()
