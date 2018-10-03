# Echo client program
import socket
import hashlib
import time

HOST = '127.0.0.1'    # The remote host
PORT = 50007          # The same port as used by the server

totalm = -1

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
print "type username:"
# prompt username
username = raw_input()
print username + " has just joined the chat session"
print "type input:"
text = raw_input()
if "ping" in text:
    # start the timer
    startTime = time.time()
    print "Ping start time: "+str(startTime)

hash = hashlib.sha224(text).hexdigest()

# <cmd>message: hello there - sdfddfddsf3423423 </cmd>

output = username+'='+'<cmd>message:'+text+'-'+hash+'</cmd>' #holder for command

# when we send data to the server, we are using a colon
# at the end of a sentence to mark the end of the current sentence
# later when the input comes back, we will then be breaking the input
# into individual parts using the semicolon ; to separate the lines
if "ping" in text:
    output = "<cmd>ping</cmd>"
if "time" in text: 
    output = "<cmd>time</cmd>"
    
s.sendall(output + ";")

data = s.recv(80000)

# breaking apart the data we get back.
response = data.split(';')

for x in response:
    print str(x)
    totalm = totalm + 1 
    
if "total" in text:
    print "total messages are "+ str(totalm)
if "pong" in response:
    stopTime = time.time()
    print "Stopped Time: " + str(stopTime)
    totalTime = stopTime - startTime
    print "Total Time: "+str(totalTime)
if "time" in response:
    currentTime = time.strftime("%x %X", time.gmtime())
    print "current time: " + str(currentTime)

    
s.close()
