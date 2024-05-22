from flask import Flask, render_template
from flask_socketio import SocketIO, emit

app = Flask(__name__)
socketio = SocketIO(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calender')
def calender():
    return render_template('calender.html')

@socketio.on('connect')
def test_connect():
    emit('new info', {'data': '新着情報があります！'})

if __name__ == '__main__':
    socketio.run(app)
