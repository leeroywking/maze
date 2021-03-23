from flask import Flask, send_file
from maze_primitives.maze import Maze
from maze_primitives.draw_maze import draw_maze

app = Flask(__name__)

# A welcome message to test our server
@app.route('/')
def index():
    maze = Maze("25x25")
    maze.make_maze_mazey()
    draw_maze(maze.walls)



    return send_file("./image2.png")

if __name__ == '__main__':
    # Threaded option to enable multiple instances for multiple user access support
    app.run(threaded=True, port=5000)



# if __name__ == "__main__":
#     maze = Maze("25x25")
#     maze.make_maze_mazey()
#     # maze.show_maze_data()
#     draw_maze(maze.walls)

