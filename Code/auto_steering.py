from communications.mapping import get_coords
import rpi_main as robot

# saves the walls of the the squares and if they have been visited
# front, right, back, left, visited
coords = [[[1,0,1,1,True], [1,0,1,0,False]], 
          [[1,0,1,1,False], [1,0,1,1,False]]]

# keeps track of the robots current direction (0 = forward/uppwards, 1 = right, 2 = back/downward, 3 = left)
current_dir = 0

# remembers the robots path by saving the directions needed to return to previously visited squares
path = []

# checks all walls around the start square and adds them and the neighbors to the coords grid, then moves the robot to the next square
def start_search():
    front, left, right = get_walls()

    rotate_right()
    back = 0
    if is_right_wall():
        back = 1
    rotate_left()

    x, y= 0, 0
    walls = [front, right, back, left, True]
    add_coord(x, y, walls)
    add_neighbors(x, y, front, right, left)
    move(x, y)
    get_coords(coords)

# search loop that moves the robot through the labyrith and saves the walls in coords grid
def search():
    start_search()
    x, y = 0, 0

    labyrinth_finished = False
    while(not labyrinth_finished):
        front, left, right = get_walls()
        back = 0
        walls = get_acctual_walls(front, right, back, left)
        x, y = uppdate_pos(x,y)
        add_coord(x,y,walls)
        add_neighbors(x, y, front, right, left)
        global coords
        get_coords(coords)

        if not move(x,y):
            global path
            if len(path) == 0:
                labyrinth_finished = True
            else:
                follow_path()
        
        labyrinth_finished = True

# returns true if any adjacent squares can be visited and hasen't been visited before, then moves the robot
def move(x,y):
    next_available = True

    if not is_right_wall() and not been_visited(x,y,1):
        rotate_right()

    elif not is_front_wall() and not been_visited(x,y,0):
        pass

    elif not is_left_wall() and not been_visited(x,y,3):
        rotate_left()

    else :
        next_available = False

    if next_available == True:
        move_one_block()
        add_to_path()

    return next_available

# moves the robot back, following the same path it came from
def follow_path():
    global current_dir
    last_dir = path.pop()
    diff = current_dir - last_dir
    if diff < 0:
        for i in range(abs(diff)):
            rotate_left()
    
    elif diff > 0:
        for i in range(diff):
            rotate_right()
    
    move_one_block()

# adds the direction to the previosly visited square to the path
def add_to_path():
    dir_right()
    dir_right()
    global current_dir
    opposite_dir = current_dir
    dir_left()
    dir_left()
    global path
    path.append(opposite_dir)

# returns true if the square has been visited before
def been_visited(x, y, square):
    if square == 0: #front
        new_x, new_y = uppdate_pos(x,y)
        
    elif square == 1: #right
        dir_right()
        new_x, new_y = uppdate_pos(x,y)
        dir_left()
    
    elif square == 3: #left
        dir_left()
        new_x, new_y = uppdate_pos(x,y)
        dir_right()

    return coords[new_y][new_x][4]

# adds neighbors to the coords grid
def add_neighbors(x, y, front, right, left):
    if front == 0:
        add_neighbor(x,y,0)
    if right == 0:
        add_neighbor(x,y,1)
    if left == 0:
        add_neighbor(x,y,3)

# adds a neighbor to the coords grid
def add_neighbor(x, y, place):
    global current_dir
    old_dir = current_dir
    current_dir = place

    new_x, new_y = uppdate_pos(x,y)
    visited = False
    add_coord(new_x,new_x, [0,0,0,0,visited])

    current_dir = old_dir

# adds squares to the cords grid
def add_coord(x, y, walls):
    max_x = len(coords[0]) - 1
    max_y = len(coords) - 1
    global current_dir
    
    if x > max_x:
        for y_index in range(len(coords)):
            if y_index == y:
                coords[y_index].append(walls)
            else:
                coords[y_index].append([0,0,0,0, False])
    elif y > max_y:
        coords.append([])
        for x_index in range(len(coords[0])):
            if x == x_index:
                coords[y].append(walls)
            else:
                coords[y].append([0,0,0,0, False])

    elif coords[y][x][4] == False:
        coords[y][x] = walls

    elif x == 0 and y == 0:
        if current_dir == 3:
            for y_index in range(len(coords)):
                if y == y_index:
                    coords[y_index].insert(x, walls)
                else:
                    coords[y_index].insert(x, [0,0,0,0, False])
        
        elif current_dir == 0:
            global start_y
            coords.insert(y, [])
            for x_index in range(len(coords[1])):
                if x == x_index:
                    coords[y].append(walls)
                else:
                    coords[y].append([0,0,0,0, False])   

# returns uppdated x and y-coordinates based on the current direction of the robot     
def uppdate_pos(x, y):
    global current_dir
    if current_dir == 0:
        y = y - 1
        if y == -1:
            y = 0
    elif current_dir == 1:
        x = x + 1
    elif current_dir == 2:
        y = y + 1
    elif current_dir == 3:
        x = x - 1
        if x == -1:
            x = 0
    return x, y

# returns the binary values of the walls as seen from the robots perspective
def get_walls():
    front = 0
    if is_front_wall():
        front = 1

    left = 0
    if is_left_wall():
        left = 1

    right = 0
    if is_right_wall():
        right = 1

    return front, left, right

# returns the binary values of the walls as seen from the map view
def get_acctual_walls(front, right, back, left):
    global current_dir
    new_coords = [front, right, back, left, True]
    for d in range(current_dir):
        new_left = new_coords[3]
        new_coords[3] = new_coords[2]
        new_coords[2] = new_coords[1]
        new_coords[1] = new_coords[0]
        new_coords[0] = new_left
    
    return new_coords

# moves the robot one block forward
def move_one_block():
    robot.driveForward(40, buss)
    return

# changes the current direction to the right
def dir_right():
    global current_dir
    current_dir = current_dir + 1
    if current_dir == 4:
        current_dir = 0
    
# changes the current direction to the left
def dir_left():
    global current_dir
    current_dir = current_dir - 1
    if current_dir == -1:
        current_dir = 3

# rotates the robot 90 degrees to the right
def rotate_right():
    robot.turnRight(90, bus)
    dir_right()

# rotates the robot 90 degrees to the right
def rotate_left():
    robot.turnLeft(90, bus)
    dir_left()
    
# rotates the robot 180 degrees
def rotate_180():
    rotate_right()
    rotate_right()

# returns true if there is a wall in front of the robot
def is_front_wall():
    return robot.isFrontWall(bus)


# returns true if there is a wall to the right of the robot
def is_right_wall():
    return robot.isRightWall(bus)

# returns true if there is a wall to the left of the robot
def is_left_wall():
    return robot.isLeftWall(bus)

# prints the coord grid
def print_coords(coords):
    for i in range(len(coords)):
        print(coords[i])


search()
print_coords(coords)