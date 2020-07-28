FROM python:3.7

ADD ./app /usr/local/app
WORKDIR /usr/local/app
RUN pip install -r /usr/local/app/requirements.txt

CMD ["python", "app.py"]
