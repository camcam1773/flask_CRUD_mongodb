FROM python:3.9-alpine

ADD app.py /
ADD requirements.txt /
ADD ./templates /templates/

RUN pip install -r requirements.txt

EXPOSE 8080
CMD [ "python", "./app.py" ]
