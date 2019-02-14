FROM python:3.6

RUN apt-get update
RUN apt-get install -y gdal-bin libpq-dev python-dev
RUN pip install pipenv

COPY ./Pipfile /src/Pipfile
COPY ./Pipfile.lock /src/Pipfile.lock

WORKDIR /src

RUN pipenv install
ENTRYPOINT ["pipenv", "run"]