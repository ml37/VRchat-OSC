import argparse
import random
import time
import os
import sys
from pythonosc import udp_client
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5 import uic

form_class = uic.loadUiType("TextChat.ui")[0]
'''char dic is used to convert the number to the corresponding character a:1, b:2 ... A:27, B:28'''
char_dic = {'a':1,'b':2,'c':3,'d':4,'e':5,'f':6,'g':7,'h':8,'i':9,'j':10,'k':11,'l':12,'m':13,'n':14,'o':15,'p':16,'q':17,'r':18,'s':19,'t':20,'u':21,'v':22,'w':23,'x':24,'y':25,'z':26,'A':27,'B':28,'C':29,'D':30,'E':31,'F':32,'G':33,'H':34,'I':35,'J':36,'K':37,'L':38,'M':39,'N':40,'O':41,'P':42,'Q':43,'R':44,'S':45,'T':46,'U':47,'V':48,'W':49,'X':50,'Y':51,'Z':52}
reverse_char_dic = {v: k for k, v in char_dic.items()}
print(reverse_char_dic)
class WindowClass(QMainWindow, form_class) :

    parser = argparse.ArgumentParser()
    parser.add_argument("--ip", default="127.0.0.1",
    help="The ip of the OSC server")
    parser.add_argument("--port", type=int, default=9000,
    help="The port the OSC server is listening on")
    args = parser.parse_args()
    def __init__(self) :
        super().__init__()
        self.setupUi(self)
        self.text_send.returnPressed.connect(self.send)
    def send(self):
        print(self.text_send.text())
        mes = self.text_send.text()
        for i in range(len(mes)):
            print(f'Line : {i} is {mes[i]} /send {char_dic[mes[i]]}')
            client.send_message("/avatar/parameters/" + str(i+1), char_dic[mes[i]])


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--ip", default="127.0.0.1",
    help="The ip of the OSC server")
    parser.add_argument("--port", type=int, default=9000,
    help="The port the OSC server is listening on")
    args = parser.parse_args()  
    app = QApplication(sys.argv)
    client = udp_client.SimpleUDPClient(args.ip, args.port)
    myWindow = WindowClass()
    myWindow.show()
    app.exec_()
