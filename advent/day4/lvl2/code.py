matrix=[]
total=0
#150
for i in range(150):
    total=0
    line=input()
    temp=[]
    for letter in line:
        temp.append(letter)
    matrix.append(temp)

def verifyRightSide(line,column):
    global total
    try:
        if line-1>-1 and column-1>-1:
            if matrix[line-1][column+1]=="M" and matrix[line+1][column-1]=="S":
                return True
            elif matrix[line-1][column+1]=="S" and matrix[line+1][column-1]=="M":
                return True
    except:
        return False
    
def verifyLeftSide(line,column):
    global total
    try:
        if line-1>-1 and column-1>-1:
            if matrix[line-1][column-1]=="M" and matrix[line+1][column+1]=="S":
                return True
            elif matrix[line-1][column-1]=="S" and matrix[line+1][column+1]=="M":
                return True
    except:
        return False
        
for line in range(len(matrix)):
    string = matrix[line]
    for column in range(len(string)):
        letter = string[column]
        if letter=="A":
            if verifyRightSide(line,column) and verifyLeftSide(line,column):
                total+=1
            
print(total)