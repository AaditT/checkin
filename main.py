

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
    attendees = []
    myFile = open("names.txt", 'r')
    for line in myFile.readlines():
        attendees.append(str(line.rstrip()))
    if request.method == 'POST':
        if request.form['username'] not in attendees:
            error = "Please register User before logging in"
            return render_template('login.html', error=error)
        else:
            if request.form['password'] == pwd:
                _names.append(str(request.form['username']))
                return redirect(url_for('index'))
            else:
                error = "Incorrect password"
    return render_template('login.html', error=error)

@app.route('/manage')
def manage():
    return render_template('manage.html')

@app.route('/add', methods=['GET', 'POST'])
def add():
    success = None
    deletion = None
    issue = None
    if request.method == 'POST':
        attendees = []
        myFile = open("names.txt", 'r')
        for line in myFile.readlines():
            attendees.append(str(line.rstrip()))
        if str(request.form['username']) in attendees:
            issue = "User '"+str(request.form['username'])+"' already exists!"
            success = None
        else:
            f = open("names.txt", "a")
            f.write(str(request.form['username'])+"\n")
            success = "'"+ str(request.form['username']) + "' has been added!"
            deletion = None
        #return redirect(url_for('index'))
    return render_template('manage.html', issue=issue, success=success, deletion=deletion)

@app.route('/delete', methods=['GET', 'POST'])
def delete():
    deletion = None
    error = None
    if request.method == 'POST':
        deletion = None
        attendees = []
        myFile = open("names.txt", 'r')
        for line in myFile.readlines():
            attendees.append(str(line.rstrip()))
        if str(request.form['username']) in attendees:
            myFile = open("names.txt", 'r+')
            d = myFile.readlines()
            myFile.seek(0)
            for i in d:
                if i != (str(request.form['username'])+"\n"):
                    myFile.write(i)
            myFile.truncate()
            myFile.close()
            deletion = "'"+ str(request.form['username']) + "' has been deleted!"
            #return redirect(url_for('index'))
        else:
            error = "User does not exist"
    return render_template('manage.html', error=error, deletion=deletion)


if __name__ == '__main__':
    app.run(debug=True, port=5000)
