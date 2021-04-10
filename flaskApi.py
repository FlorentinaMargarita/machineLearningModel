from flask import Flask
from flask import request
import logging

app = Flask(__name__)
logging.basicConfig(filename='factoryProblem.log', level=logging.DEBUG, format='{asctime} {message}', style='{')
logger = logging.getLogger()

@app.route('/')
def run_model():
    temperature = request.args.get('temperature')
    humidity = request.args.get('humidity') 
    sound = request.args.get('sound') 
    password = request.args.get('password')

    if password != 'secret':
        return "You're an intruder! BACK OFF!!!"
    
    else:  
        if float(temperature) > 30:
            logger.info('temperature is out of range')
        if float(humidity) > 50:
            logger.info('humidity is out of range')
        if float(sound) > 100:
            logger.info('sound is out of range')
            
        # These parameters used below were found when running the machine learning model.
        answerValue = (float(temperature) * -0.00025155 + float(humidity) * -0.00016897 + 0.05235515*float(sound)) - 3.9363930971520107
        problemStatus = 'no'

        if answerValue > 0.5:
            problemStatus = 'a huge'
        answer = 'The value is %s so there is %s problem in the factory.' % (answerValue, problemStatus)
        return str(answer)

# it should write the numbers it gets to a file. We want to write surprising numbers. If one of the features are 5 and more out of range, 
# of original ranges than it should write a line to this file
