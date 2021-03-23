import threading
from maze_primitives.maze import Maze
from maze_primitives.draw_maze import draw_maze

class Mazethread(object):
    def __init__(self, interval=1):
        self.interval = interval
        thread = threading.Thread(target=self.run, args=())
        thread.daemon = True
        thread.start()

    def run(self):
        while True:
            maze = Maze("25x25")
            maze.make_maze_mazey()
            draw_maze(maze.walls)