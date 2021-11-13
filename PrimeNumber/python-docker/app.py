import mpmath
def handler(event, context):
    if (event['operation'] == "pi"):
        x = int(event['value'])
        mpmath.mp.dps = x
        print("Il numero pi-greco con le", x, "cifre decimali", mpmath.pi)
        return "Il valore e' " + str(mpmath.pi)
    if event['operation'] == "primo":
        x = int(event['value'])
        print("Sto eseguendo")
        print(x)
        n, c, counter = 1, 0, 0
        primi = list(range(0))

        while c < x:
            n += 1
            for i in range(2, n + 1):
                if (n % i) == 0:
                    break
            if i == n:
                primi.append(n)
                c = c + 1
        print(primi)
        print("Il ", x, " valore e': ", n)
        return "Il" + str(x) + "valore e': " + str(n) + " La lista dei numeri primi precedenti e': " + str(primi)




