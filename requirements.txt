#install virtual env... with pipenv. 
pip install pipenv

# install Django with pipenv
pipenv install django==2.1

# aafter running above commands, activate pipenv.
# to run projects using pipenv, it must be started pipenv
pipenv shell

# now create project . it ctrates vidly package and manage.py file
django-admin startproject vidly .

#create an app with startapp named movies
python manage.py startapp movies

#pylint code syntax formatter for django.  
pipenv install pylint-django
#after sucessful install pylint-django. add .pylintrc file(pylint config file) in root folder
# and add below line in that pylint config file 
load-plugins = pylint-django 

