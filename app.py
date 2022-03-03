from flask import Flask
import json 
from urllib.request import urlopen
import logging
from flask import Flask, jsonify, request, app
from datetime import datetime

app = Flask(__name__)
logging.basicConfig(level=logging.DEBUG)
app.logger.info("Rainfall Service started")

def get_config():
    #logging.info("Getting configurations")
    app.logger.info("Getting configurations")
    global rainfall_url, location
    with open('config.json') as config_file:
        config= json.load(config_file)
    rainfall_url= config['rainfall_url']
    location= config['location']


@app.route('/')  
def query_data():
    get_config()  
    app.logger.info("Querying...")
    # store the response of URL
    response = urlopen(rainfall_url)
    # storing the JSON response from url in data
    data_json = json.loads(response.read())
    #print(data_json)
    stations= data_json['metadata']['stations']
    readings = data_json['items'][0]['readings']
    #timestamp = data_json['items'][0]['timestamp']
    for station in stations:
        if station['name']==location:
            print(station['id'])
            retrieved_station= station['id']
    
    for reading in readings:
        if reading['station_id'] == retrieved_station:
            value=reading['value']
            if value > 0:
                weather="Raining"
            else:
                weather="Not Raining"
    now = datetime.now()
    current_time = now.strftime("%H:%M")
    return "{},{},{}mm,{}".format(location, current_time, value, weather )

   