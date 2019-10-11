from flask import Flask
from localdatabase import get_count_book


app = Flask(__name__)


@app.route('/')
def index():
    return 'Hello World'


@app.route('/book/')
def book():
    count = get_count_book()
    return "тут будут книги, на данный момент их {}".format(count)


if __name__ == "__main__":
    app.run(debug=True)
