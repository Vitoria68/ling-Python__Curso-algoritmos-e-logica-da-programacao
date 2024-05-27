ordem = int(input("Qual a ordem da matriz? "))

mat = [[0 for x in range (ordem)] for x in range (ordem)]

for i in range (0 , ordem):
    for j in range (0 , ordem):
        mat[i][j] = int(input(f"Elementos [{i},{j}]: "))
print()

print("DIAGONAL PRINCIPAL:")
for i in range (0, ordem):
    print(f"{mat[i][i]} ", end = " ")
print()

negativos = 0
for i in range (0, ordem):
    for j in range (0, ordem):
        if mat[i][j] < 0:
            negativos = negativos + 1

print(f"QUANTIDADE DE NEGATIVOS = {negativos}")
     