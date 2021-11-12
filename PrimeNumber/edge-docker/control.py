import subprocess
import threading
import time

exitFlag = 0

class myThread (threading.Thread):
   def __init__(self, threadID, name, counter):
      threading.Thread.__init__(self)
      self.threadID = threadID
      self.name = name
      self.counter = counter
   def run(self):
      print ("Starting " + self.name)
      if(self.name == "Thread-1"):
         read()
      if(self.name == "Thread-2"):
         info()
      else:
         print("Error")
      print ("Exiting " + self.name)
def info():
   with open('out.txt', 'w+') as fout:
      subprocess.run(["docker", "stats", "--format", "'{{.CPUPerc}}'", "--no-stream"], stdout=fout)
def read():
   print("LESO")
   fout = open("out.txt", "r")
   line = fout.readline()
   print(line)
def print_time(threadName, counter, delay):
   while counter:
      if exitFlag:
         threadName.exit()
      time.sleep(delay)
      print ("%s: %s" % (threadName, time.ctime(time.time())))
      counter -= 1

# Create new threads
thread1 = myThread(1, "Thread-1", 1)
thread2 = myThread(2, "Thread-2", 2)

# Start new Threads
thread1.start()
thread2.start()

print ("Exiting Main Thread")