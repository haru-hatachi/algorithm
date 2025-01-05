import sys

def primeFactorization(argv):
    kazu = int(argv[1])
    sosu = [2]
    soinsu = []
    ban = 0
    sosukamo = 3
    while kazu > 1:
        while kazu % sosu[ban] == 0:
            kazu = kazu / sosu[ban]
            soinsu.append(sosu[ban])
            print(sosu[ban])
        memo = len(sosu)
        while len(sosu) == memo:
            ban = 0
            kensa = 0
            for i in range(len(sosu)):
                if sosukamo % sosu[ban] == 0:
                    break
                else:
                    kensa = kensa + 1
                ban = ban + 1
            if kensa == len(sosu):
                sosu.append(sosukamo)
            sosukamo = sosukamo + 1
    return soinsu

primeFactorization(sys.argv)
