from flask import Flask, request, jsonify, make_response
import pickle
from flask_cors import CORS,cross_origin

app = Flask(__name__)
CORS(app)
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = False


@app.route('/check',methods=["POST"])
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


# def _build_cors_preflight_response():
#     response = make_response()
#     response.headers.add("Access-Control-Allow-Origin", "*")
#     response.headers.add('Access-Control-Allow-Headers', "*")
#     response.headers.add('Access-Control-Allow-Methods', "*")
#     return response
#
# def _corsify_actual_response(response):
#     response.headers.add("Access-Control-Allow-Origin", "*")
#     return response

# driver function

if __name__ == "__main__":
    app.run()


