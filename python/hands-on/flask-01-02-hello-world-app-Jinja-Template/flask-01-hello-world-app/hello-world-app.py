from distutils.log import debug
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return "hello from flask"

#localhost:5000

@app.route('/second')
def second():
    return "DENEME"


@app.route('/third')
def third():
    return 'This is the subpage of third page'


@app.route('/forth/<string:id>')
def forth(id):
    return f'Id number of this page is {id}'























if __name__ == '__main__':
    app.run(debug=True)
  









