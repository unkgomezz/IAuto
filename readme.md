# IAuto 🎶🤖

IAuto é uma automação inteligente que gera vídeos de música usando inteligência artificial. Ele integra três ferramentas poderosas:

- 🎵 **DeepSeek** para geração de letra de música.
- 🎨 **Leonardo AI** para gerar imagens baseadas na letra.
- 🎥 **Hailuo AI** para transformar a imagem e a letra em um vídeo animado.

## 📁 Estrutura do Projeto

```
IAuto/
├── calib.py            # Script de calibração das posições do mouse
├── config.py           # Configurações de API e arquivos
├── letra.txt           # Arquivo onde a letra da música é salva
├── main.py             # Sistema principal de automação
├── posicoes.json       # Arquivo gerado com as posições calibradas do mouse
├── requirements.txt    # Dependências do projeto
```

## ⚙️ Pré-requisitos

- Python 3.10 ou superior
- Google Chrome instalado (usando perfil específico configurado)
- Conta nas plataformas: OpenRouter (DeepSeek), Leonardo AI e Hailuo AI

## 🔧 Instalação

1. Clone o repositório
```bash
git clone https://github.com/seu-usuario/IAuto.git
cd IAuto
```

2. Crie um ambiente virtual (opcional, mas recomendado)
```bash
python -m venv venv
venv\Scripts\activate  # No Windows
```

3. Instale as dependências
```bash
pip install -r requirements.txt
```

4. Configure as APIs e caminhos no `config.py`.

5. Rode o calibrador:
```bash
python calib.py
```

6. Depois de calibrar, coloque a letra da música em `letra.txt`.

7. Execute o sistema:
```bash
python main.py
```

## 🧠 Funcionalidades

- Geração automática de letra de música com IA
- Geração de imagem com Leonardo AI
- Geração de vídeo com animação com Hailuo AI
- Tudo automatizado com simulação de mouse (pyautogui)

## ✨ Créditos

💻 Desenvolvido por Gomezz | 2025