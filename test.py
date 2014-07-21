import os
a = os.popen('ipconfig/all')


print a.readlines()[1]
    
def getIp(domain):
    import socket
    myaddr = socket.getaddrinfo(domain,'http')[0][4][0]
    print(myaddr)

getIp('www.twitter.com')
