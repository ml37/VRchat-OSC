import argparse
import time
from pythonosc import udp_client


parser = argparse.ArgumentParser()
parser.add_argument("--ip", default="127.0.0.1",
    help="The ip of the OSC server")
parser.add_argument("--port", type=int, default=9000,
    help="The port the OSC server is listening on")
args = parser.parse_args()
client = udp_client.SimpleUDPClient(args.ip, args.port)
client.send_message("/avatar/parameters/MaruMegane", True)
client.send_message("/avatar/parameters/", (5))