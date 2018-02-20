from flask import Flask, render_template, request, redirect, session, flash
from mysqlconnection import MySQLConnector
import md5, re
app = Flask(__name__)
mysql = MySQLConnector(app,'users')
app.secret_key = 'ThisIsSecret' # you need to set a secret key for security purposes
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

print 'we are connected'

@app.route('/') # our index route will handle rendering our form
def index():
    print 'THIS WORKS'
    if 'user_id' not in session: 
        session['user_id'] = []
    else:
        return render_template('success.html', success = 'Welcome Back!')
    return render_template('index.html')

@app.route('/login', methods=['POST'])
def login_user():
    print "Got Login Info"
    password = md5.new(request.form['password_login']).hexdigest()
    email = request.form['email_login']
    user_query = "SELECT * FROM user where user.email = :email AND user.password = :password"
    query_data = { 'email': email, 'password': password}
    user = mysql.query_db(user_query, query_data)
    print user
    if (user != []):
        print "Success!"
        session['user_id'] = user[0]["id"]
        return render_template('success.html', success = 'Successful Login')
    else:
        flash( "Login Failed!" )
    # do the necessary logic to login if the user exists, otherwise redirect to login page with error message<br>

    if len(request.form['email_login']) < 1:
        flash("Email cannot be blank!")
    if len(request.form['password_login']) < 1:
        flash("Password cannot be blank!")
    elif not EMAIL_REGEX.match(request.form['email_login']):
        flash("Invalid Email Address!")
    return redirect('/')
 

@app.route('/register', methods=['POST'])
def create_user():
    print "Got Post Info"
    password = md5.new(request.form['password']).hexdigest()    
    query = "INSERT INTO user (first_name, last_name, email, password, create_time, updated_at) VALUES (:first_name, :last_name, :email, :password, NOW(), NOW())"
    data = {
            'first_name': request.form['first_name'],
            'last_name':  request.form['last_name'],
            'email': request.form['email'],
            'password': password,
            } 
    print request.form

    

    user_query = "SELECT * FROM user where user.email = :email"
    query_data = { 'email': request.form['email'] }
    user = mysql.query_db(user_query, query_data)

    errors = 0


    if len(request.form['first_name']) <= 2:
        flash("First name must be longer")
        errors=1
    
    if len(request.form['last_name']) <= 2:
        flash("Last name must be longer")
        errors=1

    if len(request.form['password']) < 8:
        flash("Password must be 8 char or more")
        errors=1

    if request.form['password'] != request.form['pswdcon']:
        flash("Passwords must match!")
        errors=1

    if len(request.form['email']) < 1:
        flash("Email cannot be blank!")
        errors=1

    elif not EMAIL_REGEX.match(request.form['email']):
        flash("Invalid Email Addres!")
        errors=1

    if (user==[] and errors == 0):
        mysql.query_db(query, data)
        user = mysql.query_db(user_query, query_data)
        session['user_id'] = user[0]["id"]
        return render_template('success.html', success = 'Successful Registration')
    # else:
        # flash( "User Already Exists!" )

    return redirect('/')

@app.route('/logout', methods=['POST'])    
def logout():
    print 'logout button'
    session.clear()
    return redirect('/')    

app.run(debug=True) # run our server    