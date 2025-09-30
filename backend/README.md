
---

# 📬 EMAIL-CLASSIFIER

Sistema inteligente de classificação de emails que identifica se uma mensagem é **Produtiva** ou **Improdutiva**, e gera uma resposta empática e profissional. Ideal para equipes de suporte, triagem de mensagens ou atendimento ao cliente.

---

## 🧠 Visão Geral

Este projeto full-stack combina:

- **Backend** com FastAPI + Groq API (modelo LLaMA 3.1)
- **Frontend** com HTML, CSS e JavaScript
- **NLP com spaCy** para pré-processamento de texto
- **Exportação em PDF** com jsPDF

---

## 🗂️ Estrutura do Projeto

```plaintext
EMAIL-CLASSIFIER/
├── backend/
│   ├── main.py                 # API principal
│   ├── utils/
│   │   ├── groq_client.py      # Integração com Groq
│   │   └── nlp_utils.py        # NLP com spaCy
│   └── venv/                   # Ambiente virtual Python
├── frontend/
│   ├── index.html              # Interface web
│   ├── style.css               # Estilo visual
│   ├── script.js               # Lógica JS
│   └── README.md               # Documentação
├── .env                        # Chave da API Groq
├── requirements.txt            # Dependências Python
├── LICENSE                     # Licença MIT
└── .gitignore                  # Arquivos ignorados pelo Git
```

---

## ⚙️ Backend (FastAPI + Groq)

### Funcionalidade

- Recebe o conteúdo do email via POST
- Pré-processa o texto com spaCy
- Envia para a Groq API usando o modelo `llama-3.1-8b-instant`
- Retorna a **categoria** e uma **resposta sugerida** em JSON

### Dependências

```txt
fastapi
uvicorn[standard]
httpx
python-dotenv
nltk
transformers
python-multipart
spacy
```

### Instalação

1. Crie e ative o ambiente virtual:

```bash
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows
```

2. Instale as dependências:

```bash
pip install -r requirements.txt
python -m spacy download pt_core_news_sm
```

3. Crie o arquivo `.env` com sua chave da Groq:

```
GROQ_API_KEY="sua-chave-aqui"
```

### Execução

```bash
uvicorn main:app --reload
```

