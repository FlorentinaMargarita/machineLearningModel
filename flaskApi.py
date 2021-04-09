from flask import Flask
from flask import request
import logging

app = Flask(__name__)

@app.route('/')
def run_model():
    temperature = (request.args.get('temperature')) or 0
    humidity = request.args.get('humidity') or 0
    sound = request.args.get('sound') or 0
    password = request.args.get('password')

    # These parameters used below were found when running the machine learning model.
    if password != 'secret':
        return "You're an intruder! BACK OFF!!!"
    
    else:  
        answerValue = (float(temperature) * -0.00025155 + float(humidity) * -0.00016897 + 0.05235515*float(sound)) - 3.9363930971520107
        problemStatus = 'no'

        if answerValue > 0.5:
            problemStatus = 'a huge'
        answer = 'The value is %s so there is %s problem in the factory.' % (answerValue, problemStatus)
        return str(answer)

# it should write the numbers it gets to a file. We want to write surprising numbers. If one of the features are 5 and more out of range, 
# of original ranges than it should write a line to this file
logging.basicConfig(filename='factoryProblem.log', encoding='utf-8', level=logging.DEBUG)
logging.debug('This message should go to the log file')
logging.info('So should this')