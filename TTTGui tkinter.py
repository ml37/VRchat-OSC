import argparse
import random
import time
import os
import sys
from pythonosc import udp_client
from tkinter import *
from PIL import Image, ImageTk

def button_clicked(i, j):
    print("/avatar/parameters/Textchat " + str(j+i*8+1))
    selectanimation(j+i*8+1)
def selectanimation(num):
    parser = argparse.ArgumentParser()
    parser.add_argument("--ip", default="127.0.0.1",
    help="The ip of the OSC server")
    parser.add_argument("--port", type=int, default=9000,
    help="The port the OSC server is listening on")
    args = parser.parse_args()
    client = udp_client.SimpleUDPClient(args.ip, args.port)
    client.send_message("/avatar/parameters/Textchat", num)
def selectemotional(num):
    parser = argparse.ArgumentParser()
    parser.add_argument("--ip", default="127.0.0.1",
    help="The ip of the OSC server")
    parser.add_argument("--port", type=int, default=9000,
    help="The port the OSC server is listening on")
    args = parser.parse_args()
    client = udp_client.SimpleUDPClient(args.ip, args.port)
    client.send_message("/avatar/parameters/GestureR", num+1)
    client.send_message("/avatar/parameters/GestureLeft", num+1)

root = Tk() 
root.title("Text to Emotion")
root.geometry("800x800")

label1 = Label(root, text="Idle", font=("Arial", 20))
label1.place(x=0, y=85-40)
label2 = Label(root, text="pet", font=("Arial", 20))
label2.place(x=0, y=170-40)
label3 = Label(root, text="ohh", font=("Arial", 20))
label3.place(x=0, y=255-40)
label4 = Label(root, text="hihi", font=("Arial", 20))
label4.place(x=0, y=340-40)
label5 = Label(root, text="hea!", font=("Arial", 20))
label5.place(x=0, y=425-40)
label6 = Label(root, text="ahegao", font=("Arial", 20))
label6.place(x=0, y=510-40)
label7 = Label(root, text="twinkle", font=("Arial", 20))
label7.place(x=0, y=595-40)

canvas = Canvas(root, width = 720, height = 720) 
canvas.place(x=75, y=75)
img = PhotoImage(file="ABC 1.png")
trancepan = PhotoImage(file="trancepan.png")
canvas.create_image(0,0, anchor=NW, image=img)

buttons = [[0 for x in range(8)] for y in range(8)]
for i in range(8):
    for j in range(8):
        buttons[i][j] = Button(root, text=f"{j+i*8+1}", width=2, height=2, command=lambda i=i, j=j: button_clicked(i, j))
        buttons[i][j].place(y=(i+1)*85, x=(j+1)*85)
emobuttons = [0 for x in range(8)]
for i in range(7):
    emobuttons[i] = Button(root, text=f"{i+1}", width=2, height=2, command=lambda i=i: selectemotional(i))
    emobuttons[i].place(y=(i+1)*85, x=0)

    

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
