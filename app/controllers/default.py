from app import app
from flask import render_template
from app.models.forms import loginForm


@app.route("/index")
@app.route("/")
def index():
    return render_template('index.html')

@app.route("/login")
def login():
    form =  loginForm()
    return render_template('login.html'
                           ,form = form)









