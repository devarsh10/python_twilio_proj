from twilio.rest import Client
from config import account_sid, auth_token, phone_number

def twilio_connection(account_sid, auth_token):
  client = Client(account_sid, auth_token)
  return client

def send_whatsapp_text(client,ques):
  message = client.messages.create(
    from_='whatsapp:+14155238886',
    body=ques,
    to=f'whatsapp:{phone_number}'
  )

  return message.sid

client=twilio_connection(account_sid,auth_token)