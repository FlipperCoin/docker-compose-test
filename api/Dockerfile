FROM python:3.7.2-slim

RUN pip install pipenv

COPY Pipfile Pipfile.lock /app/

WORKDIR /app

RUN pipenv install --system --deploy

COPY . /app

CMD ["flask", "run", "--host=0.0.0.0"]