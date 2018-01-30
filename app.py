import os
from flask import Flask
from flask_ask import Ask, statement
import pexpect
import pickle
import pandas as pd
import numpy as np
from collections import defaultdict, Counter
from reverse_read import reverse_readline

app=Flask(__name__)

ask = Ask(app, '/')

@ask.intent('findkeys')
def retrievr():
    os.system("/path/to/repo/sound_alarm.py &")
    speech_text = guess_locate()
    return statement(speech_text)


def guess_locate():
    read_dict = {}
    line_gen = reverse_readline('YOUR_DATA_FILE.txt')
    res_lst = []
    while len(res_lst) != 20:
        ln = next(line_gen)
        if ln.startswith('Host'):
            _, ip, _, reading = ln.split()
            read_dict[ip] = reading
            res_lst.append(read_dict)
            if ip == 'ip.of.one.computer':
                read_dict = {}
        else:
            pass
    val = pd.DataFrame(res_lst).replace({'N/A': np.nan}).values

    mdl_ = pickle.load(open('location_model_file.dat', 'rb'))
    preds = mdl_.predict(val)
    guess = Counter(preds)
    guess = guess.most_common(1)[0][0]
    reply_str = 'Try looking in the '
    if guess == 1:
        reply_str += 'bedroom'
    elif guess == 2:
        reply_str += 'bathroom'
    elif guess == 3:
        reply_str += 'kitchen'
    elif guess == 4:
        reply_str += 'living room'
    return reply_str


if __name__ == "__main__":
    app.run(host='127.0.0.1', port='5000')
