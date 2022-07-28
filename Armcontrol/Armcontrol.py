import argparse
import random
import time
import os
import sys
from pythonosc import udp_client
from tkinter import *
from PIL import Image, ImageTk


parser = argparse.ArgumentParser()
parser.add_argument("--ip", default="127.0.0.1",
help="The ip of the OSC server")
parser.add_argument("--port", type=int, default=9000,
help="The port the OSC server is listening on")
args = parser.parse_args()
client = udp_client.SimpleUDPClient(args.ip, args.port)
def a1():
    client.send_message("/avatar/parameters/Rarm", 1.00)
def a2():
    client.send_message("/avatar/parameters/Rarm", 0.00)

root = Tk() 
root.title("Text to Emotion")
root.geometry("800x800")

Rfull = Button(root, text="Rfull", command=lambda: a1())
Rfull.place(x=0, y=85)
RMin = Button(root, text="RMin", command=lambda: a2())
RMin.place(x=0, y=170)

    

mainloop()

if __name__ == "__main__":
  parser = argparse.ArgumentParser()
  parser.add_argument("--ip", default="127.0.0.1",
      help="The ip of the OSC server")
  parser.add_argument("--port", type=int, default=9000,
      help="The port the OSC server is listening on")
  args = parser.parse_args()

  client = udp_client.SimpleUDPClient(args.ip, args.port)



'''int askinputvalue 0~32'''
'''while True:
    UserInput =  input("Please input the value of the parameter: ")
    UserInput = int(UserInput)
    client.send_message("/avatar/parameters/Textchat", UserInput)'''
