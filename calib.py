#   _______________________________________________________________________________________________________________________________
#   |                                                                                                                              |
#   |           _____/\\\\\\\\\\\\______________________________________________________________________________                   |
#   |            ___/\\\//////////_______________________________________________________________________________                  |
#   |             __/\\\__________________________________________________________________________________________                 |
#   |              _\/\\\____/\\\\\\\_____/\\\\\_______/\\\\\__/\\\\\_______/\\\\\\\\___/\\\\\\\\\\\__/\\\\\\\\\\\_                |
#   |               _\/\\\___\/////\\\___/\\\///\\\___/\\\///\\\\\///\\\___/\\\/////\\\_\///////\\\/__\///////\\\/__               |
#   |                _\/\\\_______\/\\\__/\\\__\//\\\_\/\\\_\//\\\__\/\\\__/\\\\\\\\\\\_______/\\\/_________/\\\/____              |
#   |                 _\/\\\_______\/\\\_\//\\\__/\\\__\/\\\__\/\\\__\/\\\_\//\\///////______/\\\/_________/\\\/______             |
#   |                  _\//\\\\\\\\\\\\/___\///\\\\\/___\/\\\__\/\\\__\/\\\__\//\\\\\\\\\\__/\\\\\\\\\\\__/\\\\\\\\\\\_            |
#   |                   __\////////////_______\/////_____\///___\///___\///____\//////////__\///////////__\///////////__           |
#   |                                                                                                                              |
#   |______________________________________________________________________________________________________________________________|
#   |                                                                                                                              |  
#   |                                       IAuto Full - Version 1.2 - 08/04/2025 - By Gomezz                                      |
#   |                                       = Using Deep Seek V3, Leonardo AI and Hailuo AI =                                      |
#   |______________________________________________________________________________________________________________________________|

import pyautogui
import json
import time
import os
import tkinter as tk
from tkinter import ttk

def limpar_console():
    os.system('cls' if os.name == 'nt' else 'clear')
    limpar_console()
    print("\n")

def mostrar_instrucao_com_contagem(nome, segundos=10):
    root = tk.Tk()
    root.attributes('-topmost', True)
    root.overrideredirect(True)
    root.configure(bg='black')  # fundo da sombra

    largura = 850
    altura = 140
    largura_tela = root.winfo_screenwidth()
    altura_tela = root.winfo_screenheight()
    x = (largura_tela // 2) - (largura // 2)
    y = (altura_tela // 2) - (altura // 2)
    root.geometry(f"{largura}x{altura}+{x}+{y}")

    # Frame principal com borda arredondada e sombra simulada
    frame = tk.Frame(root, bg="#1e1e1e", highlightbackground="white", highlightthickness=2)
    frame.place(relx=0.5, rely=0.5, anchor="center", width=largura - 20, height=altura - 20)

    texto = tk.StringVar()
    label = tk.Label(
        frame, textvariable=texto, font=("Segoe UI", 16, "bold"),
        fg="white", bg="#1e1e1e", justify="center", padx=20, pady=10
    )
    label.pack(expand=True, fill="both")

    def atualizar_contagem(seg):
        if seg > 0:
            texto.set(f"💬 Posicione o mouse sobre: '{nome}'\n⏳ {seg} segundos restantes...")
            root.after(1000, atualizar_contagem, seg - 1)
        else:
            root.destroy()

    atualizar_contagem(segundos)
    root.mainloop()

posicoes = {}

# Lista dos elementos que queremos configurar
elementos = [

    # Leonardo AI
    "abrir_img",
    "baixar_img",
    "fechar_img",

    # Hailuo AI
    "anexo_anim",
    "texto_anim",
    "gerar_anim",
    "abrir_anim",
    "baixar_anim"
]

for nome in elementos:
    mostrar_instrucao_com_contagem(nome, 5)
    time.sleep(1)
    pos = pyautogui.position()
    posicoes[nome] = {"x": pos.x, "y": pos.y}
    print(f"\033[95m🧠 [IAuto] \033[94mPosição do {nome} salvo como: {pos}")

# Salvar no arquivo
with open("posicoes.json", "w") as f:
    json.dump(posicoes, f, indent=4)

# Mensagem final estilizada
def mensagem_final():
    root = tk.Tk()
    root.attributes('-topmost', True)
    root.overrideredirect(True)
    root.configure(bg='black')

    largura = 850
    altura = 140
    largura_tela = root.winfo_screenwidth()
    altura_tela = root.winfo_screenheight()
    x = (largura_tela // 2) - (largura // 2)
    y = (altura_tela // 2) - (altura // 2)
    root.geometry(f"{largura}x{altura}+{x}+{y}")

    frame = tk.Frame(root, bg="#1e1e1e", highlightbackground="white", highlightthickness=2)
    frame.place(relx=0.5, rely=0.5, anchor="center", width=largura - 20, height=altura - 20)

    label = tk.Label(
        frame, text="✅ Todas as posições foram salvas com sucesso!",
        font=("Segoe UI", 15, "bold"), fg="white", bg="#1e1e1e", padx=20, pady=10
    )
    label.pack(expand=True, fill="both")

    root.after(3000, root.destroy)
    root.mainloop()

mensagem_final()