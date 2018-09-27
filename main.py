from flask import Flask, request, redirect, render_template

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route('/')
def index():
  return render_template("signup.html")

@app.route('/welcome', methods=['POST'])
def welcome():
  username = request.form['username']
  password = request.form['password']
  verify_pw = request.form['verify-pw']
  email = request.form['email']
  username_error = ""
  password_error = ""
  verify_pw_error = ""

  if not username or not password or not verify_pw:
    error_msg = "Please don't leave me empty!"
    if not username:
      username_error = error_msg
    if not password:
      password_error = error_msg
    if not verify_pw:
      verify_pw_error = error_msg
    
    return render_template("signup.html", username_error=username_error,
                           password_error=password_error,
                           verify_pw_error=verify_pw_error)


  return render_template("welcome.html", name=username)


app.run()