L = int(input())
T = input()

matriz = []

for i in range(12):
    linha = []
    for j in range(12):
        linha.append(float(input()))
    matriz.append(linha)

soma = 0

for j in range(12):
    soma += matriz[L][j]

if T == 'S':
    print(f"{soma:.1f}")
else:
    media = soma / 12
    print(f"{media:.1f}")