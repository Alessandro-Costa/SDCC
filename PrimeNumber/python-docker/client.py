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
    try:
        outs, errs = proc.communicate(timeout=5)
        return proc
    except subprocess.TimeoutExpired:
        stop = 'docker stop $(docker ps --format "{{.ID}}")'
        subprocess.Popen(stop,shell=True)
        outs, errs = proc.communicate()
        print("Carico di lavoro eccessivo, gestisco tramite Lambda!")
        lambda_client = boto3.client('lambda', region_name='us-east-1')
        lambda_payload = '{"operation": "pi",'+'"value": {valore}'.format(valore=value)+'}'
        response = lambda_client.invoke(
            FunctionName='arn:aws:lambda:us-east-1:752739800150:function:cpu_intensive_lambda',
            InvocationType='RequestResponse', LogType='Tail', Payload=lambda_payload)
        print(response['Payload'].read())
        run = "gnome-terminal -- docker run -p 9001:8080 cpu_intensive:1.0"
        subprocess.run(run,shell=True)
        return response['Payload'].read()


if __name__=="__main__":
    rc = subprocess.call("./docker.sh")
    controllo()