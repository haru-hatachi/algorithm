lista = [1,8,5,7,2,9,3,6,4]
for i in range(10):
    ban = 0
    for i in range(8):
        if lista[ban] > lista[ban + 1]:
            memo = lista[ban + 1]
            lista[ban + 1] = lista[ban]
            lista[ban] = memo
        ban = ban + 1
    print(lista)