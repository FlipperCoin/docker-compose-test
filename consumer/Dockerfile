FROM python:3.7.2-slim

COPY . /app
WORKDIR /app

RUN pip install pipenv

RUN pipenv install --system --deploy

CMD ["python", "consumer.py"]