# import the necessary packages
from imutils.video import VideoStream
import imagezmq
import argparse
import socket
import time
# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-s", "--server-ip", required=True,
	help="Direccion ip del servidor de destino")
args = vars(ap.parse_args())
# initialize the ImageSender object with the socket address of the
# server
sender = imagezmq.ImageSender(connect_to="tcp://{}:5555".format(args["server_ip"]))

# get the host name, initialize the video stream, and allow the
# camera sensor to warmup
hostname = socket.gethostname()

try:
  import RPi.GPIO as gpio
  rpi = True
  print('Codigo ejecutandose en modo RPI')
except (ImportError, RuntimeError):
  rpi = False
  print('Codigo no ejecutandose en modo RPI')

if rpi == True:
	vs = VideoStream(usePiCamera=True).start()
if rpi == False:
	vs = VideoStream(src=0).start()

time.sleep(2.0)
print('inicio camara')
while True:
	frame = vs.read()
	sender.send_image(hostname, frame)