import os
import sys
import time
import subprocess

import boto3
def controllo():
    while(1):
        print("\n&&&&&&&&&& -PI- $$$$$$$$$$$$ -PRIMO-")
        operation = input()
        print("\n$$$$$$$$$ VALORE INTERO &&&&&&&&&&")
        value = input()
        func(operation,value)
        if(operation!='primo' and operation!='pi'):
            print("\nValore errati, riprovare!")

def func(operazione,value):
    print("Lavoro sul locale")
    link=' "http://localhost:9001/2015-03-31/functions/function/invocations"'
    apice = "'"
    graffe = '{'+'"operation":"{operazione}"'.format(operazione=operazione)+',"value":{value}'.format(value=value)+'}'
    cmd = "curl -XPOST" +link+" -d "+apice+graffe+apice
    proc = subprocess.Popen(cmd,shell=True)
    return proc

if __name__=="__main__":
    #rc = subprocess.call("./docker.sh")
    controllo()