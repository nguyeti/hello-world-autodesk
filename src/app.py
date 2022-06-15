from flask import Flask, request
from .logger import get_logger

logger = get_logger(__name__)

app = Flask(__name__)


@app.after_request
def log_request(response):
    """
        Log HTTP request details
    """
    url = f"{request.host}{request.path}"
    logger.debug(url)
    return response


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if 'name' in request.json:
            name = request.json.get('name')
            return {'message': f'Hello, {name}'}, 200
        else:
            return {'message': '400 Bad Request'}, 400
    else:
        accept_header = request.headers.get('Accept', None)
        if accept_header and accept_header == 'application/json':
            return {'message': 'Hello, World'}, 200
        else:
            return '<p>Hello, World</p>', 200


if __name__ == '__main__':
    app.run()
