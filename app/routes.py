from app import app
import time


@app.route('/')
@app.route('/index')
def index():
    return 'wow joanne and gary are so cool'
