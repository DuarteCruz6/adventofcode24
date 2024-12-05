tabela=[]
total=0
#150
for i in range(150):
    total=0
    linha=input()
    temp=[]
    for letra in linha:
        temp.append(letra)
    tabela.append(temp)

def verificarDireita(linha,coluna):
    global total
    try:
        if linha-1>-1 and coluna-1>-1:
            if tabela[linha-1][coluna+1]=="M" and tabela[linha+1][coluna-1]=="S":
                return True
            elif tabela[linha-1][coluna+1]=="S" and tabela[linha+1][coluna-1]=="M":
                return True
    except:
        return False
    
def verificarEsquerda(linha,coluna):
    global total
    try:
        if linha-1>-1 and coluna-1>-1:
            if tabela[linha-1][coluna-1]=="M" and tabela[linha+1][coluna+1]=="S":
                return True
            elif tabela[linha-1][coluna-1]=="S" and tabela[linha+1][coluna+1]=="M":
                return True
    except:
        return False
        
for linha in range(len(tabela)):
    string = tabela[linha]
    for coluna in range(len(string)):
        letra = string[coluna]
        if letra=="A":
            if verificarDireita(linha,coluna) and verificarEsquerda(linha,coluna):
                total+=1
            
print(total)