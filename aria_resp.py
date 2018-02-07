#!/usr/bin/python3

import subprocess
import random
from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)

@app.route("/incoming_sms", methods=['GET', 'POST'])
def incoming_sms():
    "responseds to sms via webhooks"

    body = request.values.get('Body', None) # get sent text
    resp = MessagingResponse() # start response

    reply = action(body)
    print(reply)
    resp.message(reply) # convert to twiml
    return str(resp)

# =========LOGIC=========

def action(body):
    """ If action stated then preforme service else have convo """
    #capture and get rid of prefix
    cmd = body.split()[0]
    package = body.replace(cmd, '')
    return {
            'start': start_service(package),
            'stop': stop_service(package),
            }.get(cmd.lower(), convo(body))

def start_service(package):
    output = subprocess.check_output(["docker-compose", "up"])
    print(output)
    return "Starting " + package + '!'

def stop_service(package):
    return "Stopping " + package + '!'

def convo(sentence):
        """If any of the words in the user's input was a greeting, return a
        greeting response"""

        # Sentences we'll respond with if the user greeted us
        GREETING_KEYWORDS = ["hello", "hi", "greetings", "sup", "what's up",
                             "aria", "hola"]
        GREETING_RESPONSES = ["Hi Anoop!", "hey!", "*nods*", "hey Anoop, you get my snap?"]

        for word in sentence.split():
            if word.lower() in GREETING_KEYWORDS:
                return random.choice(GREETING_RESPONSES)

if __name__ == "__main__":
    app.run(debug=True)
