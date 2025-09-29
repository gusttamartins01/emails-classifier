import os
import json
import asyncio
import PyPDF2
from fastapi import FastAPI, Form, File, UploadFile, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from utils.groq_client import gerar_resposta
from utils.nlp_utils import preprocess_text

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def home():
    return {"message": "API funcionando 🚀"}

@app.post("/process")
async def process_email(text: str = Form(None), file: UploadFile = File(None)):
    if not text and not file:
        raise HTTPException(status_code=400, detail="Nenhum texto ou arquivo PDF enviado.")

    # Se enviou um arquivo PDF, extrair o texto
    if file:
        if not file.filename.endswith(".pdf"):
            raise HTTPException(status_code=400, detail="Apenas arquivos PDF são aceitos.")

        try:
            content = await file.read()
            from io import BytesIO
            pdf_reader = PyPDF2.PdfReader(BytesIO(content))

            pdf_text = ""
            for page in pdf_reader.pages:
                pdf_text += page.extract_text() or ""

            text = pdf_text.strip()
            if not text:
                raise HTTPException(status_code=400, detail="Não foi possível extrair texto do PDF.")
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Erro ao ler PDF: {str(e)}")

    # Pré-processar e enviar para IA
    try:
        texto_limpo = preprocess_text(text)
        resultado = await gerar_resposta(text)

        if "Erro" in resultado.get("categoria", ""):
            return JSONResponse(content=resultado, status_code=503)

        return JSONResponse(content=resultado)

    except Exception as e:
        print(f"[ERRO] Falha ao gerar resposta: {str(e)}")
        return JSONResponse(content={
            "categoria": "Erro Interno do Servidor",
            "resposta": "Ocorreu um erro inesperado ao processar o email."
        }, status_code=500)
