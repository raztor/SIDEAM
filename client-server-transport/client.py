# import the necessary packages
from imutils.video import VideoStream
import imagezmq
import argparse
import socket
import time
# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-s", "--server-ip", required=True,
	help="ip address of the server to which the client will connect")
args = vars(ap.parse_args())
# initialize the ImageSender object with the socket address of the
# server
sender = imagezmq.ImageSender(connect_to="tcp://{}:5555".format(args["server_ip"]))

# get the host name, initialize the video stream, and allow the
# camera sensor to warmup
rpiName = socket.gethostname()

'''Si es un RPI'''
vs = VideoStream(usePiCamera=True).start()

'''Si es un computador'''
#vs = VideoStream(src=1).start()
time.sleep(2.0)
print('inicio camara')
while True:
	# read the frame from the camera and send it to the server
	frame = vs.read()
	sender.send_image(rpiName, frame)