tabela = []
total = 0

for i in range(140):
    linha = input()
    temp = []
    for letra in linha:
        temp.append(letra)
    tabela.append(temp)


def verificarLinha(linha, coluna):
    global total
    try:
        # Verifica "SAMX" para trás
        if tabela[linha][coluna-3:coluna+1] == ["S", "A", "M", "X"]:
            total += 1
        # Verifica "XMAS" para a frente
        if tabela[linha][coluna:coluna+4] == ["X", "M", "A", "S"]:
            total += 1
    except IndexError:
        pass


def verificarDiagonais(linha, coluna):
    global total
    try:
        # Direita superior
        if (
            tabela[linha-1][coluna+1] == "M"
            and tabela[linha-2][coluna+2] == "A"
            and tabela[linha-3][coluna+3] == "S"
        ):
            total += 1
        # Esquerda superior
        if (
            tabela[linha-1][coluna-1] == "M"
            and tabela[linha-2][coluna-2] == "A"
            and tabela[linha-3][coluna-3] == "S"
        ):
            total += 1
        # Direita inferior
        if (
            tabela[linha+1][coluna+1] == "M"
            and tabela[linha+2][coluna+2] == "A"
            and tabela[linha+3][coluna+3] == "S"
        ):
            total += 1
        # Esquerda inferior
        if (
            tabela[linha+1][coluna-1] == "M"
            and tabela[linha+2][coluna-2] == "A"
            and tabela[linha+3][coluna-3] == "S"
        ):
            total += 1
    except IndexError:
        pass


def verificarColuna(linha, coluna):
    global total
    try:
        # Para cima
        if (
            tabela[linha-1][coluna] == "M"
            and tabela[linha-2][coluna] == "A"
            and tabela[linha-3][coluna] == "S"
        ):
            total += 1
        # Para baixo
        if (
            tabela[linha+1][coluna] == "M"
            and tabela[linha+2][coluna] == "A"
            and tabela[linha+3][coluna] == "S"
        ):
            total += 1
    except IndexError:
        pass


for linha in range(len(tabela)):
    for coluna in range(len(tabela[linha])):
        letra = tabela[linha][coluna]
        if letra == "X":
            verificarLinha(linha, coluna)
            verificarDiagonais(linha, coluna)
            verificarColuna(linha, coluna)

print(total)
