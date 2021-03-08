import random

class Maze:
    def __init__(self, size):
        self.size = size
        self.length = int(size.split("x")[0])
        self.height = int(size.split("x")[1])
        self.nodes = self.build_nodes(size)
        self.edges = self.build_edges(size)
        self.walls = []
        self.last_wall = []

    def build_nodes(self, size):
        nodes = {}
        for x in range(self.length):
            for y in range(self.height):
                nodes[f"{x},{y}"] = {"edges": []}
        # print(nodes)
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

    def does_path_exist(self, start, end):
        # gonna do a depth first search
        checked_nodes = []
        to_check_nodes = [start]
        while len(to_check_nodes) > 0:
            curr_node = to_check_nodes.pop(0)
            if curr_node not in checked_nodes:
                checked_nodes.append(curr_node)
                if curr_node == end:
                    return True
                else:
                    for edge in self.nodes[curr_node]["edges"]:
                        to_check_nodes.append(edge)
        return False
    
    def do_multiple_paths_exist(self, start, end):
        checked_nodes = []
        to_check_nodes = [start]
        success_count = 0
        while len(to_check_nodes) > 0 or success_count >1:
            curr_node = to_check_nodes.pop(0)
            if curr_node not in checked_nodes:
                checked_nodes.append(curr_node)
                if curr_node == end:
                    success_count += 1
                else:
                    for edge in self.nodes[curr_node]["edges"]:
                        to_check_nodes.append(edge)
        if success_count >1:
            return True
        else:
            return False

    def show_maze_data(self):
        # print(f"nodes:{self.nodes}\n\nedges:{self.edges}")
        print(self.walls)
        print(self.last_wall)

    def make_maze_mazey(self):
        last_edge = ""
        while self.does_path_exist("0,0", "24,24"):
            edge_to_remove = self.edges[random.randint(0,len(self.edges)-1)]
            last_edge = edge_to_remove
            self.edges.remove(edge_to_remove)
            [first_coord, second_coord] = edge_to_remove.split(":")
            self.nodes[first_coord]["edges"].remove(second_coord)
            self.nodes[second_coord]["edges"].remove(first_coord)
            self.walls.append(edge_to_remove)
        #add last edge back in
        [first_coord, second_coord] = last_edge.split(":")
        self.nodes[first_coord]["edges"].append(second_coord)
        self.nodes[second_coord]["edges"].append(first_coord)
        self.walls.remove(last_edge)
        self.last_wall.append(last_edge)

if __name__ == "__main__":
    maze = Maze("25x25")
    # maze.nodes["0,1"]["edges"] = []
    # maze.nodes["1,1"]["edges"] = []
    # maze.nodes["2,1"]["edges"] = []
    # if maze.does_path_exist("0,0", "2,2"):
    #     print("A path exists!")
    # else:
    #     print("The path is cut")
    # maze.show_maze_data()
    maze.make_maze_mazey()
    maze.show_maze_data()

