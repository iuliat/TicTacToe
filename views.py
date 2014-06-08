from flask import Flask,render_template, flash, redirect, session, url_for, request
from flask.ext.wtf import Form
from wtforms import TextField
from wtforms.validators import Required
from flask.ext.sqlalchemy import SQLAlchemy
from users import User

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

app = Flask(__name__)

app.config.from_object('config')
engine = create_engine('sqlite:///storage.db', echo = True)

Session = sessionmaker(bind=engine)
session = Session()

@app.route('/')
def index():
    user = {'name': 'gigi'} # fake user
    return render_template("index.html", user = user)

class LoginForm(Form):
    user = TextField('name', validators = [Required()])

@app.route('/login/', methods = ('GET', 'POST'))
def login():
    form = LoginForm(csrf_enabled=False)
    if form.validate_on_submit():
  	user = User(name = form.name)
	# add user to db
        session.add(user)
        session.commit()
        flash('Processing...')
        return redirect('/')
    return render_template('login.html', form = form)

@app.route('/all_users/')
def all_users():
     return session.query(user).all()

@app.route('/new_game/')
def game():
     return 0

if __name__ == '__main__':
    app.run()
    
