import boto3
import mpmath
import psutil
import logging
import threading
import time

logging.basicConfig(level=logging.DEBUG,
                    format='(%(threadName)-9s) %(message)s',)

def n():
    logging.debug('Starting')
    logging.debug('Exiting')

def d():
    logging.debug('Starting')
    global token
    while (1):
        cpu_value = 0.0
        while (cpu_value < 70.0):
            token = 0;
            print(token)
            cpu_value = psutil.cpu_percent(1)
            print(cpu_value)
            time.sleep(3)
        token = 1;
        print(token)
        cpu_value = psutil.cpu_percent(1)
        time.sleep(3)
    logging.debug('Exiting')

if __name__ == '__main__':

	t = threading.Thread(name='non-daemon', target=n)

	d = threading.Thread(name='daemon', target=d)
	d.setDaemon(True)

	d.start()
	t.start()

	d.join()
	t.join()



def thread_cpu_guard(name):
    global token
    while(1):
        cpu_value = 0.0
        while(cpu_value < 70.0):
            token = 0;
            print(token)
            cpu_value = psutil.cpu_percent(1)
            print(cpu_value)
        token = 1;
        print(token)
        cpu_value = psutil.cpu_percent(1)




def thread_worker(name, event, context):
    logging.info("Thread %s: starting", name)
    if (event['operation'] == "pi"):
        x = int(event['value'])
        if(token == 0):
            mpmath.mp.dps = x
            print("Il numero pi-greco con le", x, "cifre decimali", mpmath.pi)
            return "Il valore e' " + str(mpmath.pi)
        else:
            lambda_client = boto3.client('lambda', region_name='us-east-1')
            lambda_payload = '{"operation": "pi",' + '"value": {valore}'.format(valore=x) + '}'
            response = lambda_client.invoke(
                FunctionName='arn:aws:lambda:us-east-1:752739800150:function:cpu_intensive_lambda',
                InvocationType='RequestResponse', LogType='Tail', Payload=lambda_payload)
            return response['Payload'].read()
    if event['operation'] == "primo":
        x = int(event['value'])
        if (token == 0):
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
        else:
            lambda_client = boto3.client('lambda', region_name='us-east-1')
            lambda_payload = '{"operation": "primo",' + '"value": {valore}'.format(valore=x) + '}'
            response = lambda_client.invoke(
                FunctionName='arn:aws:lambda:us-east-1:752739800150:function:cpu_intensive_lambda',
                InvocationType='RequestResponse', LogType='Tail', Payload=lambda_payload)
            return response['Payload'].read()
    logging.info("Thread %s: finishing", name)



