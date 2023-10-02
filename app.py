from openai_api import text_complition
from twilio_api import send_messsage
from flask import Flask, request

app = Flask(__name__)
@app.route('/')
def home():
    return 'All is well...'

@app.route('/twilio/receiveMessage', methods=['POST'])
def recieveMessage():
    try:
        message = request.form['Body']
        sender_id = request.form['From']
        result = text_complition(message)
        if result['status'] == 1:
            send_messsage(sender_id, result['response'])
    except:
        pass
    return 'OK', 200