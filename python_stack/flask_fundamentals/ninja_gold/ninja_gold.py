from flask import Flask, render_template, request, redirect, session
import random

app = Flask(__name__)
app.secret_key = 'SecretKey'

@app.route('/', methods = ['GET'])
def index():
    if "gold" not in session:
        session["gold"] = 0
    if "message" not in session:
        session["message"] = ""
    return render_template( "index.html", gold = session["gold"], message = session["message"] )

@app.route('/process_money', methods = ['post'])
def process_money():
    if request.form['building'] == 'farm':
        spin = random.randrange(10,21)
        result = "you earned {} farm gold".format(spin)
    elif request.form['building'] == 'cave':
        spin = random.randrange(5,11)
        result = "you earned {} cave gold".format(spin)
    elif request.form['building'] == 'house':
        spin = random.randrange(2,6)
        result = "you earned {} house gold".format(spin)
    elif request.form['building'] == 'casino':
        spin = random.randrange(-50,51)
        if spin > 0:
            result = "you won {} gold!".format(spin)
        elif spin < 0:
            result = "you lost {} gold! :(".format(spin)
        elif spin == 0:
            result = "you broke even! Atleast it was fun!!"
    
    session['gold'] += spin
    session['message'] = "  " + "|" + "  " + result + session['message']
    
    return redirect('/')

@app.route('/reset', methods=['POST'])
def reset():
    session.clear()
    return redirect('/')

app.run(debug=True)