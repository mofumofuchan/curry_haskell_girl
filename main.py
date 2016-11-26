# coding:utf-8
from flask import Flask, render_template, Response, request, abort
from server.evalProblem import EvalProblem
from functools import wraps
import codecs

app = Flask(__name__)


def consumes(content_type):
    def _consumes(function):
        @wraps(function)
        def __consumes(*argv, **keywords):
            if request.headers['Content-Type'] != content_type:
                abort(400)
            return function(*argv, **keywords)

        return __consumes

    return _consumes


@app.route('/')
def index():
    return render_template('index.html', name="test", title="hello")


@app.route('/quiz/', methods=['POST'])
def quiz_paee():
    return render_template('')


@app.route('/answer/', methods=['POST'])
@consumes('application/json')
def quiz_answer():
    # data = eval(codecs.decode(request.data, 'utf-8'))
    print(request.data)
    data = eval(request.json)
    print(request.data)
    # flag = EvalProblem(data['src']).eval()
    flag = EvalProblem(data['src']).eval()
    print(flag)
    return flag


if __name__ == '__main__':
    app.run(port=8080)
