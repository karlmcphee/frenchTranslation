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
    d = {}
    d["Translation"] = "translation"
    d["UnknownWords"] = False
    if request.method == 'POST':
        filehandler_eng = open('tokenizer_eng.pickle', 'rb')
        eng_tokenizer = pickle.load(filehandler_eng)
        model = tf.keras.models.load_model('my_model.h5')
        phrase = request.form.get('phrase')
        phrase2 = request.form.get('request')
        d["Translation"] = str(phrase) + str(phrase2)
        sys.stdout.flush()
        #tokens = tokenizer.texts_to_sequences(phrase)
        #padded_tokens = pad_sequences(tokens)
        #pred = model.predict(padded_tokens)
        #prediction = np.argmax([pred], axis=1)
        #filehandler_fr = open('tokenizer_fren.pickle', 'rb')
        #fr_tokenizer = pickle.load(filehandler_eng)
        #resp = ""
        #for i in range(len(prediction[0])):
        #    wordchoice = ""
        #    for word, index in fr_tokenizer.word_index.items():
        #        if index == n:
        #            wordchoice = word
        #            break
        #    resp += wordchoice
        #resp += " test"
        #d["Translation"] = resp
        #filehandler_fr.close()
        filehandler_eng.close()
        return d
    if request.method == 'GET':
        return d

@app.route("/translateFromFrench", methods = ['POST', 'GET'])
def translateFromFrench():
    d = {}
    d["Translation"] = "translation"
    d["UnknownWords"] = False
    if request.method == 'POST':
        filehandler_fr = open('tokenizer_fren.pickle', 'rb')
        fren_tokenizer = pickle.load(filehandler_fr)
        model = tf.keras.models.load_model('my_model.h5')
        phrase = request.args['request']['phrase']
        sys.stdout.flush()
        tokens = tokenizer.texts_to_sequences(phrase)
        padded_tokens = pad_sequences(tokens)
        pred = model.predict(padded_tokens)
        prediction = np.argmax([pred], axis=1)
        filehandler_eng = open('tokenizer_eng.pickle', 'rb')
        eng_tokenizer = pickle.load(filehandler_eng)
        resp = ""
        for i in range(len(prediction[0])):
            wordchoice = ""
            for word, index in eng_tokenizer.word_index.items():
                if index == n:
                    wordchoice = word
                    break
            resp += wordchoice
        d["Translation"] = resp
        filehandler_fr.close()
        filehandler_eng.close()
        return d
    if request.method == 'GET':
        return d

if __name__ == '__main__':
   app.run(host='0.0.0.0')