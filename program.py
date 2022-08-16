import socket
import time
import threading
from tkinter import *


root = Tk()
root.geometry("320x480")
root.config(bg="white")

def func():
    t = threading.Thread(target=recv)
    t.start()

def recv():
    listenSocket = socket.socket()
    port = 3050
    maxConnection = 99
    ip = socket.gethostname()
    print(ip)

    listenSocket.bind(("",port))
    listenSocket.listen(maxConnection)
    (clientsocket,address) = listenSocket.accept()

    while True:
        senderMessage = clientsocket.recv(1024).decode()
        if not senderMessage=="":
            time.sleep(5)
            lstBox.insert(0,"Client : "+senderMessage)

xt =0
def sendMsg():
    global xt
    if xt==0:
        s = socket.socket()
        hostname = ""
        port = 4050
        s.connect((hostname,port))
        msg = messageBox.get()
        lstBox .insert(0,"You : "+msg)
        s.send(msg.encode())
        xt=xt+1

    else:
        msg = messageBox.get()
        lstBox .insert(0,"You : "+msg)
        s.send(msg.encode())


def threadSendMsg():
    th = threading.Thread(target=sendMsg)
    th.start()

# GUI

startChartImg =PhotoImage(file="static/start2.PNG") 
buttons = Button(root,image=startChartImg,command=func,borderwidth=0)
buttons.place(x=99,y=30)

message = StringVar()
messageBox = Entry(root,textvariable=message,font=("calibre",10,"normal"),border=2,width=32)
messageBox.place(x=15,y=425)

sendMessageImg = PhotoImage(file="static/send2.PNG")
sendMessageButton = Button(root,image=sendMessageImg,command=threadSendMsg,borderwidth=0) 
sendMessageButton.place(x=260,y=420)

lstBox = Listbox(root,height=20,width=47)
lstBox.place(x=15,y=80)


root.mainloop()