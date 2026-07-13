from flask import Flask, flash, redirect, render_template, url_for, session
from flask import request
from flask_sqlalchemy import SQLAlchemy 
from datetime import datetime
from werkzeug.security import generate_password_hash



app = Flask(__name__)
app.secret_key = "cf0fa2ac5471abc98c5f9b228b726a3c"
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

@app.route('/admin/login', methods=['GET', 'POST'])
def admin_login():
    ADMIN_PASSWORD = "pew_"
    
    if request.method == 'POST':
        password = request.form.get('password')
        
        if password == ADMIN_PASSWORD:
            session['is_admin'] = True
            return redirect(url_for('show_users'))
        
        flash('Wrong password, try again.', 'danger')
        return redirect(url_for('admin_login'))
    
    return render_template('admin_login.html')


@app.route('/admin/users')
def show_users():
    if not session.get('is_admin'):
        return redirect(url_for('admin_login'))
    users = User.query.order_by(User.id).all()
    return render_template('users.html', users=users)


@app.route('/admin/users/add', methods=['GET', 'POST'])
def add_user():
    if not session.get('is_admin'):
        return redirect(url_for('admin_login'))
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        description = request.form.get('description')

        hashed_pw = generate_password_hash(password)
        new_user = User(username=username, password=hashed_pw, description=description)
        db.session.add(new_user)
        db.session.commit()

        flash("User added successfully !", "success")
        return redirect(url_for('show_users'))
    return render_template('add_user.html')

@app.route('/admin/users/edit/<int:id>', methods = ['GET','POST'])
def edit_user(id):
    if not session.get('is_admin'):
        return redirect(url_for('admin_login'))
    
    user = User.query.get_or_404(id)

    if request.method == 'POST' :
        user.username =request.form['username']
        user.description =request.form['description']
        db.session.commit()

        flash("User updated successfully !", "success")
        return redirect(url_for("show_users"))
    
    return render_template("edit_user.html", user=user)

@app.route('/admin/users/delete/<int:id>', methods=['POST'])
def delete_user(id):
    if not session.get('is_admin'):
        return redirect(url_for('admin_login'))
    
    user = User.query.get_or_404(id)
    db.session.delete(user)
    db.session.commit()

    flash('User deleted successfully !' , "danger")
    return redirect(url_for('show_users'))


if __name__ == "__main__":
    app.run(port=5000, debug="True")     