"""ola"""
import openai
from app import app


# Api Key de OpenAI
openai.api_key = app.config['API_KEY_GPT']

# Contexto de conversación del asistente
context = {"role": "system", "content": "Eres un asistente psicológico de nombre Sofia"}
messages = [context]


def gpt_response(msg_context):
    """ola"""
    
    # Añadir mensaje de whatsapp al contexto de conversación
    #msg_context.append({"role": "user", "content": new_msg})
    
    # LLamada a la API de ChatGPT
    gpt_resp = openai.ChatCompletion.create(
        model="gpt-3.5-turbo", messages=msg_context)
    # Respuesta de la API de ChatGPT
    
    response = gpt_resp["choices"][0]["message"]
    # Añadir mensaje de la API de ChatGPT al contexto de conversación
    # msg_context.append(response)
    # Retornar mensaje de la API de ChatGPT
    return response
