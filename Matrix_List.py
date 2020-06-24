from os import system,name

matrixend = []
matrixcopy = []

for x in range(0, 5, 1):
    matrix = []

    matrix.append (int(input("Digite o termo {} da linha {}: ".format(x+1, 1))))
    matrix.append (int(input("Digite o termo {} da linha {}: ".format(x+1, 2))))
    matrix.append (int(input("Digite o termo {} da linha {}: ".format(x+1, 3))))
    matrix.append (int(input("Digite o termo {} da linha {}: ".format(x+1, 4))))
    matrix.append (int(input("Digite o termo {} da linha {}: ".format(x+1, 5))))

    matrixend.append (matrix)

    system('cls' if name == 'nt' else 'clear')

valor = int(input("Qual é o valor que deseja multiplicar em linha: "))

system('cls' if name == 'nt' else 'clear')

for x in range(0, 5, 1):
    matrixcopy.append (matrixend[x])

print("Ela era assim:")

for x in range(0, 5, 1):
    print(matrixcopy[x])

for x in range(0, 5, 1):
    matrixend[x][x] = (matrixend[x][x]*valor)

print("Agora ficou assim:")

for x in range(0, 5, 1):
    print(matrixend[x])