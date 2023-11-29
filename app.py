from dotenv import load_dotenv
load_dotenv()
import os
from flask import Flask, request, render_template
from lib.password_checker import PasswordChecker

app = Flask(__name__)
app.secret_key = os.environ.get('SECRET_KEY')
app.jinja_env.autoescape = True


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/check', methods=['GET', 'POST'])
def check():
    if request.method == 'GET':  # This is to stop the bad response in case the user refreshes the page
        return render_template('index.html')
    checker = PasswordChecker()
    password = request.form.get('password')
    is_valid = checker.check(password)
    return render_template('result.html', password=password, is_valid=is_valid)
    

production = os.environ.get('PRODUCTION', False)
if __name__ == '__main__':
    if production:
        app.run(
            host="0.0.0.0",
            debug=False,
            port=int(os.environ.get('PORT', 5000))
        )
    else:
        app.run(
            host="0.0.0.0",
            debug=True,
            port=int(os.environ.get('PORT', 5000))
        )
