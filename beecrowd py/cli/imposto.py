a = float(input())
if a <= 2000.00:
    print("Isento")
elif 2000.00 < a <= 3000.00:
    print("R$ {:.2f}".format(a * 0.08))
elif 3000 < a <= 4500.00:
    print("R$ {:.2f}".format(a * 0.18))
else:
    print("R$ {:.2f}".format(a * 0.28))