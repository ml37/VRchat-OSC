from PyQt5.QtWidgets import QPushButton, QWidget, QLabel, QApplication, QMainWindow, QFileDialog, QAction
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtCore import Qt
from PyQt5 import uic
import sys
import os
import urllib.request
from urllib.request import Request, urlopen
import shutil
import zipfile
import threading
import re
import webbrowser
import argparse
import random
import time
import os
import sys
from pythonosc import udp_client
form_class = uic.loadUiType("TC.ui")[0]


class WindowClass(QMainWindow, form_class) :
    def __init__(self) :
        super().__init__()
        self.setupUi(self)
        self.sb_x.setValue(0)
        self.sb_y.setValue(0)
        self.sb_x.valueChanged.connect(self.change_x)
        self.sb_y.valueChanged.connect(self.change_y)
    def change_x(self) :
        num = self.sb_x.value()
        self.lbl_x.setText(str(self.sb_x.value()))
        parser = argparse.ArgumentParser()
        parser.add_argument("--ip", default="127.0.0.1",
        help="The ip of the OSC server")
        parser.add_argument("--port", type=int, default=9000,
        help="The port the OSC server is listening on")
        args = parser.parse_args()
        client = udp_client.SimpleUDPClient(args.ip, args.port)
        client.send_message("/avatar/parameters/TCX", num)
    def change_y(self) :
        num = self.sb_y.value()
        self.lbl_y.setText(str(self.sb_y.value()))
        parser = argparse.ArgumentParser()
        parser.add_argument("--ip", default="127.0.0.1",
        help="The ip of the OSC server")
        parser.add_argument("--port", type=int, default=9000,
        help="The port the OSC server is listening on")
        args = parser.parse_args()
        client = udp_client.SimpleUDPClient(args.ip, args.port)
        client.send_message("/avatar/parameters/TCY", num)
        
if __name__ == "__main__" :
    parser = argparse.ArgumentParser()
    parser.add_argument("--ip", default="127.0.0.1",
          help="The ip of the OSC server")
    parser.add_argument("--port", type=int, default=9000,
          help="The port the OSC server is listening on")
    args = parser.parse_args()

    client = udp_client.SimpleUDPClient(args.ip, args.port)


    app = QApplication(sys.argv)
    myWindow = WindowClass()
    myWindow.show()
    app.exec_()
    sys.exit()