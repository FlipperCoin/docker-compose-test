FROM python:3.7.2-slim

COPY . /app
WORKDIR /app

RUN pip install pipenv

RUN pipenv install --system --deploy

CMD ["flask", "run", "--host=0.0.0.0"]