import os
from twilio.rest import Client
account_sid = "AC5d92e3f3196bc6c9fbe9472d496fb474"
auth_token = "db29f68c2d5077bbf09495f055e5e7cc"
client = Client(account_sid, auth_token)
def send_messsage(to:str, message:str):
    client.messages.create(
        from_=os.getenv('FROM'),
        body = message,
        to = to
    )