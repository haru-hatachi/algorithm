lista = [4,8,5,7,2,9,3,6,1]
rupukaisu = len(lista) - 1
for i in range(rupukaisu):
    ban = 0
    print(lista)
    for j in range(rupukaisu - i):
        if lista[ban] > lista[ban + 1]:
            memo = lista[ban + 1]
            lista[ban + 1] = lista[ban]
            lista[ban] = memo
        ban = ban + 1
print(lista)