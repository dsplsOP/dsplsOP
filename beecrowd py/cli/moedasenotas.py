a = float(input())
cem = int(a // 100)
a = (a - cem * 100) % 100
cnqt = int(a // 50)
a = (a - cnqt * 50) % 50
vnt = int(a // 20)
a = (a - vnt * 20) % 20
dez = int(a // 10)
a = (a - dez * 10) % 10
cinco = int(a // 5)
a = (a - cinco * 5) % 5
dois = int(a // 2)
a = (a - dois * 2) % 2
um = int(a // 1) 
a = (a - um * 1) % 1
cnqc = int(a // 0.5)
a = (a - cnqc * 0.5) % 0.5
vntcnc = int(a // 0.25)
a = (a - vntcnc * 0.25) % 0.25
dzc = int(a // 0.1)
a = (a - dzc * 0.1) % 0.1
cncc = int(a // 0.05)
umc = int((a - cncc * 0.05) // 0.01)
print(f"NOTAS:")
print(f"{cem} nota(s) de R$ 100.00")
print(f"{cnqt} nota(s) de R$ 50.00")
print(f"{vnt} nota(s) de R$ 20.00")
print(f"{dez} nota(s) de R$ 10.00")
print(f"{cinco} nota(s) de R$ 5.00")
print(f"{dois} nota(s) de R$ 2.00")
print(f"MOEDAS:")
print(f"{um} moeda(s) de R$ 1.00")
print(f"{cnqc} moeda(s) de R$ 0.50")
print(f"{vntcnc} moeda(s) de R$ 0.25")
print(f"{dzc} moeda(s) de R$ 0.10")
print(f"{cncc} moeda(s) de R$ 0.05")
print(f"{umc} moeda(s) de R$ 0.01")