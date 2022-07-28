import cv2
import mediapipe as mp
import math
import argparse
import random
import time
import os
import sys
from pythonosc import udp_client
from tkinter import *
from PIL import Image, ImageTk

cap = cv2.VideoCapture(0)

mpHands = mp.solutions.hands
my_hands = mpHands.Hands()
mpDraw = mp.solutions.drawing_utils

def dist(x1,y1,x2,y2):
    return math.sqrt(math.pow(x1 - x2,2)) + math.sqrt(math.pow(y1 - y2,2))

compareIndex = [[18,4],[6,8],[10,12],[14,16],[18,20]]
open = [False,False,False,False,False]

while True:
    success,img = cap.read()
    h,w,c = img.shape
    imgRGB = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    results = my_hands.process(imgRGB)
    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            for i in range(0,5):
                open[i] = dist(handLms.landmark[0].x,handLms.landmark[0].y,handLms.landmark[compareIndex[i][0]].x,handLms.landmark[compareIndex[i][0]].y) < dist(handLms.landmark[0].x,handLms.landmark[0].y,handLms.landmark[compareIndex[i][1]].x,handLms.landmark[compareIndex[i][1]].y)
            print(open)
            parser = argparse.ArgumentParser()
            parser.add_argument("--ip", default="127.0.0.1",
            help="The ip of the OSC server")
            parser.add_argument("--port", type=int, default=9000,
            help="The port the OSC server is listening on")
            args = parser.parse_args()
            client = udp_client.SimpleUDPClient(args.ip, args.port) 
            if open == [True,True,True,True,True]:
                client.send_message("/avatar/parameters/Textchat", 1)
            elif open == [False,True,False,False,False]: 
                client.send_message("/avatar/parameters/Textchat", 2)
            elif open == [False,True,True,False,False]: 
                client.send_message("/avatar/parameters/Textchat", 3)
            elif open == [False,True,True,True,False]: 
                client.send_message("/avatar/parameters/Textchat", 4)
            elif open == [False,True,True,True,True]: 
                client.send_message("/avatar/parameters/Textchat", 5)
            mpDraw.draw_landmarks(img,handLms,mpHands.HAND_CONNECTIONS)

    cv2.imshow("HandTracking", img)
    cv2.waitKey(1)

#from https://developeralice.tistory.com/10