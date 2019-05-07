from flask import Flask
from redis import Redis

app = Flask(__name__)
redis = Redis(host='redis', port=6379)

@app.route('/')
def hello():
    visits_count = redis.incr('visits')
    return f"Hello you :D\r\nthis site was visited {visits_count} time(s)!"

@app.route('/data_consumed')
def data_consumed():
    counter = redis.get('data_consumed')
    return counter