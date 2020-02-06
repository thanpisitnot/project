from flask import Flask, render_template, jsonify, request, json , redirect, url_for
from flask_cors import CORS

UPLOAD_FOLDER = './dist/static/image/tour_picture'
app = Flask(__name__,
            static_folder = "./dist/static",
            template_folder = "./templates")
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})


@app.route('/create')
def hello():
    return('hello')

@app.route('/test1')
def test1():
    a = 3
    b = 4
    c = a+b
    return(str(c))

@app.route('/test/<url>')
def check(url):
    name = 'test'
    grade = 'B'
    return render_template('test.html',URL1=url, name1=name, grade1=grade)

@app.route('/test1/<url>')
def check1(url):
    name = url
    grade = 'B'
    return render_template('test.html',URL1=url, name1=name, grade1=grade)

if __name__ == "__main__":
    # reload(sys)
    # sys.setdefaultencoding('utf-8')
    app.run(debug=True)
    # app.run(host = '0.0.0.0',port=5000)