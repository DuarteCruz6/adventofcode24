levels=[]
unique=0
guard_level=0
guard_col=0

#10
#130
maxLevel=maxCol=130

def checkBounds(newLevel, newCol):
    if newLevel>-1 and newLevel <maxLevel and newCol>-1 and newCol<maxCol:
        return True
    return False

def over():
    print(unique)

def move():
    global levels, unique, guard_level, guard_col
    directions = {
        "up":(-1, 0, "right"),
        "down":(1, 0, "left"),
        "left":(0, -1, "up"),
        "right":(0, 1, "down"),
    }

    current_direction = "up"
    while True:
        rowOffset, colOffset, next_direction = directions[current_direction]
        new_level = guard_level+rowOffset
        new_col = guard_col+colOffset

        if not checkBounds(new_level, new_col):
            #out of bounds
            over()
            break
        
        new_square = levels[new_level][new_col]
        if new_square == "#": 
            #turns 90 degrees
            current_direction = next_direction
            
        elif new_square == ".":
            #unique cell
            unique+=1
            guard_level, guard_col=new_level, new_col
            levels[guard_level][guard_col]="X"
            
        elif new_square == "X":
            #already passed by
            guard_level, guard_col=new_level, new_col
                
for i in range(maxLevel):
    string = input()
    level=[]
    for pos in string:
        level.append(pos)
    levels.append(level)
    if "^" in level:
        guard_level=i
        guard_col=level.index("^")
        
levels[guard_level][guard_col]="X"
unique+=1
move()
    
    
    
    

# type: ignore