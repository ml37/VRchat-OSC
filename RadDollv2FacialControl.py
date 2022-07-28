import argparse
import random
import time
import os
import sys
from pythonosc import udp_client
from tkinter import *
from PIL import Image, ImageTk
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5 import uic

form_class = uic.loadUiType("FacialControl.ui")[0]

parser = argparse.ArgumentParser()
parser.add_argument("--ip", default="127.0.0.1",
help="The ip of the OSC server")
parser.add_argument("--port", type=int, default=9000,
help="The port the OSC server is listening on")
args = parser.parse_args()
client = udp_client.SimpleUDPClient(args.ip, args.port)

class WindowClass(QMainWindow, form_class) :
    def __init__(self) :
        super().__init__()
        self.setupUi(self)
        self.BtnR0.clicked.connect(self.R0) #R0 to R12 and L0 to L12 total 26 buttons
        self.BtnR1.clicked.connect(self.R1)
        self.BtnR2.clicked.connect(self.R2)
        self.BtnR3.clicked.connect(self.R3)
        self.BtnR4.clicked.connect(self.R4)
        self.BtnR5.clicked.connect(self.R5)
        self.BtnR6.clicked.connect(self.R6)
        self.BtnR7.clicked.connect(self.R7)
        self.BtnR8.clicked.connect(self.R8)
        self.BtnR9.clicked.connect(self.R9)
        self.BtnR10.clicked.connect(self.R10)
        self.BtnR11.clicked.connect(self.R11)
        self.BtnR12.clicked.connect(self.R12)
        self.BtnL0.clicked.connect(self.L0)
        self.BtnL1.clicked.connect(self.L1)
        self.BtnL2.clicked.connect(self.L2)
        self.BtnL3.clicked.connect(self.L3)
        self.BtnL4.clicked.connect(self.L4)
        self.BtnL5.clicked.connect(self.L5)
        self.BtnL6.clicked.connect(self.L6)
        self.BtnL7.clicked.connect(self.L7)
        self.BtnL8.clicked.connect(self.L8)
        self.BtnL9.clicked.connect(self.L9)
        self.BtnL10.clicked.connect(self.L10)
        self.BtnL11.clicked.connect(self.L11)
        self.BtnL12.clicked.connect(self.L12)
        
    def R0(self):
        client.send_message("/avatar/parameters/FacialR", 0)
    def R1(self):
        client.send_message("/avatar/parameters/FacialR", 1)
    def R2(self):
        client.send_message("/avatar/parameters/FacialR", 2)
    def R3(self):
        client.send_message("/avatar/parameters/FacialR", 3)
    def R4(self):
        client.send_message("/avatar/parameters/FacialR", 4)
    def R5(self):
        client.send_message("/avatar/parameters/FacialR", 5)
    def R6(self):
        client.send_message("/avatar/parameters/FacialR", 6)
    def R7(self):
        client.send_message("/avatar/parameters/FacialR", 7)
    def R8(self):
        client.send_message("/avatar/parameters/FacialR", 8)
    def R9(self):
        client.send_message("/avatar/parameters/FacialR", 9)
    def R10(self):
        client.send_message("/avatar/parameters/FacialR", 10)
    def R11(self):
        client.send_message("/avatar/parameters/FacialR", 11)
    def R12(self):
        client.send_message("/avatar/parameters/FacialR", 12)
    def L0(self):
        client.send_message("/avatar/parameters/FacialL", 0)
    def L1(self):
        client.send_message("/avatar/parameters/FacialL", 1)
    def L2(self):
        client.send_message("/avatar/parameters/FacialL", 2)
    def L3(self):
        client.send_message("/avatar/parameters/FacialL", 3)
    def L4(self):
        client.send_message("/avatar/parameters/FacialL", 4)
    def L5(self):
        client.send_message("/avatar/parameters/FacialL", 5)
    def L6(self):
        client.send_message("/avatar/parameters/FacialL", 6)
    def L7(self):
        client.send_message("/avatar/parameters/FacialL", 7)
    def L8(self):
        client.send_message("/avatar/parameters/FacialL", 8)
    def L9(self):
        client.send_message("/avatar/parameters/FacialL", 9)
    def L10(self):
        client.send_message("/avatar/parameters/FacialL", 10)
    def L11(self):
        client.send_message("/avatar/parameters/FacialL", 11)
    def L12(self):
        client.send_message("/avatar/parameters/FacialL", 12)



if __name__ == "__main__" :
    #QApplication : 프로그램을 실행시켜주는 클래스
    app = QApplication(sys.argv) 

    #WindowClass의 인스턴스 생성
    myWindow = WindowClass() 

    #프로그램 화면을 보여주는 코드
    myWindow.show()

    #프로그램을 이벤트루프로 진입시키는(프로그램을 작동시키는) 코드
    app.exec_()