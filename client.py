import socket
def addUser(clientSocket):
    reg=str(1)
    clientSocket.send(str.encode(reg))
    rot=True
    while rot:
        id = str(input("\t\t\t\t\tEnter the ID : - "))
        clientSocket.send(str.encode(id))
        name = input("\t\t\t\t\tEnter the Name : -")
        clientSocket.send(str.encode(name))
        age = str(input("\t\t\t\t\tEnter the Age : - "))
        clientSocket.send(str.encode(age))
        salary = str(input("\t\t\t\t\tEnter the salary : -"))
        clientSocket.send(str.encode(salary))
        exp = str(input("\t\t\t\t\tEnter the Experience : - "))
        clientSocket.send(str.encode(exp))
        response = clientSocket.recv(1024)
        print(response.decode('utf-8'))
        rot=input("enter 0 for exit ir enter 1 for add other user: - ")
def SearchEmp(clientSocket):
    reg = str(2)
    clientSocket.send(str.encode(reg))
    Emid = str(input("\t\t\t\t\tEnter the Employee ID : - "))
    clientSocket.send(str.encode(Emid))
    response = clientSocket.recv(1024)
    print(response.decode('utf-8'))
    response = clientSocket.recv(1024)
    print(response.decode('utf-8'))
def appLeave(clientSocket):
    reg = str(3)
    clientSocket.send(str.encode(reg))
    Emid = str(input("\t\t\t\t\tEnter the Employee ID : - "))
    clientSocket.send(str.encode(Emid))
    response = clientSocket.recv(1024)
    print(response.decode('utf-8'))
    Sdate = str(input("\t\t\t\t\tEnter the Start Date : - "))
    clientSocket.send(str.encode(Sdate))
    Edate = str(input("\t\t\t\t\tEnter the end date : - "))
    clientSocket.send(str.encode(Edate))
    response = clientSocket.recv(1024)
    print(response.decode('utf-8'))
def DelEmp(clientSocket):
    reg = str(4)
    clientSocket.send(str.encode(reg))
    Delid = str(input("\t\t\t\t\tEnter the Employee ID to delete Leave: - "))
    clientSocket.send(str.encode(Delid))
    response = clientSocket.recv(1024)
    print(response.decode('utf-8'))
def Display(clientSocket):
    reg = str(5)
    clientSocket.send(str.encode(reg))
    while True:
        response = clientSocket.recv(1024)
        print(response.decode('utf-8'))

clientSocket=socket.socket()
host='127.0.0.1'
port=9999
print("waiting for connection")
try:
    clientSocket.connect((host,port))
except socket.error as e :
    print(str(e))
print("\t\t\t\t\t\t ----- Welcome to Employee Leave Management System ---------")
print("\t\t\t\t\t1. APPLY LEAVE\n")
print("\t\t\t\t\t2. DELETE LEAVE\n")
print("\t\t\t\t\t3. SEARCH EMPLOYEE\n")
print("\t\t\t\t\t4. DISPLAY ALL LEAVES\n")
print("\t\t\t\t\t5. ADD USER\n")
inp=input("please enter the input")
if inp == '1':
     appLeave(clientSocket)
elif inp == '2':
    DelEmp(clientSocket)
elif inp == '3':
    SearchEmp(clientSocket)
elif inp == '4':
    Display(clientSocket)
elif inp == '5':
    addUser(clientSocket)
