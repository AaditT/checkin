

from flask import Flask, render_template, redirect, url_for, request
import sys

app = Flask(__name__)

_names = []
pwd = str(sys.argv[1])

@app.route('/')
def home():
    return redirect(url_for('index'))

@app.route('/index')
def index():
    attendees = []
    myFile = open("names.txt", 'r')
    for line in myFile.readlines():
        attendees.append(str(line.rstrip()))
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

@app.route('/manage')
def manage():
    return render_template('manage.html')

@app.route('/add', methods=['GET', 'POST'])
def add():
    error = None
    if request.method == 'POST':
        f = open("names.txt", "a")
        f.write(str(request.form['username'])+"\n")
        return redirect(url_for('index'))
    return render_template('manage.html', error=error)

@app.route('/delete', methods=['GET', 'POST'])
def delete():
    error = None
    if request.method == 'POST':
        f = open("names.txt","r+")
        d = f.readlines()
        f.seek(0)
        for i in d:
            if i != (str(request.form['username'])+"\n"):
                f.write(i)
        f.truncate()
        f.close()
        return redirect(url_for('add'))
    return render_template('manage.html', error=error)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
