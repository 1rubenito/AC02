primos = [2]
print(2, end=' ')
i = 3
while len(primos) < 100:
    for p in primos:
        if (i % p == 0) or (p*p > i):
            break
    if i % p != 0:
        primos.append(i)
        print(i,  end=' ')
    i += 1
print('<---- 100˚ Número Primo!')


