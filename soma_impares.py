print("Digite dois numeros: ")
x = int(input())
y = int(input())

if y < x :
    troca = x
    x = y
    y = troca

soma = 0
for i in range (x + 1, y) :
    if i % 2 != 0:
        soma = soma + i

print(F"SOMA DOS IMPARES = {soma}")