import os
from flask import Flask, request, render_template, escape
from lib.password_checker import PasswordChecker

app = Flask(__name__)
app.jinja_env.autoescape = True


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/check', methods=['GET', 'POST'])
def check():
    if request.method == 'GET':  # This is to stop the bad response in case the user refreshes the page
        return render_template('index.html')
    checker = PasswordChecker()
    password = format(escape(request.form.get('password')))
    is_valid = checker.check(password)
    return render_template('result.html', password=password, is_valid=is_valid)
    

if __name__ == '__main__':
    app.run(
        debug=True,
        host="0.0.0.0", # Listen for connections _to_ any server
        port=int(os.environ.get('PORT', 5000))
    )
