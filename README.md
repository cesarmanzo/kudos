# Kudos app

Coding challenge for Trakstar. Please excuse the poor frontend code, as this is my first time *ever* working with ReactJS (80% of my time was spent dealing with the frontend).

The requirements for the project are the following:

- Backend in Python3
- Every week, each user receives three kudos to give to other users within their organization
- Kudos do not accumulate
- Users should be able to give kudos to other users, and see who has given them kudos
- You should also be able to tell who you're currently logged in as, and which organization you're associated with
- When a kudo is given, the user giving the kudo should be able to include a message about why they're giving it.

## Features
- Backend created in Django 4.0.4
- API REST with Django Rest Framework
- Authentication with JWT
- Frontend created with React
- Separated frontend and backend
- Cron job to restart kudos count
- Data ready to load and test
- Multiple users with different organizations
- Image in organization (not implemented in frontend)
- CRUD available with Django Admin
- Clean and simple design (bootstrap + Swal alert)

## Prerequisites
- Python 3 (3.8.10)
- npm 8.5.5
- node 16.15.0

## Set up (Linux)
```
sudo apt-get install git
sudo apt-get install python3-pip
sudo pip3 install virtualenvwrapper

mkdir ~/.virtualenvs
export WORKON_HOME=~/.virtualenvs

Edit ~/.bashrc and add:

VIRTUALENVWRAPPER_PYTHON='/usr/bin/python3'
source /usr/local/bin/virtualenvwrapper.sh

Then, 
source .bashrc

mkvirtualenv virtualenv_name # Create virtualenv
workon virtualenv_name # Activate/switch to a virtualenv
deactivate # Deactivate virtualenv

git clone https://github.com/cesarmanzo/kudos.git
cd kudos
pip install -r requirements.txt
npm install
````

To add the cron, run:
`python manage.py crontab add`

Don't forget to remove after testing the project with:
`python manage.py crontab remove`

## Run the project
After activating your virtual environment, run the migrations:
`python manage.py migrate`

Then, load the data:
`python manage.py loaddata mydata.json`

Then, run the project:
`python manage.py runserver`

In another terminal, to run the frontend:
`npm start`

### Django Admin

To enter Django Admin, go to http://127.0.0.1:8000/admin

Login: `admin` / `admin`

### Users to test

You can login with these users and send kudos or see received/sent kudos. Just go to http://localhost:3000/ and use the data below.

|     User     |  Password    |  Organization | Remaining Kudos |
|--------------|--------------|---------------|-----------------|
|user          |use123use     |Trakstar       | 1               |
|marinela      |mar123mar     |Trakstar       | 3               |
|perfect       |per123per     |Trakstar       | 2               |
|eternal       |ete123ete     |Lenovo         | 3               |
|computer      |com123com     |Lenovo         | 1               |
|example       |exa123exa     |Formula        | 3               |
|cesar         |ces123ces     |Formula        | 1               |


## To Do
- Vastly improve design
- Implement CI/CD pipelines
- Move to robust database (PostgreSQL)
- Run in kubernetes
- Add domain and certificates
- Refactor frontend code
- Add a hundred validations
