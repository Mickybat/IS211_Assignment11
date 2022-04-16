import re
from flask import Flask, render_template, request, redirect

regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
app = Flask(__name__)
to_do_list = []


def check(email):
    if re.fullmatch(regex, email):
        print("Valid Email")
        return True
    else:
        print("invalid email")
        return False


def check_priority(priority):
    if priority == 'low' or priority == 'medium' or priority == 'high':
        print("valid input")
        return True
    else:
        print("invalid priority")
        return False


@app.route('/', methods=['POST', 'GET'])
def task_table():
    return render_template("index.html")


@app.route('/submit', methods=['POST', 'GET'])
def submit_task():

    if request.method == 'POST':

        task = request.form['task']

        priority = request.form['priority']
        isPriorityValid = check_priority(priority)

        email = request.form['email']
        isEmailValid = check(email)

        if isEmailValid and isPriorityValid:
            tempList = [task, priority, email]
            to_do_list.append(tempList)
            return render_template('index.html', to_do_list=to_do_list)
        else:
            return render_template('index.html', to_do_list=to_do_list)


@app.route('/clear', methods=['POST', 'GET'])
def clean_list():
    if request.method == "POST":
        to_do_list.clear()
        return render_template('index.html', to_do_list=to_do_list)


if __name__ == "__main__":
    app.run()