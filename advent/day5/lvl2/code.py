dic={}
ans=[]

def checkSeq(seq):
    modified = True
    while modified:
        modified = False
        for index in range(len(seq)):
            page = seq[index]
            if not check(index, page):
                order(index, page)
                modified = True
                if seq not in ans:
                    ans.append(seq)
                break
            
def order(index, page):
    keys = dic.get(page, [])
    for after in keys:
        if after in seq[:index]:
            afterIndex = seq[:index].index(after)
            seq[afterIndex], seq[index] = seq[index], seq[afterIndex]

def check(index, page):
    keys = dic.get(page, [])
    for after in keys:
        if after in seq[:index]:
            return False
    return True
    
    

#1176
#21
for i in range(1176):
    a,b=input().split("|")
    if a in dic:
        dic[a].append(b)
    else:
        dic[a]=[b]


#190
#6
for i in range(190):
    seq=input().split(",")
    checkSeq(seq)


total = 0
for seq in ans:
    seq = list(seq)  # Converter de volta para lista
    total += int(seq[len(seq) // 2])

print(total)







