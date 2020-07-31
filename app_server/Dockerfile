FROM python:3.7

RUN apt-get update \
 && apt-get install -y \
    redis-tools \
 && apt-get -y clean \
 && rm -rf /var/lib/apt/lists/*

ADD ./app /usr/local/app
WORKDIR /usr/local/app
RUN pip install -r /usr/local/app/requirements.txt

CMD ["python", "app.py"]
