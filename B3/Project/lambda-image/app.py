import boto3
import mpmath
import psutil
#Script dei nodi edge: la loro funzionalità è quella di ricevere la richiesta dal client e
# decidere se passare l'operazione al servizio AWS o di calcolarlo in locale.
def handler(event, context):
    if (event['operation'] == "pi"): #in base agli input presi si calcola o la precisione del pi-greco o l'ennesimo numero primo
        x = int(event['value'])
        mpmath.mp.dps = x            #uso una libreria python per calcolare velocemente il pi-greco
        cpu_usage = psutil.cpu_percent()
        if cpu_usage < 80.0:          #per decidere dove calcolare l'operazione controllo il valore della CPU del sistema, e se satura il sistema rindirizzo la richiesta a AWS lambda.
            print("Il numero pi-greco con le", x, "cifre decimali", mpmath.pi)
            return "Il valore e' " + str(mpmath.pi)
        else:
            print("MANDO LA RICHIESTA A LAMBDA")   #uso la libreria boto3 per comunicare con il servizio lambda
            lambda_client = boto3.client('lambda', region_name='us-east-1')
            lambda_payload = '{"operation": "pi",' + '"value": {valore}'.format(valore=x) + '}'
            response = lambda_client.invoke(
                FunctionName='arn:aws:lambda:us-east-1:752739800150:function:cpu_intensive_lambda',
                InvocationType='RequestResponse', LogType='Tail', Payload=lambda_payload)
            return response['Payload'].read()
    if event['operation'] == "primo":
        x = int(event['value'])
        print("Sto eseguendo")                     #qui viene replicato lo schema precedente ma per la seconda funzione CPU intensive.
        print(x)
        n, c, counter = 1, 0, 0
        primi = list(range(0))

        while c < x:
            n += 1
            cpu_usage = psutil.cpu_percent()
            if(cpu_usage < 80.0):
                for i in range(2, n + 1):
                    if (n % i) == 0:
                        break
                if i == n:
                    primi.append(n)
                    c = c + 1
            else:
                print("MANDO LA RICHIESTA A LAMBDA")
                lambda_client = boto3.client('lambda', region_name='us-east-1')
                lambda_payload = '{"operation": "primo",' + '"value": {valore}'.format(valore=x) + '}'
                response = lambda_client.invoke(
                    FunctionName='arn:aws:lambda:us-east-1:752739800150:function:cpu_intensive_lambda',
                    InvocationType='RequestResponse', LogType='Tail', Payload=lambda_payload)
                return response['Payload'].read()
        print(primi)
        print("Il ", x, " valore e': ", n)
        return "Il" + str(x) + "valore e': " + str(n) + " La lista dei numeri primi precedenti e': " + str(primi)




