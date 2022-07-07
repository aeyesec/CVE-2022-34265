FROM python:3

RUN apt-get update -y
RUN apt-get install libpq-dev -y

RUN pip3 install django==4.0.5
RUN pip3 install psycopg2==2.8.6
RUN django-admin startproject app
WORKDIR /app

RUN python3 manage.py startapp vuln

COPY settings.py app/settings.py
COPY models.py vuln/models.py
COPY views.py vuln/views.py
COPY urls.py app/urls.py

EXPOSE 8000
