# Poor Man's Twitter
## Installation
### Requirements
Install these and set them up to run from terminal.
* Python 3
* pip

### Install dependencies
Install all the project dependencies using the requirements.txt file.
```
pip install -r requirements.txt
```
(you can opt to set a virtualenv if you want).

## Run the server
Change directory to the root of the backend app.
```
cd Backend/PoorManTwitter
```
The first time you run it you have to init the database.

```
python manage.py makemigrations api
python manage.py migrate
```

Run the server.
```
python manage.py runserver
```

## Running the tests

Use manage.py to run the unit tests.
```
python manage.py test
```

## Run the client
Open Frontend/index.html in your browser.