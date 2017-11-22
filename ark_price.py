import logging
from flask import Flask, render_template
from flask_ask import Ask, statement, question, session
import requests
import os

app = Flask(__name__)

ask = Ask(app, "/")

logger = logging.getLogger()


@ask.launch
def launch():
    return ark_price()


@ask.intent("DeludedIntent")
def ark_price():
    r = requests.get("https://api.coinmarketcap.com/v1/ticker/ark/")
    if r.status_code == 200:
        price = r.json()[0]["price_usd"]
        speech = "The conference yesterday revealed to the world the stuttering potheads that run this scam. Price has already tanked 10%. Once it breaks through the $1.50 resistance the panic will begin and small holders and speculators will begin to offload, with the whales already long gone. Once it shoots through the $1 mark, unabated FEAR will ripe through all ARKies. With all those who dumped their current accounts into this scam twitching at their arsehole continuously while refreshing bittrex. The $0.50 mark will be met, the largest panic in history will ensue. The final deluded Nodes will begin to go offline, and wagecuckers with their engineering salaries loaded up in ARK will be left with it stuck in their wallet unable to move it to bittrex to salvage some self respect. The price WILL tank at this point to sub $0.10, and most probably sub ICO levels. From that day forward the deluded Arkie wagecucking engineering nerds who bought this coin thinking it had fundamentals will go back to their jobs, with no money in their current accounts, to be made redundant by the next wave of pajeets arriving to undercut their wages. Deluded AKies will hold bags FOREVER, with no job, no money, and no crypto. I warned you ARKies. There's still time to get out. Sell NOW. Dont be deluded, dont be an ARKie."
    logger.info('speech = {}'.format(speech))
    return statement(speech)

@ask.intent("ArkPriceIntent")
def ark_price():
    r = requests.get("https://api.coinmarketcap.com/v1/ticker/ark/")
    if r.status_code == 200:
        price = r.json()[0]["price_usd"]
        speech = "The price of Ark is {0:.2f} $".format(float(price))
    logger.info('speech = {}'.format(speech))
    return statement(speech)


@ask.intent('AMAZON.HelpIntent')
def help():
    speech_text = 'You can say hello to me!'
    return question(speech_text).reprompt(speech_text).simple_card('ArkPrice', speech_text)


@ask.session_ended
def session_ended():
    return "{}", 200

if __name__ == '__main__':
    if 'ASK_VERIFY_REQUESTS' in os.environ:
        verify = str(os.environ.get('ASK_VERIFY_REQUESTS', '')).lower()
        if verify == 'false':
            app.config['ASK_VERIFY_REQUESTS'] = False
    app.run(debug=True)
