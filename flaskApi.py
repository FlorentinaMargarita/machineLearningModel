from flask import Flask
from flask import request

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
        answer = (float(temperature) * -0.00025155 + float(humidity) * -0.00016897 + 0.05235515*float(sound)) - 3.9363930971520107
        return str(answer)
    print(temperature)

