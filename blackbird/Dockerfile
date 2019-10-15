FROM python:3

WORKDIR /usr/src/app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install psycopg2
RUN apt-get update
RUN apt-get --assume-yes install netcat
RUN pip install psycopg2


RUN pip install --upgrade pip
RUN pip install pipenv
COPY ./Pipfile /usr/src/app/Pipfile
RUN pipenv install

COPY . /usr/src/app/

ENTRYPOINT ["/usr/src/app/entrypoint.sh"]
