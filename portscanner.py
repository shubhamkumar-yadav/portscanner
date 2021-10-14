import socket
target = input("Enter the ip address  you want to scan :")
portrange = input("Enter the range you want to scan (ex:5-200) :")
lowport = int(portrange.split('-')[0])
highport = int(portrange.split('-')[1])
print('scanning port',target,'from',lowport,'to',highport)
for port in range(lowport,highport):
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    status = s.connect_ex((target,port))
    if (status==0):
        print('port',port,'open....')
    else:
        print('port',port,'closed.....')
s.close()        