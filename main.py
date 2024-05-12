from flask import Flask, request, jsonify
from flask_cors import CORS
import lights as l



app = Flask(__name__)
CORS(app)
data = ""
rsc = 200
#403 forbidden
#200 ok



def check():
    l.operate(data.lower())

@app.route('/recieve-output', methods=['GET'])
def send_return():
    x = l.operate(data)
    return jsonify(x), rsc

@app.route('/sent-op', methods=['POST'])
def recieve_op():
    global data
    if request.method == 'POST':
        data = request.json.get('data')
        print(data)
        
        check()

        return jsonify({"message": "Data received successfully"}), rsc



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8899, debug=True)