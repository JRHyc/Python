from flask import Flask, render_template, request, redirect
app = Flask(__name__)

@app.route('/')
def index():
  return render_template("index.html")

@app.route('/process', methods=['POST'])
def process():
   print "Got Post Info"
   
   name = request.form['name']
   email = request.form['email']
   print name
   print email
   # redirects back to the '/' route
   return redirect('/')



app.run(debug=True)