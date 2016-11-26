# coding:utf-8
from flask import Flask, render_template, Response, request, abort
from server.evalProblem import EvalProblem
from functools import wraps
import codecs
import json

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
    print(codecs.decode(request.data, 'utf-8'))
    data = eval(codecs.decode(request.data, 'utf-8'))
    flag = EvalProblem(data['src']).eval()
    data['user_problem_ans'] = flag
    response = json.dumps(data, ensure_ascii=False, sort_keys=True)
    return Response(response, mimetype='application/json')


if __name__ == '__main__':
    app.run(port=8080)
