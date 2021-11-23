import boto3
import psutil
import math
#Script dei nodi edge: la loro funzionalità è quella di ricevere la richiesta dal client e
# decidere se passare l'operazione al servizio AWS o di calcolarlo in locale.

def a(n):
    return 1 / n ** 2

def handler(event, context):
    if (event['operation'] == "pi"): #in base agli input presi si calcola o la precisione del pi-greco o l'ennesimo numero primo
        PASSI = int(event['value'])
        Sn = 0
        cpu_usage = psutil.cpu_percent()

        for n in range(1, PASSI +1):
            an = a(n)
            Sn += an
            pin = math.sqrt(6 * Sn)
        print("Il numero pi-greco con", str(PASSI), "grado di accuratezza", str(pin))    #per decidere dove calcolare l'operazione controllo il valore della CPU del sistema, e se satura il sistema rindirizzo la richiesta a AWS lambda.

        return "Il valore e' " + str(pin)

    if event['operation'] == "primo":
        x = int(event['value'])
        print("Sto eseguendo")                     #qui viene replicato lo schema precedente ma per la seconda funzione CPU intensive.
        print(x)
        n, c, counter = 1, 0, 0
        primi = list(range(0))
        while c < x:
            n += 1
            cpu_usage = psutil.cpu_percent()    
            for i in range(2, n + 1):
                    if (n % i) == 0:
                        break
            if i == n:
                    primi.append(n)
                    c = c + 1          
        print(primi)
        print("Il ", x, " valore e': ", n)
        return "Il" + str(x) + "valore e': " + str(n) + " La lista dei numeri primi precedenti e': " + str(primi)




