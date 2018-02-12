from flask import Flask, render_template, request, redirect, session, flash
app = Flask(__name__)
app.secret_key = 'secretKey'

@app.route('/')
def index():
  return render_template("index.html")

@app.route('/results', methods=['post'])
def results():
  name = request.form['name']
  email = request.form['email']
  location = request.form['location']
  comment = request.form['comment']
  error = False
  print name
  print email
  print location
  print comment

  if len(request.form['name']) < 1:
    flash('Fatal Error!! Name cannot be left blank!')
    error = True
  if len(request.form['comment']) < 1:
    flash('Fatal Error!! Comment field cannot be left blank!')
    error = True
  if len(request.form['comment']) > 120:
    flash('Fatal Error!! Comments cannot exceed 120 characters!')
    error = True

  if error:
    return redirect('/')

  
  return render_template('results.html', name = name, email = email, location = location, comment = comment)



app.run(debug=True)