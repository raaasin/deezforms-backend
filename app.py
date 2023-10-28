
from flask import Flask, jsonify, request
from models.roberta import *
from flask_cors import CORS
from supa import insert_main, edit_data_main, fetch_data,edit_data_scraped,insert_scraped,fetch_data_scraped
import json
app = Flask(__name__)

CORS(app)

@app.route('/', methods=['GET'])
def index():    
    return jsonify({'message': 'Check the URL, also try POST method to /api/custom with a JSON body'})

@app.route('/api/newuser', methods=['POST'])
def newuser():
    data = request.get_json()
    print(data)
    insert_main(data)
    #call selenium to do the stuff
    #store it here
    #insert to another table

@app.route('/api/fetchuser', methods=['POST'])
def fetchuser():
    data = request.get_json()
    retrieval=fetch_data(data)
    return retrieval

@app.route('/api/edituser', methods=['POST'])
def edituser():
    data = request.get_json()
    edit_data_main(data)
    
 
# Define a route for handling POST requests at the '/api/custom' URL
@app.route('/api/fillme', methods=['POST'])
def custom():
    # Retrieve JSON data from the request body
    data = request.get_json()
    print(data)
    scrapy=fetch_data_scraped(data)
    text=scrapy.get("gitscrape")+" "+scrapy.get("linkscrape")
    #return jsonify(text)

    # Check if JSON data is provided; if not, return an error response
    if data is None:
        return jsonify(error='No JSON data provided'), 400

    return get_answers(data,text)
    # Initialize an empty dictionary to store responses



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
