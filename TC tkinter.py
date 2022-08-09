import argparse
import random
import time
import os
import sys
from pythonosc import udp_client
from tkinter import *

def change(i,j):
        print(f'{j+1}, {i+1}')
        parser = argparse.ArgumentParser()
        parser.add_argument("--ip", default="127.0.0.1",
        help="The ip of the OSC server")
        parser.add_argument("--port", type=int, default=9000,
        help="The port the OSC server is listening on")
        args = parser.parse_args()
        client = udp_client.SimpleUDPClient(args.ip, args.port)
        client.send_message("/avatar/parameters/TCX", j+1)
        client.send_message("/avatar/parameters/TCY", i+1)
root = Tk() 
root.title("Text to Emotion")
root.geometry("800x800")
canvas = Canvas(root, width = 700, height = 700) 
canvas.place(x=0, y=0)
img = PhotoImage(file="D:\git\VRCSDK3_Koyuki\Assets\Koyuki\TTT system\TC100_2000.png")
canvas.create_image(0,0, anchor=NW, image=img)

buttons = [[0 for x in range(10)] for y in range(10)]
for i in range(10):
    for j in range(10):
        buttons[i][j] = Button(root, text=f"{j+i*10+1}", width=8, height=4, command=lambda i=i, j=j: change(i, j))
        buttons[i][j].place(y=(9 - i)*70 , x=j*70)
mainloop()