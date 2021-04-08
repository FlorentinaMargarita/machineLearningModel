from flask import Flask
from flask import request


app = Flask(__name__)

@app.route('/')
def hello_world():
    temperature = request.args.get('temperature')
    humidity = request.args.get('humidity')
    sound = request.args.get('sound')

    # request is an object provided by flask. It has data about the incoming request. 

    # These parameters used below were found when running the machine learning model.
    answer = (float(temperature) * -0.00025155 + float(humidity) * -0.00016897 + 0.05235515*float(sound)) - 3.9363930971520107
    return str(answer)
   