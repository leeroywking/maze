import random

class Maze:
    def __init__(self, size):
        self.size = size
        self.length = int(size.split("x")[0])
        self.height = int(size.split("x")[1])
        self.start = "0,0"
        self.exit = f"{self.length-1},{self.height-1}"
        self.nodes = self.build_nodes(size)
        self.edges = self.build_edges(size)
        self.walls = []
        self.last_wall = []

    def build_nodes(self, size):
        nodes = {}
        for x in range(self.length):
            for y in range(self.height):
                nodes[f"{x},{y}"] = {"edges": []}
        return nodes

    def build_edges(self, size):
        edges = []
        # if there is a node and either its x or its y position is off by one from another node then it is linked by default at start
        for node in self.nodes:
            curr_x = int(node.split(",")[0])
            curr_y = int(node.split(",")[1])
            if f"{curr_x + 1},{curr_y}" in self.nodes:
                self.nodes[node]["edges"].append(f"{curr_x +1},{curr_y}")
                if f"{curr_x +1},{curr_y}:{curr_x},{curr_y}" not in edges:
                    edges.append(f"{curr_x},{curr_y}:{curr_x +1},{curr_y}")
            if f"{curr_x - 1},{curr_y}" in self.nodes:
                self.nodes[node]["edges"].append(f"{curr_x -1},{curr_y}")
                if f"{curr_x -1},{curr_y}:{curr_x},{curr_y}" not in edges:
                    edges.append(f"{curr_x},{curr_y}:{curr_x -1},{curr_y}")
            if f"{curr_x},{curr_y +1}" in self.nodes:
                self.nodes[node]["edges"].append(f"{curr_x},{curr_y+1}")
                if f"{curr_x},{curr_y +1}:{curr_x},{curr_y}" not in edges:
                    edges.append(f"{curr_x},{curr_y}:{curr_x},{curr_y +1}")
            if f"{curr_x},{curr_y -1}" in self.nodes:
                self.nodes[node]["edges"].append(f"{curr_x},{curr_y-1}")
                if f"{curr_x},{curr_y-1}:{curr_x},{curr_y}" not in edges:
                    edges.append(f"{curr_x},{curr_y}:{curr_x},{curr_y -1}")
        # print(edges)
        return edges

    def does_path_exist(self, start, end, already_visited_nodes = set()):
        # gonna do a depth first search
        checked_nodes = []
        to_check_nodes = [end]
        #already_visited_nodes is a set of nodes visited in a previous check
        while len(to_check_nodes) > 0:
            curr_node = to_check_nodes.pop(0)
            if curr_node not in checked_nodes:
                checked_nodes.append(curr_node)
                if curr_node == start or curr_node in already_visited_nodes:
                    already_visited_nodes.add(curr_node)
                    return True, already_visited_nodes
                else:
                    already_visited_nodes.add(curr_node)
                    for edge in self.nodes[curr_node]["edges"]:
                        to_check_nodes.append(edge)
        return False, already_visited_nodes

    def show_maze_data(self):
        print(f"nodes:{self.nodes}\n\nedges:{self.edges}")
        print(self.walls)
        print(self.last_wall)

    def remove_wall(self, edge):
        [first_coord, second_coord] = edge.split(":")
        self.nodes[first_coord]["edges"].append(second_coord)
        self.nodes[second_coord]["edges"].append(first_coord)
        self.walls.remove(edge)
        self.last_wall.append(edge)

    def add_wall(self, edge):
        self.edges.remove(edge)
        [first_coord, second_coord] = edge.split(":")
        self.nodes[first_coord]["edges"].remove(second_coord)
        self.nodes[second_coord]["edges"].remove(first_coord)
        self.walls.append(edge)

    def make_maze_mazey(self):
        while len(self.edges) > 0:
            edge_to_remove = self.edges[random.randint(0, len(self.edges) - 1)]
            self.add_wall(edge_to_remove)
            already_visited_nodes = set()
            for node in self.nodes:
                path_exists , already_visited_nodes = self.does_path_exist(self.start,node, already_visited_nodes)
                if path_exists == False:
                    self.remove_wall(edge_to_remove)
                    break




if __name__ == "__main__":
    maze = Maze("25x25")
    maze.make_maze_mazey()
    # maze.show_maze_data()

