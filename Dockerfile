FROM python:3.8

COPY ./src /src/
ADD requirements.txt .

RUN pip install -r requirements.txt

ENTRYPOINT ["python", "./src/routes.py"]