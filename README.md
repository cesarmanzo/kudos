# Kudos app
Coding Challenge for Trakstar


**Make sure you have Python3 installed**



## Set up
```
sudo apt-get install git

sudo apt-get install python3-pip

sudo pip3 install virtualenvwrapper

mkdir ~/.virtualenvs
export WORKON_HOME=~/.virtualenvs

vim ~/.bashrc

VIRTUALENVWRAPPER_PYTHON='/usr/bin/python3'
source /usr/local/bin/virtualenvwrapper.sh

source .bashrc


mkvirtualenv virtualenv_name # Create virtualenv
workon virtualenv_name # Activate/switch to a virtualenv
deactivate virtualenv_name # Deactivate virtualenv


git clone https://github.com/cesarmanzo/kudos.git
cd kudos
pip install requirements.txt

python manage.py runserver

```
