"""ola"""
import json
import requests
from app import app


token_whats = app.config['API_KEY_WHATS']
verify_token = app.config['VERIFY_TOKEN']


def send_msg(phone_number_id, from_number, respons):
    """ola"""
    payload = json.dumps({
        'messaging_product': 'whatsapp',
        "recipient_type": "individual",
        'to': from_number,
        "type": "text",
        'text': {
            "preview_url": False,
            'body': respons}
    })
    headers = {
        'Content-Type': 'application/json'
    }

    requests.post(
        f'https://graph.facebook.com/v16.0/{phone_number_id}/messages?access_token={token_whats}',
        headers=headers,
        data=payload
    )


def verify_webhook(mode, token, challenge):
    """ola"""
    if mode and token:
        if mode == 'subscribe' and token == verify_token:
            print('WEBHOOK_VERIFIED')
            return challenge, 200
        else:
            return 'Verification token mismatch', 403
    else:
        return 'Bad request', 400
