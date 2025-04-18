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
                                                                                                        
# Importações
import time
import traceback
import pyautogui
import openai
import httpx
import os
import glob
import json
import config
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

# Configurações
openai.api_key = config.openai_api_key
openai.api_base = config.openai_api_base
txt_path = config.txt_path
quantidade_prompts = config.quantidade_prompts

# Iniciando o IAuto
def limpar_console():
    os.system('cls' if os.name == 'nt' else 'clear')

limpar_console()
print("\n")
print(f"\033[95m🧠 [IAuto] \033[94mBem-vindo ao IAuto!")
time.sleep(2)
print(f"\033[95m🧠 [IAuto] \033[94mCarregando o sistema:")
time.sleep(2)
print("\n")
print(f"\033[95m🧠 [IAuto] \033[94m3...")
time.sleep(1)
print(f"\033[95m🧠 [IAuto] \033[94m2...")
time.sleep(1)
print(f"\033[95m🧠 [IAuto] \033[94m1...")
time.sleep(1)
limpar_console()
time.sleep(2)
print(f"\033[95m🧠 [IAuto] \033[94mSistema inicializado com sucesso.")
print("\n")

# Função para dividir a letra da música proporcionalmente
def dividir_letra_em_partes(letra, partes):
    linhas = [linha.strip() for linha in letra.strip().split("\n") if linha.strip()]
    total_linhas = len(linhas)
    tamanho_parte = max(1, total_linhas // partes)
    
    resultado = []
    for i in range(partes):
        inicio = i * tamanho_parte
        fim = (i + 1) * tamanho_parte if i < partes - 1 else total_linhas
        parte = "\n".join(linhas[inicio:fim])
        resultado.append(parte)
    return resultado

# Função para gerar os prompts
def gerar_prompts(letra, quantidade):
    prompts_imagem = []
    prompts_video = []

    # Prompt base para imagem
    system_prompt_imagem = (
        "You are an expert at transforming song lyrics into highly visual descriptions for AI image generation. "
        "Images should be in a cartoon-style animation suitable for children. "
        "Each prompt should describe only ONE unique, self-contained scene. "
        "DO NOT include multiple versions, alternate scenes, or extended narratives. "
        "Use short, clear, and playful language suitable for children. "
        "Limit description to a maximum of 3 sentences per prompt. "
        "Your goal is to vividly illustrate the meaning or emotion of the lyrics through a single cartoon-like moment. "
        "Ultra detailed, 32k uhd, 3d rendered style with child-like graphics, computer graphics, colorful elements, vivid, beautiful, fun, 3d modeling. "
        "Always include this at the beginning of all prompts: "
        "'Ultra detailed, 32k uhd, 3d rendered style with childish graphics, CG, colorful elements, vivid, beautiful, fun, 3d modeling.' "
        "Be creative, use background elements and a beautiful and comfortable setting. "
        "Images must maintain logical progression."
    )

    # Prompt base para vídeo (usará como input o prompt da imagem)
    system_prompt_video = (
        "You are an expert at turning descriptions of cartoon images into short animated scene ideas."
        "Describe a short animated scene based on the image prompt, in a kid-friendly cartoon style."
        "Include smooth camera movements, character actions, and fun background animation."
        "Use short, fun sentences, no more than 3 per prompt."
        "Always include this at the beginning:"
        "'Ultra detailed, 32k uhd, 3d rendered style with kid-friendly graphics, CG, colorful elements, vivid, beautiful, fun, 3d modeling.'"
        "Use simple motion prompts."
        "DO NOT make prompts complex."
        "Just do the basics."
    )

    partes_letra = dividir_letra_em_partes(letra, quantidade)
    time.sleep(3)
    print(f"\033[95m🤖 [Deep Seek] \033[94mConectado à API com sucesso.")
    time.sleep(2)

    for i, trecho in enumerate(partes_letra):
        print(f"\033[95m🤖 [Deep Seek] \033[94mGeração do prompt {i+1}/{quantidade} em progresso:")

        # Gera prompt de imagem com base no trecho
        resposta_img = httpx.post(
            "https://openrouter.ai/api/v1/chat/completions",
            headers={
                "Authorization": f"Bearer {openai.api_key}",
                "Content-Type": "application/json"
            },
            json={
                "model": "deepseek/deepseek-chat",
                "messages": [
                    {"role": "system", "content": system_prompt_imagem},
                    {"role": "user", "content": trecho}
                ]
            }
        )

        if resposta_img.status_code == 200:
            prompt_imagem = resposta_img.json()["choices"][0]["message"]["content"].strip()
            print(f"\033[95m🤖 [Deep Seek] \033[94mPrompt de imagem gerado com sucesso.")
            prompts_imagem.append(prompt_imagem)
        else:
            print(f"\033[91m🤖 Erro ao gerar prompt de imagem {i+1}: {resposta_img.text}")
            continue  # pula para o próximo

        # Gera prompt de vídeo baseado no prompt da imagem
        resposta_vid = httpx.post(
            "https://openrouter.ai/api/v1/chat/completions",
            headers={
                "Authorization": f"Bearer {openai.api_key}",
                "Content-Type": "application/json"
            },
            json={
                "model": "deepseek/deepseek-chat",
                "messages": [
                    {"role": "system", "content": system_prompt_video},
                    {"role": "user", "content": prompt_imagem}
                ]
            }
        )

        if resposta_vid.status_code == 200:
            prompt_video = resposta_vid.json()["choices"][0]["message"]["content"].strip()
            print(f"\033[95m🤖 [Deep Seek] \033[94mPrompt de vídeo gerado com sucesso.")
            prompts_video.append(prompt_video)
        else:
            print(f"\033[91m🤖 Erro ao gerar prompt de vídeo {i+1}: {resposta_vid.text}")

        time.sleep(3)

    return prompts_imagem, prompts_video

# Carregamento da letra.txt
if not os.path.exists(txt_path):
    raise FileNotFoundError(f"O arquivo {txt_path} não foi encontrado.")

with open(txt_path, "r", encoding="utf-8") as f:
    letra = f.read()

prompts_imagem, prompts_video = gerar_prompts(letra, quantidade_prompts)

# Selenium Leonardo AI
options = Options()
options.add_argument("--start-maximized")
options.add_argument("--disable-extensions")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--no-sandbox")
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_argument("--disable-infobars")
options.add_experimental_option("excludeSwitches", ["enable-logging"])
options.add_argument(rf"--user-data-dir={config.chrome_user_data_dir}")
options.add_argument(rf"--profile-directory={config.chrome_profile_dir}")

# ! Se quiser rodar em segundo plano (sem abrir janela), descomente:
# ! Sistema desativado no momento! (NÃO ATIVE)
#options.add_argument("--headless")

# Carrega as posições
with open("posicoes.json", "r") as f:
    posicoes = json.load(f)

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
wait = WebDriverWait(driver, 30)

try:
    driver.get("https://app.leonardo.ai/image-generation")
    print("\n")
    print(f"\033[95m🧙‍♂️ [Leonardo AI] \033[94mConectado a API com sucesso.")
    time.sleep(7)

    print(f"\033[95m🧙‍♂️ [Leonardo AI] \033[94mConfigurando resolução da imagem.")
    pre_prompt_button = wait.until(EC.element_to_be_clickable((
        By.XPATH,
        "//div[contains(@id, 'accordion-panel')]/div[5]/div[2]/button[4]/div/div"
    )))
    pre_prompt_button.click()
    time.sleep(2)

    option_button = wait.until(EC.element_to_be_clickable((
        By.XPATH,
        "//div[contains(@id, 'chakra-modal--body')]/div/div[2]/div[4]/div/button[4]"
    )))
    option_button.click()
    time.sleep(1)

    close_modal_button = wait.until(EC.element_to_be_clickable((
        By.XPATH,
        "//div[contains(@id, 'chakra-modal--body')]/div/div[1]/button"
    )))
    close_modal_button.click()
    print(f"\033[95m🧙‍♂️ [Leonardo AI] \033[94mConfigurações aplicadas com sucesso.")
    time.sleep(2)

    for idx, prompt in enumerate(prompts_imagem):
        # 🔒 Fecha o modal pressionando ESC para garantir que o próximo prompt não falhe
        try:
            from selenium.webdriver.common.keys import Keys
            body = driver.find_element(By.TAG_NAME, "body")
            body.send_keys(Keys.ESCAPE)
            time.sleep(2)
            print(f"\033[95m🧙‍♂️ [Leonardo AI] \033[94mA tela foi limpa.")
        except Exception as e:
            print("⚠️ Não foi possível fechar o modal com ESC:", e)

        # 🔄 Aguarda o textarea estar visível e clicável após fechar modal
        prompt_input = wait.until(EC.element_to_be_clickable((By.XPATH, "//textarea")))

        prompt_input.click()
        prompt_input.send_keys(Keys.CONTROL + "a")
        prompt_input.send_keys(Keys.DELETE)
        prompt_input.send_keys(prompt)
        print(f"\033[95m🧙‍♂️ [Leonardo AI] \033[94mPrompt inserido com sucesso.")

        generate_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(., 'Generate')]")))
        generate_button.click()
        print(f"\033[95m🧙‍♂️ [Leonardo AI] \033[94mIniciando geração de imagem.")

        print(f"\033[95m🧙‍♂️ [Leonardo AI] \033[94mAguardando a imagem ser gerada.")
        time.sleep(40)

        x = posicoes["abrir_img"]["x"]
        y = posicoes["abrir_img"]["y"]
        time.sleep(5)
        pyautogui.moveTo(x, y)
        pyautogui.click()
        print(f"\033[95m🧙‍♂️ [Leonardo AI] \033[94mAbrindo imagem.")

        x = posicoes["baixar_img"]["x"]
        y = posicoes["baixar_img"]["y"]
        time.sleep(3)
        pyautogui.moveTo(x, y)
        pyautogui.click()
        print(f"\033[95m🧙‍♂️ [Leonardo AI] \033[94mBaixando imagem.")
        time.sleep(3)

        x = posicoes["fechar_img"]["x"]
        y = posicoes["fechar_img"]["y"]
        time.sleep(3)
        pyautogui.moveTo(x, y)
        pyautogui.click()
        print(f"\033[95m🧙‍♂️ [Leonardo AI] \033[94mFechando imagem.")
    print("\n")

    # Caminho onde as imagens foram salvas pela Leonardo AI
    caminho_imagens = config.caminho_imagens

    imagens_geradas = sorted(
    glob.glob(os.path.join(caminho_imagens, "*.png")) + glob.glob(os.path.join(caminho_imagens, "*.jpg")),
    key=os.path.getmtime
    )   

    print(f"\033[95m🧩 [Hailuo AI] \033[94mConectado a API com sucesso.")
    time.sleep(2)
    print(f"\033[95m🧩 [Hailuo AI] \033[94mTotal de imagens encontradas: {len(imagens_geradas)}")
    time.sleep(2)

    # Abre uma nova aba e acessa o site da Hailuo AI
    driver.execute_script("window.open('');")
    driver.switch_to.window(driver.window_handles[-1])

    # Ordena as imagens pela data de modificação (garante ordem correta de download)
    imagens_geradas = sorted(
        glob.glob(os.path.join(caminho_imagens, "*.png")) + glob.glob(os.path.join(caminho_imagens, "*.jpg")),
        key=os.path.getmtime
    )

    # Para cada imagem
    for idx, imagem_path in enumerate(imagens_geradas):
        driver.get("https://hailuoai.video/create")
        time.sleep(5)

        print(f"\033[95m🧩 [Hailuo AI] \033[94mProcessando imagem {idx + 1}/{len(imagens_geradas)}:")

        # Clica no botão de anexo de imagem
        x = posicoes["anexo_anim"]["x"]
        y = posicoes["anexo_anim"]["y"]
        pyautogui.moveTo(x, y)
        pyautogui.click()
        time.sleep(2)

        # Escreve o caminho da imagem e envia
        pyautogui.write(imagem_path)
        pyautogui.press("enter")
        print(f"\033[95m🧩 [Hailuo AI] \033[94mImagem enviada.")
        time.sleep(8)

        # Clica no campo de texto para inserir o prompt
        x = posicoes["texto_anim"]["x"]
        y = posicoes["texto_anim"]["y"]
        pyautogui.moveTo(x, y)
        pyautogui.click()
        time.sleep(0.5)
        pyautogui.click()

        # Garante que há um prompt disponível para essa imagem
        if idx < len(prompts_video):
            prompt_video = prompts_video[idx]
        else:
            prompt_video = "Gentle children's animation based on a cheerful song."

        pyautogui.write(prompt_video)
        print(f"\033[95m🧩 [Hailuo AI] \033[94mPrompt de vídeo inserido.")
        time.sleep(5)

        # Clica em gerar
        x = posicoes["gerar_anim"]["x"]
        y = posicoes["gerar_anim"]["y"]
        pyautogui.moveTo(x, y)
        pyautogui.click()
        print(f"\033[95m🧩 [Hailuo AI] \033[94mAnimação sendo gerada.")
        time.sleep(300)

        # Clica para abrir vídeo
        x = posicoes["abrir_anim"]["x"]
        y = posicoes["abrir_anim"]["y"]
        pyautogui.moveTo(x, y)
        pyautogui.click()
        print(f"\033[95m🧩 [Hailuo AI] \033[94mVídeo aberto.")
        time.sleep(2)

        # Clica para baixar
        x = posicoes["baixar_anim"]["x"]
        y = posicoes["baixar_anim"]["y"]
        pyautogui.moveTo(x, y)
        pyautogui.click()
        print(f"\033[95m🧩 [Hailuo AI] \033[94mAnimação baixada.")
        time.sleep(5)

    print("\n")
    print(f"\033[95m🧠 [IAuto] \033[94mProcesso finalizado com sucesso.")
    print("\n")

except Exception as e:
    print("❌ Erro durante o processo:", e)
    traceback.print_exc()
    driver.save_screenshot("erro.png")
    print("📸 Screenshot salvo como erro.png")