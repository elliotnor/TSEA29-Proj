

coords = [[[0,0,0,0,False]]]

def get_coords(auto_map):
    global coords
    coords = auto_map


def get_sizes():
    global coords
    margin = 20
    squaresize1 = (400 - margin*2)/len(coords)
    
    squaresize2 =(400 - margin*2)/len(coords[0])
    squaresize = 0
    top_margin = 0
    side_margin = 0
    if squaresize1 < squaresize2:
        squaresize = squaresize1
        top_margin = margin
        side_margin = (400 - squaresize*len(coords[0])) / 2

    else:
        squaresize = squaresize2
        top_margin = (400 - squaresize*len(coords)) / 2
        side_margin = margin 
    
    return squaresize, top_margin, side_margin
    

def get_map(mapWindow):
    mapWindow.delete('all')
    squaresize, top_margin, side_margin = get_sizes()
    global coords
    for y in range(len(coords)):
        for x in range(len(coords[y])):
            if coords[y][x][0] == 1:
                x1 = side_margin + squaresize*x
                x2 = x1 + squaresize
                y1 = top_margin + squaresize*y
                y2 = y1
                mapWindow.create_line(x1, y1, x2, y2, fill="tan4", width=2)               
           
            if coords[y][x][1] == 1:
                x1 = side_margin + squaresize*(x + 1)
                x2 = x1
                y1 = top_margin + squaresize*y
                y2 = y1 + squaresize
                mapWindow.create_line(x1, y1, x2, y2, fill="tan4", width=2)
        

            if coords[y][x][2] == 1:
                x1 = side_margin + squaresize*x
                x2 = x1 + squaresize
                y1 = top_margin + squaresize*(y + 1)
                y2 = y1
                mapWindow.create_line(x1, y1, x2, y2, fill="tan4", width=2)

            if coords[y][x][3] == 1:
                x1 = side_margin + squaresize*x
                x2 = x1
                y1 = top_margin + squaresize*y
                y2 = y1 + squaresize
                mapWindow.create_line(x1, y1, x2, y2, fill="tan4", width=2)
           
