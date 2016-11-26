#coding:utf-8
from flask import Flask, render_template

app = Flask(__name__);

@app.route('/')
def index():
   return render_template('index.html', name="test", title="hello")

'''
@app.route('/quiz', methods=['POST'])
def quiz_paee():
    return render_template('')

@app.route('/answer')
def quiz_answer():
    ''' '''
    return
'''

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
