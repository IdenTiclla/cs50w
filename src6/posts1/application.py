import time
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/posts', methods=["POST"])
def posts():
    start = int(request.form.get("start"))
    end = int(request.form.get("end"))

    posts = []
    
    for i in range(start, end + 1):
        posts.append(f"Post #{i}")

    time.sleep(1)

    return jsonify(posts)
    

if __name__ == '__main__':
  app.run(host='127.0.0.1', port=8000, debug=True)
 