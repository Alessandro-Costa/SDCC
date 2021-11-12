import subprocess
import mpmath
import boto3
#from flask import Flask

#app = Flask(__name__)

#@app.route("/")
#def index():
   # return "Congratulations, it's a web app!"

#@app.route("/pi/<valore>")
#def pi(valore):
    #x = int(valore)
    #if (x< 100000):
     #   mpmath.mp.dps = x
      #  print("Il numero pi-greco con le", x, "cifre decimali", mpmath.pi)
       # return "Il valore è\n" + str(mpmath.pi)
    #else:
       # return "Sgrodolo"
#@app.route("/primo/<valore>")
#def primo(valore):
 #   x = int(valore)
  #  print("Sto eseguendo")
   # print(x)
    #n, c, counter = 1, 0, 0
    #primi = list(range(0))

    #while c < x:
    #    n += 1
    #    for i in range(2, n + 1):
    #        if (n % i) == 0:
    #            break
    #    if i == n:
    #        primi.append(n)
    #        c = c + 1
    #print(primi)
    #print("Il", x, "valore è:", n)
    #return "Il\t"+str(x)+"\tvalore è:\t"+str(n)+"\nLa lista dei numeri primi precedenti è:"+str(primi)
import threading
import psutil
def handler(event, context):
    if (event['operation'] == "pi"):
        x = int(event['value'])
        fp = open("out.txt","r")
        subprocess.run(["docker", "stats", "--format", "'{{.CPUPerc}}'", "--no-stream"], stdout=fp)
        line = int(fp.readline())
        while(line < 70):
       #if (x < 100000):
            mpmath.mp.dps = x
            print("Il numero pi-greco con le", x, "cifre decimali", mpmath.pi)
            return "Il valore e' " + str(mpmath.pi)
        #else:
        lambda_client = boto3.client('lambda', region_name='us-east-1')
        lambda_payload = '{"operation": "pi","value": 100000}'
        response =lambda_client.invoke(FunctionName='arn:aws:lambda:us-east-1:752739800150:function:cpu_intensive_lambda', InvocationType ='RequestResponse', LogType='Tail', Payload=lambda_payload)
        return response['Payload'].read()
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

#if __name__ == "__main__":
 #   app.run(host="127.0.0.1", port=9000, debug=True)





