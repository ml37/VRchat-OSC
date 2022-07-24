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

form_class = uic.loadUiType("TTT.ui")[0]

class WindowClass(QMainWindow, form_class) :
    def __init__(self) :
        super().__init__()
        self.setupUi(self)
    
        self.btn.clicked.connect(self.imageload)
        '''self.btn_ok.clicked.connect(self.ok)
        self.btn_download.clicked.connect(self.download)
        self.btn_download_all.clicked.connect(self.download_all)'''

    def imageload(self):
        self.qPixmapFileVar = QPixmap()
        self.qPixmapFileVar.load("ABC.png")
        #self.qPixmapFileVar = self.qPixmapFileVar.scaledToWidth(600)
        self.image.setPixmap(self.qPixmapFileVar)


if __name__ == "__main__":
  parser = argparse.ArgumentParser()
  parser.add_argument("--ip", default="127.0.0.1",
      help="The ip of the OSC server")
  parser.add_argument("--port", type=int, default=9000,
      help="The port the OSC server is listening on")
  args = parser.parse_args()
  app = QApplication(sys.argv) 
  myWindow = WindowClass() 
  myWindow.show()
  app.exec_()

  client = udp_client.SimpleUDPClient(args.ip, args.port)


'''int askinputvalue 0~32'''
'''while True:
    UserInput =  input("Please input the value of the parameter: ")
    UserInput = int(UserInput)
    client.send_message("/avatar/parameters/Textchat", UserInput)'''
