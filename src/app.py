from flask import Flask, jsonify
import datetime
import socket
import os

app = Flask(__name__)

@app.route('/api/v1/details')
def details():
    return jsonify({
        'message': 'Hello World',
        'time': datetime.datetime.now().strftime("%I:%M:%S%p on %B %d, %Y"),
        'server': socket.gethostname(),
        'env_user': os.getenv('USER', 'Not Set')
#        'message2' : 'bye bye'
    })

@app.route('/api/v1/healthz')
def healthz():
    return jsonify({'status': 'up'}), 200

if __name__ == '__main__':

    app.run(host="0.0.0.0")