A API estará disponível em: [http://localhost:8000](http://localhost:8000)

### Documentação da API

- Swagger: [http://localhost:8000/docs](http://localhost:8000/docs)
- ReDoc: [http://localhost:8000/redoc](http://localhost:8000/redoc)

---

## 🎨 Frontend (HTML + CSS + JS)

### Funcionalidade

- Interface amigável para colar o conteúdo do email
- Botão para classificar via API
- Exibe resultado com categoria e resposta
- Permite exportar o resultado em PDF
- Responsivo para dispositivos móveis

### Como usar

1. Abra `frontend/index.html` no navegador
2. Cole o conteúdo do email
3. Clique em **Classificar**
4. Veja o resultado e exporte em PDF se desejar

---

## 🧪 Exemplo de Uso

### Entrada:
```text
Olá, estou com dificuldades para acessar minha conta bancária pelo aplicativo. Podem me ajudar?
```

### Saída:
```json
{
  "categoria": "Produtivo",
  "resposta": "Olá! Sentimos muito pela dificuldade. Podemos te ajudar com o acesso ao aplicativo bancário. Por favor, informe o modelo do seu celular e o sistema operacional (Android/iOS) para orientarmos melhor."
}
```

---

## 📦 Requisitos

- Python 3.11+
- Navegador moderno (Chrome, Firefox, Edge)
- Conexão com a internet (para acessar a Groq API)
- Chave válida da Groq (obtenha em [groq.com](https://groq.com))

---

## 📄 Licença

Este projeto está sob a licença MIT. Você pode usar, modificar e distribuir livremente.

```text
MIT License

Copyright (c) 2025 gustta

Permission is hereby granted, free of charge, to any person obtaining a copy...
```

---

## 📁 .gitignore

```plaintext
# Python
__pycache__/
*.py[cod]
*.env
venv/

# VSCode
.vscode/

# Logs
*.log

# OS
.DS_Store
Thumbs.db
```
----


<br>
<br>

# 📬 EMAIL-CLASSIFIER — English Version 🇬🇧


An intelligent email classification system that identifies whether a message is Productive or Unproductive, and generates a professional, empathetic response. Ideal for support teams, message triage, or customer service.

---

## 🧠 Project Overview

This full-stack project combines:

- **Backend**: FastAPI + Groq API (LLaMA 3.1 model)
- **Frontend**: HTML, CSS, JavaScript
- **NLP**: spaCy for text preprocessing
- **PDF Export**: jsPDF for downloadable results

---

## 🗂️ Project Structure

```plaintext
EMAIL-CLASSIFIER/
├── backend/
│   ├── main.py                 # FastAPI server
│   ├── utils/
│   │   ├── groq_client.py      # Groq integration
│   │   └── nlp_utils.py        # NLP preprocessing
│   └── venv/                   # Python virtual environment
├── frontend/
│   ├── index.html              # Web interface
│   ├── style.css               # Styling
│   ├── script.js               # Frontend logic
│   └── README.md               # Documentation
├── .env                        # Groq API key
├── requirements.txt            # Python dependencies
├── LICENSE                     # MIT license
└── .gitignore                  # Git ignore rules
```

---

## ⚙️ Backend (FastAPI + Groq)

### Features

- Receives email content via POST
- Preprocesses text using spaCy
- Sends request to Groq API using `llama-3.1-8b-instant` model
- Returns a **category** and a **suggested response** in JSON format

### Dependencies

```txt
fastapi
uvicorn[standard]
httpx
python-dotenv
nltk
transformers
python-multipart
spacy
groq
```

### Setup Instructions

1. Create and activate a virtual environment:

```bash
python -m venv venv
source venv/bin/activate  # macOS/Linux
venv\Scripts\activate     # Windows
```

2. Install dependencies:

```bash
pip install -r requirements.txt
python -m spacy download pt_core_news_sm
```

3. Create a `.env` file with your Groq API key:

```
GROQ_API_KEY="your-key-here"
```

### Run the Server

```bash
uvicorn main:app --reload
```

API will be available at: [http://localhost:8000](http://localhost:8000)

### API Documentation

- Swagger: [http://localhost:8000/docs](http://localhost:8000/docs)
- ReDoc: [http://localhost:8000/redoc](http://localhost:8000/redoc)

---

## 🎨 Frontend (HTML + CSS + JS)

### Features

- User-friendly interface to paste email content
- Button to classify via API
- Displays result with category and suggested response
- Allows PDF export of the result
- Fully responsive for mobile devices

### How to Use

1. Open `frontend/index.html` in your browser
2. Paste the email content
3. Click **Classify**
4. View the result and optionally export it as a PDF

---

## 🧪 Example

### Input:
```text
Hi, I'm having trouble accessing my bank account through the app. Can you help me?
```

### Output:
```json
{
  "category": "Productive",
  "response": "Hello! We're sorry to hear you're having trouble. We can help you access your banking app. Please let us know your phone model and operating system (Android/iOS) so we can guide you better."
}
```

---

## 📦 Requirements

- Python 3.11+
- Modern browser (Chrome, Firefox, Edge)
- Internet connection (to access Groq API)
- Valid Groq API key (get one at [groq.com](https://groq.com))

---

## 📄 License

This project is licensed under the MIT License. You are free to use, modify, and distribute it.

```text
MIT License

Copyright (c) 2025 gustta

Permission is hereby granted, free of charge, to any person obtaining a copy...
```

---

## 📁 .gitignore

```plaintext
# Python
__pycache__/
*.py[cod]
*.env
venv/

# VSCode
.vscode/

# Logs
*.log

# OS
.DS_Store
Thumbs.db
```

---
