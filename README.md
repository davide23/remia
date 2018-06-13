# remia

To install requirements and all the rest: (keep in mind to replace your paths)

- git clone git@github.com:davide23/remia.git
- virtualenv venv -p /usr/local/Cellar/python/3.6.5/bin/python3.6 .   # to install with Python 3
- source venv/bin/activates
- pip install -r requirements.txt
- psql .                                       # this will open the db shell, you need to create one (it's one command line) 
- CREATE USER dav;
- CREATE DATABASE remia_clients OWNER dav;     # keep dav, it's the name I put in the settings
- \q                                           # you get out of the terminal
- python manage.py migrate
- python manage.py runserver

URL: http://localhost:8000/pages

my models name, if you wanna use it as parameters name (don't have to) 

    full_name
    street_and_number
    postcode
    city 


Also, I put in the template crispy_forms just cause was the quickest way for me to test it.. to the f* you want :) 
# remia
