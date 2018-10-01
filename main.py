from flask import Flask, request, redirect, render_template

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route('/')
def find():
  return render_template("signup.html")

@app.route('/', methods=['POST'])
def signup():
  username = request.form['username']
  password = request.form['password']
  verify_pw = request.form['verify-pw']
  email = request.form['email']
  username_error = ""
  password_error = ""
  verify_pw_error = ""
  email_error = ""
  email_error_msg = "Not a valid e-mail"

  if not username or not password or not verify_pw:
    error_msg = "Please don't leave me empty!"
    if not username:
      username_error = error_msg
    if not password:
      password_error = error_msg
    if not verify_pw:
      verify_pw_error = error_msg
  
  if len(username) < 3 or len(username) > 20:
    if not username_error:
      username_error = "Your username should be between 3 and 20 characters"

  if len(password) < 3 or len(password) > 20:
    if not password_error:
      password_error = "Your password should be between 3 and 20 characters"

  if password != verify_pw:
    if not verify_pw_error:
      verify_pw_error = "These passwords do not match!"

  for char in password:
    if char == " ":
      password_error = "Passwords should not contain spaces"

  if email:
    if len(email) < 3 or len(email) > 20:
      email_error = "Must be between 3 and 20 characters" 
    elif not email_error:
      at_char = False
      dot_char = False
      for char in email:
        if char == '.' and not dot_char:
          dot_char = True
        elif char == '@' and not at_char:
          at_char = True
        elif char == '.' and dot_char:
          email_error = email_error_msg
        elif char == '@' and at_char:
          email_error = email_error_msg
          
      if not at_char or not dot_char:
        email_error = email_error_msg

      if email.find('.') < email.find('@') and not email_error:
        email_error = email_error_msg

  if username_error or password_error or verify_pw_error or email_error:
    return render_template("signup.html", username_error=username_error,
                           password_error=password_error,
                           verify_pw_error=verify_pw_error,
                           username=username,
                           email=email,
                           email_error=email_error)
  else:
    return redirect('/welcome?name=' + username)

@app.route('/welcome')
def welcome():
  username = request.args.get('name')
  return render_template("welcome.html", name=username)

app.run()