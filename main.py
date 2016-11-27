# coding:utf-8
from flask import Flask, render_template, Response, request, abort, g
from contextlib import closing
from server.evalProblem import EvalProblem
from functools import wraps
import sqlite3
import json

DATABASE = '/Users/sh07_bell/tmp/curry_haskell_girl/curry_haskell_girl.db'
app = Flask(__name__)
app.config.from_object(__name__)

USER_ID = 1
TRUE_NUMBER = 1

""" ----- quiz ----- """
""" ----- SQL ----- """


def connect_db():
    return sqlite3.connect(app.config['DATABASE'])


def init_db():
    with closing(connect_db()) as db:
        with app.open_resource('schema.sql', mode='r') as f:
            db.cursor().executescript(f.read())
        db.commit()


@app.teardown_request
def teardown_request(exeption):
    db = getattr(g, 'db', None)
    if db is not None:
        db.close()


@app.before_request
def before_request():
    g.db = connect_db()


def consumes(content_type):
    def _consumes(function):
        @wraps(function)
        def __consumes(*argv, **keywords):
            if request.headers['Content-Type'] != content_type:
                abort(400)
            return function(*argv, **keywords)

        return __consumes

    return _consumes


# root
@app.route('/')
def index():
    return render_template('index.html', name="test", title="hello")


# quiz_page
@app.route('/quiz/<int:quiz_id>/', methods=['GET'])
def quiz_page(quiz_id):
    cursor = g.db.cursor()
    cursor.execute("select * from quiz where quiz_id=?", (quiz_id,))
    quiz = cursor.fetchone()
    print(quiz)
    return render_template('quiz.html', quiz_text=quiz[2], quiz_hint=quiz[3])


@app.route('/sample')
def sample():
    return render_template('simple2.html')


# request_quiz_anser_judg
@app.route('/answer/', methods=['POST'])
@consumes('application/json')
def quiz_answer():
    data = {
        'quiz_id': request.json['quiz_id'],
        'src': request.json['src']
    }
    flag = EvalProblem(data['quiz_id'], data['src'], g.db).eval()
    if flag == 1:
        quiz_true(USER_ID, data['quiz_id'])

    data['user_problem_ans'] = flag
    response = json.dumps(data, ensure_ascii=False, sort_keys=True)
    return Response(response, mimetype='application/json')


def quiz_true(user_id, quiz_id):
    cursor = g.db.cursor()
    cursor.execute("select answered from answers where user_id=?", (user_id,))
    tmp = cursor.fetchone()
    if tmp is None:
        g.db.execute("insert into answers('user_id','answered') values(?, ?)", (user_id, quiz_id))
        g.db.commit()
    else:
        print("ok")


# request_quiz
@app.route('/request/', methods=['POST'])
@consumes('application/json')
def request_quiz():
    data = {
        "quiz_id": request.json['quiz_id']
    }
    print(data)
    cursor = g.db.cursor()
    cursor.execute("select * from quiz where quiz_id=?", (data['quiz_id'],))
    tmp = cursor.fetchone()
    request_data = {
        "quiz_id": tmp[0],
        "quiz_name": tmp[1],
        "quiz_text": tmp[2],
        "quiz_hint": tmp[3],
    }
    response = json.dumps(request_data, ensure_ascii=False, sort_keys=False)
    return Response(response, mimetype='application/json')


@app.route('/story/', methods=['POST'])
@consumes('application/json')
def get_story():
    quiz_section_id = {
        "quiz_id": request.json["quiz_id"]
    }
    cursor = g.db.cursor()
    cursor.execute("select * from story where quiz_section_id=?", (quiz_section_id["quiz_id"],))
    tmp = cursor.fetchone()
    data = {
        "story": tmp[1]
    }
    response = json.dumps(data, ensure_ascii=False, sort_keys=False)
    return Response(response, mimetype='application/json')


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8080, debug=True)
