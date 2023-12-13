import tensorflow as tf
import pickle

from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "Hello, World!"

@app.route("/test")
def test():
    d = {}
    d["test1"] = "test2"
    return d

@app.route("/translateFromEng", methods = ['POST','GET'])
def translateFromEng():
    with open('tokenizer_fren.pickle', 'rb') as handle:
        tokenizer = pickle.load(handle)
    new_model = tf.keras.models.load_model('model.h5')
    if request.method == 'POST':
        translation = "test"
        d = {}
        d["Translation"] = translation
        d["UnknownWords"] = False
        return d
    if request.method == 'GET':
        return 'Received!'

@app.route("/translateFromFrench", methods = ['POST', 'GET'])
def translateFromFrench():
    with open('tokenizer_fren.pickle', 'rb') as handle:
        tokenizer = pickle.load(handle)
    new_model = tf.keras.models.load_model('model.h5')
    if request.method == 'POST':
        translation = "test"
        d = {}
        d["Translation"] = translation
        d["UnknownWords"] = False
        return d
    if request.method == 'GET':
        return 'Received!'

if __name__ == '__main__':
   app.run(host='0.0.0.0')