import os
from twilio.rest import Client
# account_sid = 
# auth_token = 
client = Client(account_sid, auth_token)
def send_messsage(to:str, message:str):
    client.messages.create(
        from_=os.getenv('FROM'),
        body = message,
        to = to
    )
