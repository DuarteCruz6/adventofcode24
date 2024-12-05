def increasing(report):
    for i in range(len(report)-1):
        if report[i]>=report[i+1]:
            return False
        if report[i+1]-report[i]>3:
            return False
    return True

def decreasing(report):
    for i in range(len(report)-1):
        if report[i]<=report[i+1]:
            return False
        if report[i]-report[i+1]>3:
            return False
    return True

total=0
for i in range(1000):
    report = [int(i) for i in input().split()]
    if(report[0]<report[1]):
        if increasing(report):
            total+=1
    elif(report[1]<report[0]):
        if decreasing(report):
            total+=1
print(total)
        