"""ola"""
from app import app, chatgpt
from flask_pymongo import PyMongo


mongo = PyMongo(app)


def add_chat(msg, phone):
    """ola"""
    # Consulta la existencia del user en la DB
    chat = mongo.db.chat.find_one({'phone': phone})
    # Si ese User existe, se actualizará el contexto de la conversacion. Si no se creará
    if chat:
        # Se añade el nuevo mensaje del user al contexto
        chat['messages'].append({"role": "user", "content": msg})
        # Se hace la petición a la API de Chatgpt y se recibe la respuesta
        gpt_response = chatgpt.gpt_response(msg_context=chat['messages'])
        # Se añade la respuesta de ChatGPT al contexto
        chat['messages'].append(gpt_response)
        # Se actualiza la conversación en la DB
        mongo.db.chat.update_one(
            {'phone': phone},
            {
                "$set":
                {
                    'messages': chat['messages']
                }
            }
        )
        # Se devuelve la respuesta de ChatGPT
        return gpt_response.content
    else:
        # Creamos el contexto
        messages = [chatgpt.context, {"role": "user", "content": msg}]
        # Se hace la petición a la API de Chatgpt y se recibe la respuesta
        gpt_response = chatgpt.gpt_response(msg_context=messages)
        # Se añade la respuesta de ChatGPT al contexto
        messages.append(gpt_response)
        # Se crea la nueva conversación
        mongo.db.chat.insert_one(
            {
                'phone': phone,
                'messages': messages
            }
        )
        # Se devuelve la respuesta de ChatGPT
        return gpt_response.content


def new_chat(phone):
    """ola"""
    # Consulta la existencia del user en la DB
    chat = mongo.db.chat.find_one({'phone': phone})
    # Creamos el contexto
    messages = [chatgpt.context, {
        "role": "user", "content": "Saluda y presentate en muy pocas palabras y hazme un pregunta"}]
    # Se hace la petición a la API de Chatgpt y se recibe la respuesta
    gpt_response = chatgpt.gpt_response(msg_context=messages)
    # Se añade la respuesta de ChatGPT al contexto
    messages.append(gpt_response)
    # Si ese User existe, se actualizará el contexto de la conversacion. Si no se creará
    if chat:
        # Se actualiza la conversación en la DB
        mongo.db.chat.update_one(
            {'phone': phone},
            {
                "$set":
                {
                    'messages': messages
                }
            }
        )
        # Se devuelve la respuesta de ChatGPT
        return gpt_response.content
    else:
        # Se crea la nueva conversación
        mongo.db.chat.insert_one(
            {
                'phone': phone,
                'messages': messages
            }
        )
        # Se devuelve la respuesta de ChatGPT
        return gpt_response.content
