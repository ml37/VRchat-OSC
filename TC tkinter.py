import argparse
import random
import time
import os
import sys
from pythonosc import udp_client
from pythonosc import dispatcher
from pythonosc import  osc_server
from tkinter import *

parser = argparse.ArgumentParser()
parser.add_argument("--ip", default="127.0.0.1",
help="The ip of the OSC server")
parser.add_argument("--port", type=int, default=9000,
help="The port the OSC server is listening on")
args = parser.parse_args()
client = udp_client.SimpleUDPClient(args.ip, args.port)
        
def change(i,j):
        print(f'{j+1}, {i+1}')
        client.send_message("/avatar/parameters/TCX", int(j+1))
        client.send_message("/avatar/parameters/TCY", int(i+1))
def changeE(i,j):
        print(f'{j+1}, {i+1}')
        client.send_message("/avatar/parameters/TCXE", int(j+1))
        client.send_message("/avatar/parameters/TCYE", int(i+1))
def on():
        parser = argparse.ArgumentParser()
        parser.add_argument("--ip", default="127.0.0.1",
        help="The ip of the OSC server")
        parser.add_argument("--port", type=int, default=9000,
        help="The port the OSC server is listening on")
        args = parser.parse_args()
        client = udp_client.SimpleUDPClient(args.ip, args.port)
        client.send_message("/avatar/parameters/TextchatOnOff", True)
def off():
        parser = argparse.ArgumentParser()
        parser.add_argument("--ip", default="127.0.0.1",
        help="The ip of the OSC server")
        parser.add_argument("--port", type=int, default=9000,
        help="The port the OSC server is listening on")
        args = parser.parse_args()
        client = udp_client.SimpleUDPClient(args.ip, args.port)
        client.send_message("/avatar/parameters/TextchatOnOff", False)
def img_load():
        if os.path.isfile('D:\git\VRCSDK3_Koyuki\Assets\Koyuki\TTT system\TC100_2000.png') == True:
                img_bg = PhotoImage(file="D:\git\VRCSDK3_Koyuki\Assets\Koyuki\TTT system\TC100_2000.png")
                canvas.create_image(0,0, anchor=NW, image=img_bg)
def TCEOn():
        parser = argparse.ArgumentParser()
        parser.add_argument("--ip", default="127.0.0.1",
        help="The ip of the OSC server")
        parser.add_argument("--port", type=int, default=9000,
        help="The port the OSC server is listening on")
        args = parser.parse_args()
        client = udp_client.SimpleUDPClient(args.ip, args.port)
        client.send_message("/avatar/parameters/TCEOn", True)
def TCEOff():
        parser = argparse.ArgumentParser()
        parser.add_argument("--ip", default="127.0.0.1",
        help="The ip of the OSC server")
        parser.add_argument("--port", type=int, default=9000,
        help="The port the OSC server is listening on")
        args = parser.parse_args()
        client = udp_client.SimpleUDPClient(args.ip, args.port)
        client.send_message("/avatar/parameters/TCEOn", False)
def top():
        print('top')
        parser = argparse.ArgumentParser()
        parser.add_argument("--ip", default="127.0.0.1",
        help="The ip of the OSC server")
        parser.add_argument("--port", type=int, default=9000,
        help="The port the OSC server is listening on")
        args = parser.parse_args()
        client = udp_client.SimpleUDPClient(args.ip, args.port)
        client.send_message("/avatar/parameters/Mid", False)
        client.send_message("/avatar/parameters/Top", True)
def mid():
        print('mid')
        parser = argparse.ArgumentParser()
        parser.add_argument("--ip", default="127.0.0.1",
        help="The ip of the OSC server")
        parser.add_argument("--port", type=int, default=9000,
        help="The port the OSC server is listening on")
        args = parser.parse_args()
        client = udp_client.SimpleUDPClient(args.ip, args.port)
        client.send_message("/avatar/parameters/Mid", True)
        client.send_message("/avatar/parameters/Top", False)

root = Tk() 
root.title("Text to Emotion")
root.geometry("1400x800")
canvas = Canvas(root, width = 700, height = 700) 
canvas.place(x=0, y=0)

buttons = [[0 for x in range(10)] for y in range(10)]
for i in range(10):
    for j in range(10):
        buttons[i][j] = Button(root, text=f"{j+i*10+1}", width=8, height=4, command=lambda i=i, j=j: change(i, j))
        buttons[i][j].place(y=(9 - i)*70 , x=j*70)
buttons2 = [[0 for x in range(10)] for y in range(10)]
for i in range(10):
    for j in range(10):
        buttons2[i][j] = Button(root, text=f"{j+i*10+1}", width=8, height=4, command=lambda i=i, j=j: changeE(i, j))
        buttons2[i][j].place(y=(9 - i)*70 , x=j*70 + 720)
OnRadiobutton = Radiobutton(root, text="On", value=1, command=lambda: on())
OffRadiobutton = Radiobutton(root, text="Off", value=0, command=lambda: off())
OnRadiobutton.place(y=700, x=100)
OffRadiobutton.place(y=700, x=200)
TCEOnRadioButton = Radiobutton(root, text="On", value=1, command=lambda: TCEOn())
TCEOffRadioButton = Radiobutton(root, text="Off", value=0, command=lambda: TCEOff())
TCEOnRadioButton.place(y=700, x=300)
TCEOffRadioButton.place(y=700, x=400)
buton = Button(root, text="Top", command=lambda: top())
buton.place(y=700, x=500)
buton2 = Button(root, text="Mid", command=lambda: mid())
buton2.place(y=700, x=600)
mainloop()
if __name__ == "__main__":
  parser = argparse.ArgumentParser()
  parser.add_argument("--ip",
      default="127.0.0.1", help="The ip to listen on")
  parser.add_argument("--port",
      type=int, default=5005, help="The port to listen on")
  args = parser.parse_args()

  ###code must be translate from tkinter to pyqt