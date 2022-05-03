import json
from flask import Flask, request, make_response
from flask_restful import Resource, Api
from flask_cors import CORS
import pickle
import pandas as pd

from train_classifier import TrainClassifier

app = Flask(__name__)
CORS(app)
api = Api(app)

categories = ['related', 'request', 'offer', 'aid_related', 'medical_help', 'medical_products', 'search_and_rescue', 'security', 'military', 'child_alone', 'water', 'food', 'shelter', 'clothing', 'money', 'missing_people', 'refugees', 'death',
              'other_aid', 'infrastructure_related', 'transport', 'buildings', 'electricity', 'tools', 'hospitals', 'shops', 'aid_centers', 'other_infrastructure', 'weather_related', 'floods', 'storm', 'fire', 'earthquake', 'cold', 'other_weather', 'direct_report']

# ! WARNING: MAKE SURE YOU START THE REACT SERVER AS WELL.


class MachineLearningResponse(Resource):
    def get(self):
        # load text from url
        text = request.args.get('text')
        print(text)
        # predict
        prediction = model.predict([text])
        # convert prediction list to hash of columns
        prediction_hash = {}
        for i in range(len(prediction[0])):
            # convert to string
            prediction_hash[categories[i]] = str(prediction[0][i])

        print(prediction_hash)

        # return prediction
        # set Access-Control-Allow-Origin: * in the header of the response
        resp = make_response(json.dumps(prediction_hash))
        resp.headers['Access-Control-Allow-Origin'] = '*'
        return resp


api.add_resource(MachineLearningResponse, '/')

if __name__ == '__main__':
    # set list of categories for ease of use.

    model = pickle.load(open('./pickles/cv.pkl', 'rb'))
    app.run(debug=True)