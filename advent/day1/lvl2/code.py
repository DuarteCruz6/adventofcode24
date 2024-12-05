left=[]
right=[]

for i in range(1000):
    a,b=[int(i) for i in input().split()]
    left.append(a)
    right.append(b)
    left.sort()
    right.sort()

total=0
for i in left:
    total+=i*right.count(i)
print(total)