import requests
from flask import Flask, render_template, jsonify, request
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/convert', methods=["POST"])
def convert():
    currency = request.form.get('currency')
    payload = {"access_key":"18577cdff577b0376cdf7024fed7b1bd", "symbols":currency}
    response = requests.get("http://data.fixer.io/api/latest",params=payload)

    if response.status_code != 200:
        return jsonify({"success":False})
    
    data = response.json()
    if currency not in data["rates"]:
         return jsonify({"success":False})
        
    return jsonify({"success":True, "rate":data["rates"][currency]})

if __name__ == '__main__':
  app.run(host='127.0.0.1', port=8000, debug=True)
 
