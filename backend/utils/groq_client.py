import os
import json
from dotenv import load_dotenv
from groq import Groq, APIError 
import asyncio 

load_dotenv()
client = Groq()

async def gerar_resposta(texto: str):
    if not os.getenv("GROQ_API_KEY"):
        return {
            "categoria": "Erro",
            "resposta": "Chave da API (Groq) não encontrada. Verifique o arquivo .env."
        }

    MODEL = "llama-3.1-8b-instant" 

    response = await asyncio.to_thread(
        client.chat.completions.create,
        model=MODEL,
        response_format={"type": "json_object"},
        messages=[
            {
                "role": "system",
                "content": (
                    "Você é um assistente profissional que classifica emails como 'Produtivo' ou 'Improdutivo'. "
                    
                    "**Regras de Classificação:** "
                    "1. Classifique como 'Produtivo' se o email contiver dúvidas, pedidos de ajuda, solicitações de suporte técnico, orientações sobre uso de aplicativos, plataformas, bancos, softwares, criação de contas ou e-mails, ou qualquer demanda voltada ao trabalho, tecnologia ou assistência prática. "
                    "2. Classifique como 'Produtivo' também se o email demonstrar necessidade de acolhimento, como relatos de dificuldades pessoais, pedidos de autoajuda ou suporte emocional — desde que haja intenção clara de receber ajuda. "
                    "3. Classifique como 'Improdutivo' se o email for composto por saudações genéricas ('boa noite', 'tudo bem'), mensagens informais sem objetivo claro, spam, ou assuntos pessoais irrelevantes para suporte ou orientação. "
                    
                    "Gere uma resposta profissional, empática, humanizada e acessível, que ofereça ajuda, direcione soluções e incentive autonomia. "
                    "**Regras de Resposta:** Sempre retorne APENAS um objeto JSON com os campos 'categoria' e 'resposta'. NUNCA inclua texto adicional ou formatação Markdown (```json). "
                    "Exemplo: {'categoria': 'Produtivo', 'resposta': '...'}"
                )
            },
            {
                "role": "user",
                "content": "Classifique o seguinte email: " + texto
            }
        ],
        temperature=0.0
    )
        
    resposta_raw = response.choices[0].message.content.strip()

    try:
            resposta_json = json.loads(resposta_raw) 
            
            if isinstance(resposta_json, dict) and "categoria" in resposta_json and "resposta" in resposta_json:
                return resposta_json
            else:
                return {
                    "categoria": "Classificado pela IA (JSON Inválido)",
                    "resposta": resposta_raw
                }

    except json.JSONDecodeError:
            return {
                "categoria": "Classificado pela IA (Erro de Parsing)",
                "resposta": resposta_raw
            }

    except APIError as e:
        
        api_error_message = getattr(e.response, 'text', str(e.body)) if e.response else str(e)
        print(f"[ERRO] Erro da API da Groq: {e}")
        return {
            "categoria": "Erro da API",
            "resposta": f"A API da Groq retornou um erro: {e.status_code} - {api_error_message}"
        }
    except Exception as e:
        print(f"[ERRO] Falha geral: {e}")
        return {
            "categoria": "Erro de Conexão",
            "resposta": "Não foi possível conectar à Groq. Verifique sua chave ou conexão."
        }