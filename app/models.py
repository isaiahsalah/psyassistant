"""
Este módulo dispone de la conexión a la base de datos de Mongo 
y las diferentes operaciones realacionada con la lectura y escritura de datos
"""
from app import app, chatgpt
from flask_pymongo import PyMongo


mongo = PyMongo(app)


def add_chat(msg, phone):
    """Esta función guarda la información de la conversación en la base de datos"""
    # Consulta la existencia del usuario con su numero de Whatsapp
    # en la DB y si existe, se recuperan sus datos
    chat = mongo.db.chat.find_one({'phone': phone})
    # Si ese usuario existe, se actualizará el contexto de la conversacion.
    # Si no se creará una nueva conversación
    if chat:
        # Se añade el nuevo mensaje del usuario al contexto
        chat['messages'].append({"role": "user", "content": msg})
        # Se envia el mensaje a la API de Chatgpt y se guarda la respuesta en una variable
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
        # Se crea una nueva conversación, dandole un contexto
        messages = [chatgpt.context, {"role": "user", "content": msg}]
        # Se manda el contexto de conversación a la API de Chatgpt y se recibe la respuesta
        gpt_response = chatgpt.gpt_response(msg_context=messages)
        # Se añade la respuesta de ChatGPT al contexto o conversación
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
    """En esta función se resetea la conversación"""
    # Se consulta la existencia del usuario en la DB, buscandolo por su número de whatsapp
    chat = mongo.db.chat.find_one({'phone': phone})
    # Creamos el contexto o conversación
    messages = [chatgpt.context, {
        "role": "user", "content": "Saludame y buscame charla"}]
    # Se manda el contexto a la API de Chatgpt y se recibe la respuesta en una variable
    gpt_response = chatgpt.gpt_response(msg_context=messages)
    # Se añade la respuesta de ChatGPT a la conversación
    messages.append(gpt_response)
    # Si ese usuario existe, se reiniciará la conversacion. Si no, se creará una nueva
    if chat:
        # Se reiniciará la conversación en la DB
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
