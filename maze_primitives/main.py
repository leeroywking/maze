#!/bin/usr/python3

from maze import Maze
from draw_maze import draw_maze

if __name__ == "__main__":
    size = "10x10"
    maze = Maze(size)
    maze.make_maze_mazey()
    # maze.show_maze_data()
    draw_maze(maze.walls, size, 1000,1000)