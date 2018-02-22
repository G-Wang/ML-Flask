from app import app
from flask import render_template
import time


@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Hippo',
            'networth': '10B'}
    posts = [
        {
            'author': {'username': 'Hippo kid'},
            'body': 'I was born last week!'
        },
        {
            'author': {'username': 'Hippo baby'},
            'body': 'I was born last night..'
        }
    ]
    return render_template('index.html', title = "HOME", user = user, posts = posts)
