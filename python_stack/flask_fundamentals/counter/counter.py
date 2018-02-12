from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = 'SecretKey'

@app.route('/')
def index():
    if 'count' not in session:
        session['count'] = 0
    session['count'] = session['count'] + 1
    print session['count']
    return render_template('index.html', count = session['count'])

@app.route('/double', methods=['POST'])
def double():
    session['count'] += 1
    return redirect('/')

@app.route('/reset')
def reset():
    session.pop('count')
    # session['count'] = 0
    return redirect('/')

app.run(debug=True)
