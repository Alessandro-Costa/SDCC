import os
import sys
import time
import subprocess

import boto3
def controllo():
    while(1):
        time.sleep(1)
        print("\n&&&&&&&&&& -PI- $$$$$$$$$$$$ -PRIMO- $$$$$$$$$$$ -READ-")
        operation = input()
        if(operation == "read" or operation =="READ"):
            fl = open("log.txt", 'r+')
            fo = open("output.txt", 'r+')
            content = fo.read()
            if(content == ''):
                print("Il contenuto del file è vuoto")
            print(content)
            fl.close()
            fo.close()
            controllo()
        print("\n$$$$$$$$$ VALORE INTERO &&&&&&&&&&")
        value = input()
        func(operation,value)
        if(operation!='primo' and operation!='pi' and operation!= 'PRIMO' and operation!= 'PI'):
            print("\nValore errati, riprovare!")

def func(operazione,value):
    link=' "http://172.17.0.3:8080/2015-03-31/functions/function/invocations"'
    apice = "'"
    graffe = '{'+'"operation":"{operazione}"'.format(operazione=operazione)+',"value":{value}'.format(value=value)+'}'
    cmd = "curl -XPOST" +link+" -d "+apice+graffe+apice
    fl = open("log.txt",'w+')
    fo = open("output.txt",'w+')
    proc = subprocess.Popen(cmd,shell=True,stderr = fl,stdout=fo)
    fl.close()
    fo.close()
    return proc

if __name__=="__main__":
    controllo()