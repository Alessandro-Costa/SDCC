Per l'esecuzione corretta dell'applicazione sarà necessario avere installato docker, con tutte le sue funzionalità, per poter creare l'immagine e il container dove si sviluppa l'ambiente esecutivo.
In caso non si possieda, si può consultare la guida online rilasciata ufficialmente dagli sviluppatori di Docker. https://docs.docker.com/engine/install/ubuntu/ o consentire al file docker.sh di installarlo.
Ora si può avviare il file docker.sh da terminale con il comando:
$  ./docker.sh
All'interno di questo script, ci sono vari funzioni da terminale che consentono la creazione dell'immagine del client e del nodo edge e dell'avvio come amministratore dei nodi edge.
WARNING: è necessario possedere le credenziali corrette per poter accedere come root aws per consentire la comunicazione con il cloud aws esterno.
Per questo la prima esecuzione sara solo offline, una volta acquisite le credenzali è possibile scommentiare delle parti di codice del file docker.sh per avviare l'applicazione online.
In ultimo è stato anche inserito il comando per controllare lo stato della CPU e della Memoria di ogni singolo container.
All'interno della cartella "Project" sono racchiusi altre cartelle come Edge, Client e aws con i loro file .py e i dockerfile.

Una volta fatto partire il file "docker.sh", si apriranno diversi terminali.
Il terminale denominato come Client è dove l'utente può interagire con l'ambiente. Sarà necessario far partire il programma di esecuzione chiamato "client.py".
Il comando per farlo è il seguente:
$ python3 client.py

Una volta avviato ci verranno chiesti diversi input, ai quali possiamo rispondere e verificare se la domanda venga inoltrata o ai nodi edge o al servizio AWS lambda.

