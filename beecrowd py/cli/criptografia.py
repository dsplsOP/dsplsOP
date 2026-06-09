n = int(input())

for _ in range(n):
    texto = str(input())

    # 🔹 1ª passada: +3 nas letras
    passo1 = ""
    for c in texto:
        if c.isalpha():
            passo1 += chr(ord(c) + 3)
        else:
            passo1 += c

    # 🔹 2ª passada: inverter
    passo2 = passo1[::-1]

    # 🔹 3ª passada: metade pra frente -1
    resultado = ""
    metade = len(passo2) // 2

    for i in range(len(passo2)):
        if i >= metade:
            resultado += chr(ord(passo2[i]) - 1)
        else:
            resultado += passo2[i]

    print(resultado)