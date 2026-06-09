n1, n2, n3, n4 = map(float, input().split())
media = ((n1 * 2) + (n2 * 3) + (n3 * 4) + n4) / 10
if 5 <= media < 7:
        ne = float(input())
        mediafinal = (media + ne) / 2
print(f"Media: {media:.1f}")
if media >= 7.0:
            print("Aluno aprovado.")
elif 5.0 > media:
            print("Aluno reprovado.")
else:
            print("Aluno em exame.")
            print(f"Nota do exame: {ne:.1f}")
            if mediafinal >= 5.0:
                print("Aluno aprovado.")
            else:
                print("Aluno reprovado.")
            print(f"Media final: {mediafinal:.1f}")
                    