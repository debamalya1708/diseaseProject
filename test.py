from flask import Flask, jsonify, request
import pickle
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'
# app.config['JSONIFY_PRETTYPRINT_REGULAR'] = False

@app.route('/res')
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



# driver function
if __name__ == '__main__':
    app.run(debug=True)


