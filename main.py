# coding:utf-8
from flask import Flask, render_template, Response, request, abort, g
from contextlib import closing
from server.evalProblem import EvalProblem
from functools import wraps
import sqlite3
import json

DATABASE = './curry_haskell_girl.db'
app = Flask(__name__)
app.config.from_object(__name__)

#connect
def connect_db():
   return sqlite3.connect(app.config['DATABASE'])

#init
def init_db():
   with closing(connect_db()) as db:
       with app.open_resource('schema.sql', mode='r') as f:
           db.cursor().executescript(f.read())
       db.commit()

@app.before_request
def before_request():
   g.db = connect_db()


@app.teardown_request
def teardown_request(exeption):
   db = getattr(g, 'db', None)
   if db is not None:
       db.close()

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
    data = {
        'id': request.json['id'],
        'src': request.json['src']
    }
    flag = EvalProblem(data['src']).eval()
    if flag:
        quiz_true(data['id'])

    data['user_problem_ans'] = flag
    response = json.dumps(data, ensure_ascii=False, sort_keys=True)
    return Response(response, mimetype='application/json')

def quiz_true(id):
    g.db.execute("update user_ans set result_flag=? where quiz_id=?", (1, id))
    g.db.commit()


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8080, debug=True)
