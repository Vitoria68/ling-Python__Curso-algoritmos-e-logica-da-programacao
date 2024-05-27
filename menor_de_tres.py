um = int(input("Primeiro valor: "))
dois = int(input("Segundo valor: "))
tres = int(input("Terceiro valor: "))

if um < dois and um < tres:
    menor = um
elif dois < um and dois < tres:
    menor = dois
else:
    menor = tres

print("MENOR = %d" %(menor))