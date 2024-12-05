matrix = []
total = 0

for i in range(140):
    line = input()
    temp = []
    for letter in line:
        temp.append(letter)
    matrix.append(temp)


def verifyLine(line, column):
    global total
    try:
        #Verify "SAMX" 
        if matrix[line][column-3:column+1] == ["S", "A", "M", "X"]:
            total += 1
        #Verify "XMAS"
        if matrix[line][column:column+4] == ["X", "M", "A", "S"]:
            total += 1
    except IndexError:
        pass


def verifyDiagonals(line, column):
    global total
    try:
        #to the right and upwards
        if (
            matrix[line-1][column+1] == "M"
            and matrix[line-2][column+2] == "A"
            and matrix[line-3][column+3] == "S"
        ):
            total += 1
        #to the left and upwards
        if (
            matrix[line-1][column-1] == "M"
            and matrix[line-2][column-2] == "A"
            and matrix[line-3][column-3] == "S"
        ):
            total += 1
        #to the right and downwards
        if (
            matrix[line+1][column+1] == "M"
            and matrix[line+2][column+2] == "A"
            and matrix[line+3][column+3] == "S"
        ):
            total += 1
        #to the left and downwards
        if (
            matrix[line+1][column-1] == "M"
            and matrix[line+2][column-2] == "A"
            and matrix[line+3][column-3] == "S"
        ):
            total += 1
    except IndexError:
        pass


def verifyColumn(line, column):
    global total
    try:
        #Updwards
        if (
            matrix[line-1][column] == "M"
            and matrix[line-2][column] == "A"
            and matrix[line-3][column] == "S"
        ):
            total += 1
        #Downwards
        if (
            matrix[line+1][column] == "M"
            and matrix[line+2][column] == "A"
            and matrix[line+3][column] == "S"
        ):
            total += 1
    except IndexError:
        pass


for line in range(len(matrix)):
    for column in range(len(matrix[line])):
        letter = matrix[line][column]
        if letter == "X":
            verifyLine(line, column)
            verifyDiagonals(line, column)
            verifyColumn(line, column)

print(total)
