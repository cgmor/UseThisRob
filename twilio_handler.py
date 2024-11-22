import os
from twilio.rest import Client
from app import twilioClient

def send_text(poop):
    message = twilioClient.messages.create(body='Test message from demo script',
    from_='+17039366577',
    to='+17037270516')
    print(message.sid)
    print(message.body)
    
