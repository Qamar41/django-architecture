## Istruction to run this project


#### User Endpoints

Method | Endpoint | Functionality
--- | --- | ---
GET | `/api/users` | List users
POST | `/api/user/create` | Creates a user



### Installation 

 
First ensure you have python globally installed in your computer. If not, you can get python [here](python.org).

After doing this, confirm that you have installed virtualenv globally as well. If not, run this:

    $ pip install virtualenv

Create a virtual environment

    $ virtualenv .venv && source .venv/bin/activate
Install dependancies

    $ pip install -r requirements.txt
Make migrations & migrate

### Set database
make postgreSql database with any name
and update environment variables accordingly in .env file  which is located inside directory configurations

then 
    $ python manage.py makemigrations && python manage.py migrate
Create Super user
    
    $ python manage.py createsuperuser

### Launching the app
    $ python manage.py runserver