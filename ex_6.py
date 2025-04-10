entre_10_20 = 0
fora = 0
for x in range(10):
    n = int(input("me diga um numero: "))
    if 10 >= n <= 20:
        entre_10_20 += 1
    else:
        fora += 1
print(f"Foram {entre_10_20} Digitados entre 20 e 10")
print(f"Foram {fora} Digitados fora da sequencia de 20 e 10")