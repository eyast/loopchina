from flask import Flask
from twilio.twiml.voice_response import VoiceResponse

app = Flask(__name__)


@app.route("/answer", methods=['GET', 'POST'])
def answer_call():
    """Respond to incoming phone calls with a brief message."""
    # Start our TwiML response
    resp = VoiceResponse()

    # Read a message aloud to the caller
    #resp.say("Thank you for calling! Have a great day.", voice='alice')
    resp.play("https://loopchina.blob.core.windows.net/loopchina/china.mp3", loop=0)
    return str(resp)

if __name__ == "__main__":
    app.run(debug=True)