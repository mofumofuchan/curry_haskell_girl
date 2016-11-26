from flask import Flask, jsonify
app = app = Flask(__name__);

@app.route('/', methods=['POST'])
def index():
    result = {
        "Result": {
            "Greeting": "s"
        }
    }
    return jsonify(result)

app.run(port=12345)


