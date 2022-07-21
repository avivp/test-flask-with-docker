# test-flask-with-docker
integration test of python flask app using pytest against docker

raising a docker container using pytest, and running web request against flask app running in docker.


## Run python script

> python src/routes.py

Navigate to http://127.0.0.1:5000/item/1 to hit Flask app running localy

## Build and run docker

> pip freeze > requirements.txt

> docker build -t <img_name> .

> docker run -d -p 5000:5000 <img_name>

Navigate to http://127.0.0.1:5000/item/1 to hit Flask app running in container

## Run integration test
> pytest test/test_webapp_int.py

