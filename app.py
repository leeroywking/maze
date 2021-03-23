from flask import Flask, send_file
from maze_threader import Mazethread

app = Flask(__name__)
maze_generator = Mazethread()
# A welcome message to test our server
@app.route('/')
def index():
    return send_file("./image2.png")


if __name__ == '__main__':
    # Threaded option to enable multiple instances for multiple user access support
    app.run(threaded=True, port=5000)


