while True:
    n = int(input())

    if n == 0:
        break

    for i in range(n):
        linha = ""

        for j in range(n):

            topo = i
            esquerda = j
            baixo = n - 1 - i
            direita = n - 1 - j

            valor = min(topo, esquerda, baixo, direita) + 1

            linha += f"{valor:3}"

            if j != n - 1:
                linha += " "

        print(linha)

    print()