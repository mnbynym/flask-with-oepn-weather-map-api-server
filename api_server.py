from flask import Flask, jsonify, abort, request
from flask_cors import CORS
import requests
import json

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False
CORS(app)

APP_ID = "YOUR_KEY"
BASE_URL = "http://api.openweathermap.org/data/2.5/weather?q={city}&appid={app_id}"

@app.route('/weather/<string:city>', methods=['GET'])
def get_all(city):
	request_url = BASE_URL.format(city=city, app_id=APP_ID)
	result = requests.get(request_url)
	return jsonify(json.loads(result.text)), 200

if __name__ == "__main__":
    app.run(debug=True)