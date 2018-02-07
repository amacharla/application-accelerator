#!/usr/bin/python3

from flask import Flask
from twilio.rest import Client

app = Flask(__name__)

account_sid = 'ACd91de867ea0bbfcb5d355485aba2f6d8'
auth_token = 'f4d768c7bc020e8c9c60195d32baa9a3'
client = Client(account_sid, auth_token)

#client.api.account.messages.create(
#        to='+19784956909',
#        from_='+13158732742',
#        body="Aria is aliveee")

@app.route("/")
def hello():
    return "Hello World!"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
