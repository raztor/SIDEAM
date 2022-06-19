import torch
import numpy as np
import cv2
import argparse
import socket
import imagezmq
from time import time
from imutils import build_montages
import imutils

class MugDetection:
    """
    Class implements Yolo5 model to make inferences on a youtube video using Opencv2.
    """

    def __init__(self, capture_index, model_name):
        """
        Initializes the class with youtube url and output file.
        :param url: Has to be as youtube URL,on which prediction is made.
        :param out_file: A valid output file name.
        """
        self.capture_index = capture_index
        self.model = self.load_model(model_name)
        self.classes = self.model.names
        self.device = 'cuda' if torch.cuda.is_available() else 'cpu'
        print("Using Device: ", self.device)


    def get_video_capture(self):
        """
        Creates a new video streaming object to extract video frame by frame to make prediction on.
        :return: opencv2 video capture object, with lowest quality frame available for video.
        """

        return cv2.VideoCapture(self.capture_index)

    def load_model(self, model_name):
        """
        Loads Yolo5 model from pytorch hub.
        :return: Trained Pytorch model.
        """
        if model_name:
            model = torch.hub.load('ultralytics/yolov5', 'custom', path=model_name, force_reload=True)
        else:
            model = torch.hub.load('ultralytics/yolov5', 'yolov5s', pretrained=True)
        return model

    def score_frame(self, frame):
        """
        Takes a single frame as input, and scores the frame using yolo5 model.
        :param frame: input frame in numpy/list/tuple format.
        :return: Labels and Coordinates of objects detected by model in the frame.
        """
        self.model.to(self.device)
        frame = [frame]
        results = self.model(frame)
        labels, cord = results.xyxyn[0][:, -1], results.xyxyn[0][:, :-1]
        '''Confianza pero solo para el primer objeto'''
        try:
            preconf = (results.pandas().xyxy[0].sort_values('confidence'))  # [:, :-1])
            preconf = preconf.to_numpy()
            confidence = round(preconf.item(4), 2)
            return labels, cord, confidence
        except:
            return labels, cord

    def class_to_label(self, x):
        """
        For a given label value, return corresponding string label.
        :param x: numeric label
        :return: corresponding string label
        """
        return self.classes[int(x)]

    def plot_boxes(self, results, frame):
        """
        Takes a frame and its results as input, and plots the bounding boxes and label on to the frame.
        :param results: contains labels and coordinates predicted by model on the given frame.
        :param frame: Frame which has been scored.
        :return: Frame with bounding boxes and labels ploted on it.
        """
        try:
            labels, cord, confidence = results
        except:
            labels, cord = results

        n = len(labels)
        x_shape, y_shape = frame.shape[1], frame.shape[0]
        for i in range(n):
            row = cord[i]
            if fuente == 'rpi':
                if row[4] >= 0.3:
                    x1, y1, x2, y2 = int(row[0] * x_shape), int(row[1] * y_shape), int(row[2] * x_shape), int(
                        row[3] * y_shape)
                    bgr = (0, 255, 0)
                    cv2.rectangle(frame, (x1, y1), (x2, y2), bgr, 2)
                    cv2.putText(frame, self.class_to_label(labels[i]), (x1, y1), cv2.FONT_HERSHEY_SIMPLEX, 0.9, bgr, 2)
                    '''Print de la confidencia'''
                    print(confidence)

            else:
                if row[4] >= 0.81:
                    x1, y1, x2, y2 = int(row[0] * x_shape), int(row[1] * y_shape), int(row[2] * x_shape), int(
                        row[3] * y_shape)
                    bgr = (0, 255, 0)
                    cv2.rectangle(frame, (x1, y1), (x2, y2), bgr, 2)
                    cv2.putText(frame, self.class_to_label(labels[i]), (x1, y1), cv2.FONT_HERSHEY_SIMPLEX, 0.9, bgr, 2)
                    '''Print de la confidencia'''
                    print(confidence)
        return frame

    def __call__(self):
        """
        This function is called when class is executed, it runs the loop to read the video frame by frame,
        and write the output into a new file.
        :return: void
        """
        if fuente == 'ipcam':
            cap = stream
        elif fuente == 'webcam':
            cap = self.get_video_capture()
            assert cap.isOpened()
        elif fuente == 'rpi':
            pass

        print('Fin definicion de cap')

        while True:
            if fuente == 'rpi':
                hostname, frame = image_hub.recv_image()
                image_hub.send_reply(b'OK')
            else:
                ret, frame = cap.read()
            frame = cv2.resize(frame, (416, 416))

            start_time = time()
            results = self.score_frame(frame)
            frame = self.plot_boxes(results, frame)

            end_time = time()
            fps = 1 / np.round(end_time - start_time, 2)
            # print(f"Frames Per Second : {fps}")

            cv2.putText(frame, f'FPS: {int(fps)}', (20, 70), cv2.FONT_HERSHEY_SIMPLEX, 1.5, (0, 255, 0), 2)

            cv2.imshow(f'SIDEAM V.1({hostname})', frame)

            if cv2.waitKey(5) & 0xFF == 27:
                break
        if fuente == 'webcam':
            cap.release()


webcam_source = 'DUMMY'
hostname = socket.gethostname()
ap = argparse.ArgumentParser()
ap.add_argument("-f", "--fuente", required=True,
    help="seleccionar la fuente de video (webcam, rpi, yt, ipcam)")
fuente = vars(ap.parse_args())['fuente']

print(f'Usando {fuente} como fuente de imagen')

if fuente == 'rpi':
    image_hub = imagezmq.ImageHub()
elif fuente == 'ipcam':
    stream = cv2.VideoCapture('rtsp://usuario:usuario@10.6.110.13/mpeg4/media.amp')
    print('detectado stream')
elif fuente == 'webcam':
    webcam_source = 0


detector = MugDetection(capture_index=webcam_source, model_name='./modelos/sideam.pt')
detector()