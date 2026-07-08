from flask import Flask, redirect, render_template, url_for
from flask import request
from flask_sqlalchemy import SQLAlchemy 
from datetime import datetime
#from app import app, db

from werkzeug.security import generate_password_hash

# in register():



app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///userr.db"
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(70), nullable=False)
    password = db.Column(db.String(70), nullable=False)
    description = db.Column(db.String(255), nullable=True)
    datetime = db.Column(db.DateTime, default=datetime.utcnow)

with app.app_context():
    db.create_all()         

@app.route('/')
def home():
    all_users = User.query.all()
    return render_template("home.html", users=all_users)

@app.route('/welcome')
def welcome_page():
    return render_template("welcome.html")

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/visit')
def visit():
    return render_template("visit.html")

@app.route('/registration', methods=["GET", 'POST'])
def register():

   

    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        description = request.form.get('description')

        hashed_pw = generate_password_hash(password)
        new_user = User(username=username, password=hashed_pw, description=description)
   
        print(f"Username: {username}, Password: {password}, Description: {description}")
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for('home'))
    return render_template('register.html')

@app.route('/admin/users')
def show_users():
    users = User.query.order_by(User.id).all()
    return render_template('users.html', users=users)


if __name__ == "__main__":
    app.run(port=5000)     