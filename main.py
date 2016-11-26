# coding:utf-8
from flask import Flask, render_template, Response, request, abort
from server.evalProblem import EvalProblem
from functools import wraps

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


@app.route('/quiz', methods=['POST'])
def quiz_paee():
    return render_template('')


@app.route('/answer', methods=['POST'])
@consumes
def quiz_answer():
    src = request.json['src']
    flag = EvalProblem(src).eval()
    print(flag)


if __name__ == '__main__':
    app.run(port=8080)
