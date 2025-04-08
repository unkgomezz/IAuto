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
#   |                                       IAuto Full - Version 1.1 - 08/04/2025 - By Gomezz                                      |
#   |                                       = Using Deep Seek V3, Leonardo AI and Hailuo AI =                                      |
#   |______________________________________________________________________________________________________________________________|

# IAuto 🎶🤖

IAuto é uma automação inteligente que gera vídeos de música usando inteligência artificial. Ele integra três ferramentas poderosas:

- 🎵 **DeepSeek** para geração de letras musicais com IA.
- 🎨 **Leonardo AI** para criação de imagens com base na letra.
- 🎥 **Hailuo AI** para transformar letra + imagem em vídeos animados.

## 📁 Estrutura do Projeto

IAuto/
├── calib.py            # Script de calibração do mouse (posições)
├── config.py           # Configurações de APIs, caminhos e parâmetros
├── letra.txt           # Arquivo com a letra da música
├── main.py             # Automação principal
├── posicoes.json       # Arquivo salvo após calibração
├── requirements.txt    # Dependências do projeto

## ⚙️ Pré-requisitos

- Python 3.10+
- Google Chrome instalado (com perfil configurado)
- Contas nas plataformas:
  - OpenRouter (DeepSeek)
  - Leonardo AI
  - Hailuo AI

## 🔧 Instalação

1. Clone o repositório
```bash
git clone https://github.com/seu-usuario/IAuto.git
cd IAuto
```

2. Crie um ambiente virtual (recomendado)
```bash
python -m venv venv
# Windows:
venv\Scripts\activate
# Linux/macOS:
source venv/bin/activate
```

3. Instale as dependências
```bash
pip install -r requirements.txt
```

4. Configure as APIs e caminhos no `config.py`.

## 🛠️ Variáveis de Configuração (`config.py`)

| Variável                | Descrição |
|-------------------------|----------|
| `openai_api_key`        | Chave da API do DeepSeek (via OpenRouter) |
| `hailuo_api_key`        | Chave da API do Hailuo |
| `leonardo_api_key`      | Chave da API do Leonardo AI |
| `letra_path`            | Caminho do arquivo com a letra (`letra.txt`) |
| `output_path`           | Caminho para salvar o vídeo gerado |
| `chrome_profile_path`   | Caminho do perfil do Google Chrome |
| `prompt_image_default`  | Prompt base para gerar imagem |
| `resolution`            | Resolução do vídeo final |

## ▶️ Como Usar

1. Execute o calibrador de posições (você irá clicar nas áreas necessárias):
```bash
python calib.py
```

2. Escreva ou cole a letra da música no `letra.txt`.

3. Execute o script principal:
```bash
python main.py
```

## ✨ Créditos

💻 Desenvolvido por **Gomezz**  
📅 Versão: 1.1 — 08/04/2025