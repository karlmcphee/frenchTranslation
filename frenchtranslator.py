import tensorflow as tf
import pickle
import werkzeug
from tensorflow.keras.preprocessing.sequence import pad_sequences
import sys

from flask import Flask, request

app = Flask(__name__)

@app.errorhandler(werkzeug.exceptions.BadRequest)
def handle_bad_request(e):
    return 'bad request!', 400

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
    with open('tokenizer_eng.pickle', 'rb') as handle:
        tokenizer = pickle.load(handle)
    new_model = tf.keras.models.load_model('my_model.h5')
    d = {}
    d["Translation"] = "translation"
    d["UnknownWords"] = False
    if request.method == 'POST':
        #phrase = request.args('phrase')
        #tokens = tokenizer.texts_to_sequences(phrase)
        #padded_tokens = pad_sequences(tokens)
        #if len(tokens) == 0:
        #    d["UnknownWords"] = True
        return d
    if request.method == 'GET':
        return d

@app.route("/translateFromFrench", methods = ['POST', 'GET'])
def translateFromFrench():
    with open('tokenizer_fren.pickle', 'rb') as handle:
        tokenizer = pickle.load(handle)
    new_model = tf.keras.models.load_model('model.h5')
    d = {}
    d["Translation"] = "translation"
    d["UnknownWords"] = False
    if request.method == 'POST':
        for key in request.args:
            print(key)
    sys.stdout.flush()
        #tokens = tokenizer.texts_to_sequences(phrase)
        #padded_tokens = pad_sequences(tokens)
        return d
    if request.method == 'GET':
        return d

if __name__ == '__main__':
   app.run(host='0.0.0.0')