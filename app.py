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


@app.route("/size/<cell_size>/<res_size>")
def size_route(cell_size, res_size = "1000x1000"):
    # size = request.args["size"]
    print(cell_size)
    length = int(res_size.split("x")[0])
    width = int(res_size.split("x")[1])
    # size = "10x10"
    maze = Maze(cell_size)
    maze.make_maze_mazey()
    draw_maze(maze.walls, str(cell_size), length,width, str(cell_size))
    return send_file(f"{cell_size}.png")

if __name__ == '__main__':
    # Threaded option to enable multiple instances for multiple user access support
    app.run(threaded=True, port=5000)


