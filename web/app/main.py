import os
import requests

from flask import Flask, render_template, request, flash, redirect, url_for

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get("SECRET_KEY")

@app.route("/")
def root():
    api_url = os.environ.get("API_URL")
    request_url = f'{api_url}/users/'
    response = requests.get(request_url)
    users = response.json()

    return render_template("index.jinja2", users=users)

@app.route("/add", methods=['GET', 'POST'])
def add_user():
    if request.method == 'POST':
        email = request.form.get('email', "")
        password = request.form.get('password', "")

        if not email:
            flash('Email is required!')
        elif not password:
            flash('Password is required!')
        else:
            api_url = os.environ.get("API_URL")
            request_url = f'{api_url}/users/'
            response = requests.post(request_url, json=request.form)
            return redirect(url_for('root'))
    else:
        return render_template ("add.jinja2")
