from flask import Flask, render_template
from flask_socketio import SocketIO, emit, join_room, leave_room

app = Flask(__name__ )
app.config['SECRET_KEY'] = 'top-secret!'
app.config['SESSION_TYPE'] = 'filesystem'
socketio = SocketIO(app)


@app.route('/')
def main_page():
   return  render_template('index.html')

@app.route('/getcallerData', methods=['POST', 'GET'])
def getcallerData():
    if request.method == 'POST':
        data = request.get_json()
         # getcallerData(data)
        return jsonify("ok")


if __name__ == '__main__':
    socketio.run(app, host="0.0.0.0", port=8080, debug=True)
    # app.run(debug=True)