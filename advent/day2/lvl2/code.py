total=0

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

def check(report):
    global total
    notSafe = True
   
    if(report[0]<report[1]):
        if increasing(report):
            total+=1
            notSafe=False
    elif(report[1]<report[0]):
        if decreasing(report):
            total+=1
            notSafe=False
    return notSafe

for x in range(1000):
    report = [int(i) for i in input().split()]
    notSafe = check(report)
    if notSafe:
        for j in range(len(report)):
            newReport = report[:j]+report[j+1:]
            notSafe = check(newReport)
            if not notSafe:
                #we got one that works
                break
    
print(total)