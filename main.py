

from flask import Flask, render_template, redirect, url_for, request
import sys
app = Flask(__name__)

attendees = ["adarsh","surya","arnav","jay","iggy","andrew","aadit","dev"]
_names = []
pwd = str(sys.argv[1])

@app.route('/')
def home():
    return redirect(url_for('index'))

@app.route('/index')
def index():
    return render_template('index.html', registered=_names, attendees = attendees)

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['password'] == pwd:
            _names.append(str(request.form['username']))
            return redirect(url_for('index'))
        else:
            error = "incorrect password"
    return render_template('login.html', error=error)

@app.route('/add', methods=['GET', 'POST'])
def add():
    error = None
    if request.method == 'POST':
        if request.form['password'] == pwd:
            _names.append(str(request.form['username']))
            return redirect(url_for('index'))
        else:
            error = "incorrect password"
    return render_template('add.html', error=error)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
