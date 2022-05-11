import json
import os
from flask import Flask, request, make_response
from flask_restful import Resource, Api
from flask_cors import CORS
import pickle
import pandas as pd

from train_classifier import TrainClassifier

app = Flask(__name__)
cors = CORS(app)
api = Api(app)

categories = ['related', 'request', 'offer', 'aid_related', 'medical_help', 'medical_products', 'search_and_rescue', 'security', 'military', 'child_alone', 'water', 'food', 'shelter', 'clothing', 'money', 'missing_people', 'refugees', 'death',
              'other_aid', 'infrastructure_related', 'transport', 'buildings', 'electricity', 'tools', 'hospitals', 'shops', 'aid_centers', 'other_infrastructure', 'weather_related', 'floods', 'storm', 'fire', 'earthquake', 'cold', 'other_weather', 'direct_report']

# ! WARNING: MAKE SURE YOU START THE REACT SERVER AS WELL.


class MachineLearningResponse(Resource):
    """
    This is the root path of the web server.
    """

    def get(self):
        # load text from url
        text = request.args.get('text')
        if text is None:
            text = 'this is a test'
        # predict
        prediction = model.predict([text])
        # convert prediction list to hash of columns
        prediction_hash = {}
        for i in range(len(prediction[0])):
            # convert to string
            prediction_hash[categories[i]] = str(prediction[0][i])

        # return prediction
        resp = make_response(json.dumps(prediction_hash))
        # disable cors
        resp.headers['Access-Control-Allow-Origin'] = '*'
        # return json
        return resp


class HeartBeat(Resource):
    """
    This is the ping/heartbeat path of the web server.
    """

    def get(self):
        # return heartbeat
        return 'ok'


api.add_resource(MachineLearningResponse, '/')
api.add_resource(HeartBeat, '/heartbeat')

if __name__ == '__main__':
    model = pickle.load(open('./pickles/cv.pkl', 'rb'))
    # get port server is running on
    print("Server is running on port", 5000)
    app.run(debug=True, port=5000)
