FROM python:3.10-alpine

ADD app.py /
ADD requirements.txt /
ADD ./templates /templates/
ADD ./tests tests/

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

EXPOSE 8080
CMD [ "python", "./app.py" ]
