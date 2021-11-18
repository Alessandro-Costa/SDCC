import random
import time
import subprocess


def controllo():
    while(1):
        i = random.randint(3, 4)
        time.sleep(1)
        fl = open("log.txt", 'r+')
        fo = open("output.txt", 'r+')
        content = fo.read()
        log = fl.read()
        print("\n&&&&&&&&&& -PI- $$$$$$$$$$$$ -PRIMO- $$$$$$$$$$$ -READ-")
        operation = input()
        if(operation == "read" or operation =="READ"):
            if(content == ''):
                print("Il contenuto del file è vuoto")
            print(content)
            print(log)
            fl.close()
            fo.close()
            controllo()
        print("\n$$$$$$$$$ VALORE INTERO &&&&&&&&&&")
        value = input()
        func(operation,value,i)
        if(operation!='primo' and operation!='pi' and operation!= 'PRIMO' and operation!= 'PI'):
            print("\nValore errati, riprovare!")

def func(operazione,value,i):
            link=' "http://172.17.0.{numero}:8080/2015-03-31/functions/function/invocations"'.format(numero=i)
            apice = "'"
            graffe = '{'+'"operation":"{operazione}"'.format(operazione=operazione)+',"value":{value}'.format(value=value)+'}'
            cmd = "curl -XPOST" +link+" -d "+apice+graffe+apice
            fl = open("log.txt",'w+')
            fo = open("output.txt",'w+')
            proc = subprocess.Popen(cmd,shell=True,stderr = fl,stdout=fo)
            time.sleep(1)
            fl.close()
            fo.close()
            return proc


if __name__=="__main__":
    controllo()