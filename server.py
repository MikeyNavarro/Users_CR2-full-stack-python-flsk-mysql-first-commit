from flask import Flask, render_template, redirect , request

from users import User
app = Flask(__name__)

@app.route('/')
def home():
  return render_template('index.html')

@app.route('/users')
def users():
  
  return render_template('users.html', users = User.get_all())

@app.route('/users/create')
def createUsers():
  return render_template('usersCreate.html')

@app.route('/submitCreates', methods = ['POST'])
def submitUser():
  print(request.form)
  

  User.save(request.form)

  return redirect('/users')


if __name__ == '__main__':
  app.run(debug=True)