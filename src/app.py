"""
This aims to create a wrapper REST service for readtime prediction
"""

from flask import Flask, request, abort

from prediction_service import predict_time

app = Flask(__name__)


@app.route('/time', methods=['GET', 'POST'])
def calculate_time():
    if request.json and 'text' in request.json:
        return '%.2f seconds' % predict_time(request.json['text'])
    if request.form and 'text' in request.form:
        return '%.2f seconds' % predict_time(request.form['text'])

    abort(400)


@app.route('/')
def index():
    return '''
    <html>
        <head><title>Reading Time</title></head>
        <body>
            <form action="/time" method="POST">
                <label>
                    Text:
                    <textarea name="text" style="width: 100%; display: block; height: 400px" required></textarea>
                </label>
                <br>
                <button type="submit">Submit</button>
            </form>
        </body>
    </html>
    '''


if __name__ == '__main__':
    app.run()
