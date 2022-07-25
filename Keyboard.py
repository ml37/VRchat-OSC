import argparse
import random
import time
import os
import sys
from pythonosc import udp_client
from tkinter import *
from PIL import Image, ImageTk

if __name__ == "__main__":
  parser = argparse.ArgumentParser()
  parser.add_argument("--ip", default="127.0.0.1",
      help="The ip of the OSC server")
  parser.add_argument("--port", type=int, default=9000,
      help="The port the OSC server is listening on")
  args = parser.parse_args()

  client = udp_client.SimpleUDPClient(args.ip, args.port)

  
client.send_message("/avatar/parameters/Keyboard", 16)