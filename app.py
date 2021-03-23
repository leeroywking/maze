from flask import Flask, send_file#, request
from maze_threader import Mazethread
from maze_primitives.maze import Maze
from maze_primitives.draw_maze import draw_maze


app = Flask(__name__)
maze_generator = Mazethread()
# A welcome message to test our server
@app.route('/')
def index():
    return send_file("./image2.png")


@app.route("/size/<size>")
def size_route(size):
    # size = request.args["size"]
    maze = Maze(size)
    maze.make_maze_mazey()
    draw_maze(maze.walls, size)
    return send_file(f"{size}.png")

if __name__ == '__main__':
    # Threaded option to enable multiple instances for multiple user access support
    app.run(threaded=True, port=5000)


