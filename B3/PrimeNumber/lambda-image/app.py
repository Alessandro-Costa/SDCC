import boto3
import mpmath
import psutil
token = 0
def handler(event, context):
    if (event['operation'] == "pi"):
        token = 1
        x = int(event['value'])
        mpmath.mp.dps = x
        cpu_usage = psutil.cpu_percent()
        if(cpu_usage <80.0):
            print("Il numero pi-greco con le", x, "cifre decimali", mpmath.pi)
            token = 0
            return "Il valore e' " + str(mpmath.pi)
        else:
            print("MANDO LA RICHIESTA A LAMBDA")
            lambda_client = boto3.client('lambda', region_name='us-east-1')
            lambda_payload = '{"operation": "pi",' + '"value": {valore}'.format(valore=x) + '}'
            response = lambda_client.invoke(
                FunctionName='arn:aws:lambda:us-east-1:752739800150:function:cpu_intensive_lambda',
                InvocationType='RequestResponse', LogType='Tail', Payload=lambda_payload)
            token = 0
            return response['Payload'].read()
    if event['operation'] == "primo":
        token = 1
        x = int(event['value'])
        print("Sto eseguendo")
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
                token = 0
                return response['Payload'].read()
        print(primi)
        print("Il ", x, " valore e': ", n)
        token = 0
        return "Il" + str(x) + "valore e': " + str(n) + " La lista dei numeri primi precedenti e': " + str(primi)




