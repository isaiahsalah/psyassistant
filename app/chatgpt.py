"""
Este módulo sirve para comunicarme con la api de ChatGPT 
y recibir una respueste de este
"""
import openai
from app import app


# Api Key de OpenAI
openai.api_key = app.config['API_KEY_GPT']

# Asignamos rol de conversación al asistente
context = {
    "role": "system",
    "content": app.config['CONTEXT_GTP']}

def gpt_response(msg_context):
    """
    Esta función recibe un mensaje y lo manda a ChatGPT. 
    Este responde y se retorna esa respuesta
    """
    # Se manda el mensage a travez de la API de ChatGPT y se recupera la respuesta de este.
    gpt_resp = openai.ChatCompletion.create(
        model="gpt-3.5-turbo", messages=msg_context)
    # Se extrae el mensaje de la respuesta de ChatGPT.
    response = gpt_resp["choices"][0]["message"]
    # Se retorna el mensaje de la API de ChatGPT
    return response
