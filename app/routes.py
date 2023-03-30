"""

Este módulo contiene funciones útiles para crear la API.

"""

from app import app, models, whatsapp
from flask import request


@app.route('/webhook', methods=['POST'])
def webhook():
    """Este módulo contiene funciones útiles para crear la API."""

    body = request.get_json()

    if body['object']:
        if body['entry'] and body['entry'][0]['changes'] and body['entry'][0]['changes'][0] and body['entry'][0]['changes'][0]['value']['messages'] and body['entry'][0]['changes'][0]['value']['messages'][0]:

            phone_number_id = body['entry'][0]['changes'][0]['value']['metadata']['phone_number_id']
            from_number = body['entry'][0]['changes'][0]['value']['messages'][0]['from']
            msg_body = body['entry'][0]['changes'][0]['value']['messages'][0]['text']['body']

            if msg_body == "/exit":
                response = models.new_chat(phone=from_number)
            else:
                response = models.add_chat(msg=msg_body, phone=from_number)

            whatsapp.send_msg(
                from_number=from_number,
                phone_number_id=phone_number_id,
                respons=response)
        return 'Success', 200
    else:
        return 'Not Found', 404


@app.route('/webhook')
def verify():
    """Este módulo contiene funciones útiles para crear la API."""
    mode = request.args.get('hub.mode')
    token = request.args.get('hub.verify_token')
    challenge = request.args.get('hub.challenge')
    response = whatsapp.verify_webhook(
        challenge=challenge, mode=mode, token=token)
    return response
