import csv
import socket
from _thread import *
import array as arr
import csv
import numpy as np
fields=['id','name','age','salary','exp']
import pandas as pd

serverSocket = socket.socket()
lst=[]
lst1=[]
lst2=[]
host = '127.0.0.1'
port = 9999
threadcount = 0
try:
    serverSocket.bind((host, port))
except socket.error as e:
    print("warnings")
print("waiting for connection")
serverSocket.listen(10)

def client_thread(connection):
    loop=connection.recv(2048)
    loop1=loop.decode("utf-8")
    if loop1== '1':
        i=-1
        j=1
        while True:
            data=connection.recv(2048)
            data1=data.decode("utf-8")
            lst.append(data1)
            i=i+1
            if i==4:
                i=-1
                #with open("C:\\Users\\Administrator\\Desktop\\LMS\\leave.csv", 'w') as csvfile:
                file = open('C:\\Users\\Administrator\\Desktop\\LMS\\leave.csv', 'a+', newline='')
                with file:
                    write = csv.writer(file)
                    write.writerows([lst],)
                    lst.clear()
                    reply="Successfully added ....!!!"
                    connection.send(str.encode(reply))
            if not data:
                break
        connection.close()
    elif loop1=='2':
        while True:
            emp=connection.recv(2048)
            empId= emp.decode("utf-8")
            csv_file=csv.reader(open("C:\\Users\\Administrator\\Desktop\\LMS\\leave.csv","r"))
            for row in csv_file:
                if empId==row[0]:
                    found=row
            def listToString(s):
                str1 = ""
                for ele in s:
                    str1 += ele + " "
                return str1
            gotIt=listToString(found)
            msg="\t\tFound it :)"
            connection.sendall(str.encode(gotIt))
        connection.close()
    elif loop1 == '3':
        j=-1
        while True:
            Lemp = connection.recv(2048)
            LempId = Lemp.decode("utf-8")
            lst1.append(LempId)
            j=j+1
            csv_file = csv.reader(open("C:\\Users\\Administrator\\Desktop\\LMS\\leave.csv"))
            for row in csv_file:
                if LempId == row[0]:
                    found = row
                    rep="\t\tfound :)"
                    connection.sendall(str.encode(rep))
                if j == 2:
                    j = -1
                    file = open('C:\\Users\\Administrator\\Desktop\\LMS\\apLeave.csv', 'a+', newline='')
                    with file:
                        write = csv.writer(file)
                        write.writerows([lst1],)
                        lst1.clear()
                        crt=1
            ac="done"
            connection.sendall(str.encode(ac))
            if not Lemp:
                break
        connection.close()
    elif loop1 == '4':
        lines = list()
        delem = connection.recv(2048)
        delemId =delem.decode("utf-8")
        with open('C:\\Users\\Administrator\\Desktop\\LMS\\apLeave.csv', 'r') as readFile:
                reader = csv.reader(readFile)
                for row in reader:
                    lines.append(row)
                for field in row:
                    if field == delemId:
                        lines.remove(row)
        with open('C:\\Users\\Administrator\\Desktop\\LMS\\apLeave.csv', 'w') as writeFile:
            writer = csv.writer(writeFile)
            writer.writerows(lines)
        ac = "done"
        connection.sendall(str.encode(ac))
    elif loop1 == '5':
            with open('C:\\Users\\Administrator\\Desktop\\LMS\\leave.csv', 'r') as file:
                reader = csv.reader(file)
                for row in reader:
                    lst2.append(row)
            connection.sendall(str.encode(lst2))

while True:
    client, address = serverSocket.accept()
    print("connected to " + address[0] + " " + str(address[1]))
    start_new_thread(client_thread,(client,))
    threadcount += 1
    print("threadcounter" + str(threadcount))
serverSocket.close()