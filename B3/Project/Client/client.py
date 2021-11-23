import random
import time
import subprocess
#Client Script:il codice seguente emula l'esperienza dell'utente nell'interagire con le funzioni serverless.
#Suddivisa in 2 funzioni le quali si occupano della gestione della richiesta di calcolo prelevando l'input dall'utente
#e la comunicazione con i nodi edge.

def controllo():
    while(1):                       #La funzione controllo deve essere sempre in ascolto, per permettere ogni volta che l'utente richiede
        i = random.randint(3, 4)    #una delle due funzioni serverless
        time.sleep(1)
        fl = open("log.txt", 'r+')  #creo due file per salvare le info sul sottoprocesso che chiamerò per la comunicazione con gli altri nodi
        fo = open("output.txt", 'r+')#e per salvare il risultato dell'ultima richiesta.
        content = fo.read()
        log = fl.read()
        print("\nSCEGLIERE L'OPERAZIONE DA SVOLGERE: DIGITARE TRA PI, PRIMO O READ")
        operation = input()
        if(operation == "read" or operation =="READ"):  #oltre che richiedere una delle due funzioni serverless, ho creato una funzione per leggere il contenuto dei file senza dover uscire dallo script
            if(content == ''):
                print("Il contenuto del file è vuoto")
            print(content)
            print(log)
            fl.close()
            fo.close()
            controllo()
        print("\nINSERIRE IL VALORE INTERO DA ANALIZZARE")
        value = input()
        func(operation,value,i) #dopo aver preso i diversi input, chiamo la funzione che chiamerà i diversi nodi, che simulo solamente 2 che vengono chiamati in modo random, poichè ipotizzo che dipenda dalla loro locazione geografica e quindi tendenzialmente dovrei scegliere sempre quello piu vicino per avere una comunicazione più veloce
        if(operation!='primo' and operation!='pi' and operation!= 'PRIMO' and operation!= 'PI'):
            print("\nValore errati, riprovare!")

def func(operazione,value,i):
            link=' "http://172.17.0.{numero}:8080/2015-03-31/functions/function/invocations"'.format(numero=i)
            apice = "'"
            graffe = '{'+'"operation":"{operazione}"'.format(operazione=operazione)+',"value":{value}'.format(value=value)+'}'
            cmd = "curl -XPOST" +link+" -d "+apice+graffe+apice
            fl = open("log.txt",'w+')
            fo = open("output.txt",'w+') #creo il comando della chiamata dei nodi edge e invoco una delle due funzionalità
            proc = subprocess.Popen(cmd,shell=True,stderr = fl,stdout=fo)
            time.sleep(1)
            fl.close()
            fo.close()
            return proc


if __name__=="__main__":
    controllo()