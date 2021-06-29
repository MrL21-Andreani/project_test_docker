FROM python:3.8
WORKDIR /test_docker

ENV FLASK_APP app.py

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY . .
CMD ["flask","run"]



