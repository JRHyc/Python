from flask import Flask, render_template, request, redirect, session
import random

app = Flask(__name__)
app.secret_key = 'SecretKey'

@app.route('/', methods = ['GET'])
def index():
    if 'rand_num' not in session:
        session['rand_num'] = random.randrange(0, 101)
    print session['rand_num'] , "Is the random number"
    return render_template('index.html', rand_num = session['rand_num'])

@app.route('/guess_num', methods=['POST'])
def guess_num():
    session['guess_num'] = request.form['guess_num']
    print session['guess_num'] + " this is the guessed number"
    if int(session['guess_num']) > session['rand_num']:
        result = 'Too high!'
        print result
    elif int(session['guess_num']) < session['rand_num']:
        result = 'Too low!'
        print result
    else:
        result = 'Correct!'
        print result
    return render_template('index.html', result = result, guess_num = session['guess_num'] )

@app.route('/reset', methods=['POST'])
def reset():
    session.clear()
    return redirect('/')

app.run(debug=True)