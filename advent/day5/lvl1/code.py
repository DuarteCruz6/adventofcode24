dic={}
ans=[]

def check(index,page):
    global dic
    try:
        keys = dic[page]

        for after in keys.split(","):
            if after in seq[0:index]:
                return False
        return True
    except:
        return True
    
    

#1176
for i in range(1176):
    a,b=input().split("|")
    if a in dic:
        dic[a]+=b+","
    else:
        dic[a]=b+","

for i in range(190):
    
    a=True
    seq=input().split(",")
    for index in range(len(seq)):
        page=seq[index]
        if not check(index,page):
            a=False
            break
    if a:
        ans.append(seq)

total=0
for i in ans:
    total+=int(i[len(i)//2])
print(total)