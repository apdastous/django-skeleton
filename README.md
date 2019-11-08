# To run locally

This all assumes late 2019ish debian/ubuntu/mint.

Install global pre-requisites:
```shell script
$ sudo apt-get install python3.6-dev build-essential virtualenv
```

Go to project root, create a python virtual environment, and install dependencies:
```shell script
$ virtualenv -p python3.6 venv
$ source venv/bin/activate
$ pip3 install -r requirements.txt
```

Create sqlite database (if you are not doing development on this project, this is a one time step):
```shell script
$ source venv/bin/activate
$ python manage.py migrate
```

Run the local dev server:
```shell script
$ source venv/bin/activate
$ python manage.py runserver
```

Open your browser and go to:

* http://localhost:8000/ 
* http://localhost:8000/monitoring/ping
* http://localhost:8000/admin/