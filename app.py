from flask import Flask, jsonify, request 
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/', methods=['GET','POST'])
def landingPage(sensors):
    # return jsonify({'name':"Prateek Mahajan"})
    return sensors
    data = request.get_json()
    print(data)
    return jsonify(data)

if __name__=='__main__':
	app.run(debug=True)