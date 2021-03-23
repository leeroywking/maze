# from maze_maker.maze_primitives.maze import Maze
from PIL import Image, ImageDraw, ImageFont
import sys

def draw_maze(walls, filename = "image2.png"):
    img = Image.new("RGB", (1000, 1000), (255, 255, 255))
    img.save("image.png", "PNG")
    draw = ImageDraw.Draw(img)
    draw.line((0,0,0,1000),fill=200,width=5)
    draw.line((0,1000,1000,1000),fill=200,width=5)
    draw.line((1000,0,1000,1000),fill=200,width=5)
    draw.line((0,0,1000,0),fill=200,width=5)
    # get a font
    # fnt = ImageFont.truetype("./aquire-font/Aquire-BW0ox.otf", 8)
    # draw.multiline_text((5,5), "Start", font=fnt, fill=(0, 0, 0))
    # draw.multiline_text((975,980), "End", font=fnt, fill=(0, 0, 0))

    for wall in walls:
        [node1, node2] = wall.split(":")
        [node1_x, node1_y] = [int(node1.split(",")[0]) , int(node1.split(",")[1])]
        [node2_x, node2_y] = [int(node2.split(",")[0]), int(node2.split(",")[1])]
        if node1_x - node2_x != 0:
            #vertical line
            draw.line((node2_x*40,node2_y*40,node2_x*40,(node2_y +1) *40),fill=200,width=5)
            pass
        elif node1_y - node2_y != 0:
            #horizontal line
            draw.line((node2_x*40,node2_y*40,(node2_x +1) *40,node2_y *40),fill=200,width=5)
            pass
    img.save(f"{filename}.png", "PNG")
    # img.show()


if __name__=="__main__":
    example_walls = ['1,6:2,6', '4,1:4,2', '4,8:4,9', '5,1:5,2', '8,0:8,1', '2,8:2,9', '7,7:7,8', '0,1:0,2', '3,1:4,1', '1,2:2,2', '4,0:5,0', '2,1:2,2', '0,7:1,7', '0,6:0,7', '5,7:6,7', '8,3:8,4', '7,8:7,9', '7,5:8,5', '7,1:8,1', '8,1:8,2', '5,3:5,4', '1,0:2,0', '3,5:3,6', '6,3:7,3', '0,2:1,2', '8,2:8,3', '6,0:7,0', '2,4:3,4', '5,4:6,4', '6,1:6,2', '8,7:8,8', '2,7:3,7', '9,7:9,8', '3,2:3,3', '1,6:1,7', '3,4:3,5', '1,9:2,9', '1,0:1,1', '8,5:9,5', '5,6:5,7', '6,6:7,6', '5,1:6,1', '2,4:2,5', '1,1:1,2', '6,1:7,1', '1,7:2,7', '3,0:3,1', '5,5:6,5', '3,8:4,8', '2,6:3,6', '5,2:6,2', '5,5:5,6', '5,6:6,6', '7,0:7,1', '1,5:2,5', '2,6:2,7', '0,8:1,8', '1,4:2,4', '4,4:4,5', '7,2:7,3', '9,5:9,6', '7,2:8,2', '4,5:5,5', '4,3:4,4', '1,4:1,5', '3,6:4,6', '6,5:6,6', '1,5:1,6', '8,5:8,6', '8,3:9,3', '4,9:5,9', '7,8:8,8', '4,8:5,8', '8,8:9,8', '5,8:5,9', '0,3:0,4', '7,7:8,7', '3,3:4,3', '9,6:9,7', '6,4:6,5', '4,3:5,3']
    draw_maze(example_walls)
    