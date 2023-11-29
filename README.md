# Password Checker



## Introduction

During week 7 of the Makers Academy bootcamp, I developed an intricate password checker as a day-long project. This utility enforces 9 rigorous validation steps to ensure password strength. The accompanying Dockerfile ensures smooth containerization for easy deployment and scaling.

## Features

In the following order:
- Checks if the password is at least 20 characters long
- Checks if the password contains nummbers
- Checks if the password contains symbols
- Checks if the password contains both uppercase and lowercase characters
- Checks if the password contains an animal (from an extensive list of animals)
- Checks if all the digits in the password add up to at least 60
- Checks if the password contains a word to start a question (from a list of words)
- Checks that any consecutive digits don't add to more than 16
- Checks if the password contains the first name of an English monarch (from a list of English monarchs)

- See [password_checker.py](https://github.com/shakey0/PasswordChecker/blob/main/lib/password_checker.py) for the code to check the password.

## Deployment & CI/CD Pipeline Process

1. Used Docker to containerise the app on my local machine.
    - [See Dockerfile](https://github.com/shakey0/PasswordChecker/blob/main/Dockerfile)
2. Created a script - main.yml - to build and test the app in GitHub Actions.
3. Created a new web service in Render.
4. Configured GitHub to give Render the necessary permissions on this repository, so each time a new push is made to the main branch, and the tests pass, the latest version of the app will be deployed to Render.

## Key Technologies

- **Backend:** Python, Flask
- **Frontend:** CSS, HTML
- **Testing:** Pytest, Playwright
- **Deployment:** Docker, GitHub Actions, Render

## CI/CD Pipeline

I have included a CI/CD pipeline in this project so that when the code is pushed to Github the tests will run and the code will be deployed to https://exoframe.xf.mkrs.link . However, my Exoframe token from Makers is no longer valid, and so the pipeline will fail in the CD part.

## Installation & Setup

Run the following command to clone the repo:
```bash
git clone https://github.com/shakey0/PasswordChecker
cd PasswordChecker
```

Create your virtual environment:
```bash
pipenv install
pipenv shell
```

Install dependencies:
```bash
pip install -r requirements.txt
```

Create a .env file with the following:
```bash
SECRET_KEY=a_secret_key
```

Run the tests:
```bash
pytest
```

Start the server:
```bash
python app.py
```

### Run with Docker

Build a Docker image (image tag optional):
```bash
docker build -t password_checker .
```

Start the Docker container:
```bash
docker run -e PRODUCTION=True -e SECRET_KEY=a_secret_key -p 5000:5000 password_checker
```