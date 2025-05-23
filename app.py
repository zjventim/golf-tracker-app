from flask import Flask, render_template, request, redirect
from db import insert_round, get_rounds, create_user_table, get_user_by_id, validate_login, create_user
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user

app = Flask(__name__)

@app.route('/HomePage', methods=['GET', 'POST'])
@login_required
def index():
    if request.method == 'POST':
        course_id = int(request.form['course_id'])
        date = request.form['date']
        score = int(request.form['score'])
        insert_round(course_id, date, score)
        return redirect('/HomePage')
    
    rounds = get_rounds()
    return render_template("index.html", rounds=rounds)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user = validate_login(request.form['username'], request.form['password'])
        if user:
            login_user(User(id=user[0], username=user[1]))
            return redirect('/HomePage')
        return "Invalid credentials"
    return render_template('login.html') 

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        try:
            create_user(request.form['username'], request.form['password'])
            return redirect('/login')
        except:
            return "User already exists"
    return render_template('signup.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect('/login')

if __name__ == '__main__':
    app.run(debug=True)

class User(UserMixin):
    def __init__(self, id, username):
        self.id = id
        self.username = username

@LoginManager.user_loader
def load_user(user_id):
    user = get_user_by_id(user_id)
    if user:
        return User(id=user[0], username=user[1])
    return None