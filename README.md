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

## Key Technologies

- **Backend:** Python, Flask, Docker
- **Frontend:** CSS, HTML
- **Testing:** Playwright

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

Run the tests:
```bash
pytest
```

Start the server:
```bash
python app.py
```

### Run with Docker

Build a Docker image (image name optional):
```bash
docker build -t password_checker .
```

Start the Docker container:
```bash
docker run -p 5000:5000 password_checker
```