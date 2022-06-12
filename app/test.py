from flask import Flask, request, jsonify, make_response
import pickle
from flask_cors import CORS,cross_origin

app = Flask(__name__)
CORS(app)
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = False


@app.route('/',methods=["POST"])
def home():
    request_data = request.get_json()
    print(request_data)
    x_test=[[request_data["age"],request_data["hypertension"],request_data["heartDisease"],request_data["avgGlucose"]]]
    filename = 'stroke_analysis.sav'
    loaded_model = pickle.load(open(filename, 'rb'))
    pred = loaded_model.predict(x_test)
    data=str(pred[0])
    response=jsonify({'data': data})
    # response.headers.add("Access-Control-Allow-Origin", "*")
    return response

@app.route('/register',methods=["POST"])
def register():
    data = "Register post called"
    response = jsonify({'data': data})
    return response


@app.route('/',methods=["GET"])
def come():
    data = "Welcome"
    response = jsonify({'data': data})
    return response

if __name__ == "__main__":
    # app.debug = True
    app.run()


