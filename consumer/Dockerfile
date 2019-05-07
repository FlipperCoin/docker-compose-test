FROM python:3.7.2-slim

RUN pip install pipenv

COPY Pipfile Pipfile.lock /app/

WORKDIR /app

RUN pipenv install --system --deploy

COPY . /app

CMD ["python", "consumer.py"]