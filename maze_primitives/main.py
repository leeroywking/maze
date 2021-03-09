from maze import Maze
from draw_maze import draw_maze

if __name__ == "__main__":
    maze = Maze("25x25")
    maze.make_maze_mazey()
    # maze.show_maze_data()
    draw_maze(maze.walls)