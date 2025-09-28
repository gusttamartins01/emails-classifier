from fastapi import FastAPI, Form, HTTPException
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
async def process_email(text: str = Form(...)):
    if not text.strip():
        raise HTTPException(status_code=400, detail="O conteúdo do email está vazio.")

    try:
    
        texto_limpo = preprocess_text(text)

        resultado = await gerar_resposta(text)

        if "Erro" in resultado.get("categoria", ""):
            return JSONResponse(content={
                "categoria": resultado["categoria"],
                "resposta": resultado["resposta"]
            }, status_code=503)

        return JSONResponse(content={
            "categoria": resultado["categoria"],
            "resposta": resultado["resposta"]
        })

    except Exception as e:
        print(f"[ERRO] Falha ao gerar resposta: {str(e)}")
   
        return JSONResponse(content={
            "categoria": "Erro Interno do Servidor",
            "resposta": "Ocorreu um erro inesperado ao processar o email. Verifique o log do servidor."
        }, status_code=500)