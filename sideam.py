import torch
import numpy as np
import cv2
import argparse
import socket
import imagezmq
from time import time


def list_ports():
    non_working_ports = []
    dev_port = 0
    working_ports = []
    available_ports = []
    while len(non_working_ports) < 6:
        camera = cv2.VideoCapture(dev_port)
        if not camera.isOpened():
            non_working_ports.append(dev_port)
            # print("Port %s is not working." %dev_port)
        else:
            is_reading, img = camera.read()
            # w = camera.get(3)
            # h = camera.get(4)
            if is_reading:
                # print("Port %s is working and reads images (%s x %s)" %(dev_port,h,w))
                working_ports.append(dev_port)
            else:
                # print("Port %s for camera ( %s x %s) is present but does not reads." %(dev_port,h,w))
                available_ports.append(dev_port)
        dev_port += 1
    return working_ports


class MugDetection:

    def __init__(self, capture_index, model_name):
        self.capture_index = capture_index
        self.model = self.load_model(model_name)
        self.classes = self.model.names
        self.device = 'cuda' if torch.cuda.is_available() else 'cpu'
        print("Using Device: ", self.device)

    def get_video_capture(self):

        return cv2.VideoCapture(self.capture_index)

    def load_model(self, model_name):

        if model_name:
            model = torch.hub.load('ultralytics/yolov5', 'custom', path=model_name, force_reload=True)
        else:
            model = torch.hub.load('ultralytics/yolov5', 'yolov5s', pretrained=True)
        return model

    def score_frame(self, frame):

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
        except IndexError:
            return labels, cord

    def class_to_label(self, x):

        return self.classes[int(x)]

    def plot_boxes(self, results, frame):

        try:
            labels, cord, confidence = results
        except ValueError:
            labels, cord = results

        n = len(labels)
        x_shape, y_shape = frame.shape[1], frame.shape[0]
        for i in range(n):
            row = cord[i]
            if fuente == 'rpi':
                if row[4] >= 0.7:
                    x1, y1, x2, y2 = int(row[0] * x_shape), int(row[1] * y_shape), int(row[2] * x_shape), int(
                        row[3] * y_shape)
                    bgr = (0, 255, 0)
                    cv2.rectangle(frame, (x1, y1), (x2, y2), bgr, 2)
                    cv2.putText(frame, self.class_to_label(labels[i]), (x1, y1), cv2.FONT_HERSHEY_SIMPLEX, 0.9, bgr, 2)
            else:
                if row[4] >= 0.5:
                    x1, y1, x2, y2 = int(row[0] * x_shape), int(row[1] * y_shape), int(row[2] * x_shape), int(
                        row[3] * y_shape)
                    bgr = (0, 255, 0)
                    cv2.rectangle(frame, (x1, y1), (x2, y2), bgr, 2)
                    cv2.putText(frame, self.class_to_label(labels[i]), (x1, y1), cv2.FONT_HERSHEY_SIMPLEX, 0.9, bgr, 2)
        return frame

    def __call__(self):

        global hostname
        if fuente == 'ipcam':
            cap = stream
        elif fuente == 'webcam':
            cap = self.get_video_capture()
            assert cap.isOpened()
        elif fuente == 'rpi':
            pass
        else:
            raise Exception('Error desconocido al definir las fuentes')

        print('Fin definicion de cap')
        while True:
            if fuente == 'rpi':
                hostname, frame = image_hub.recv_image()
                image_hub.send_reply(b'OK')
            else:
                ret, frame = cap.read()
            # 416
            frame = cv2.resize(frame, (500, 500))

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


webcam_avaliable_fid = list_ports()
webcam_source = 'DUMMY'
hostname = socket.gethostname()
ap = argparse.ArgumentParser('Fuente de imagen')

ap.add_argument('-f', '--fuente', help='seleccionar la fuente de video (webcam, rpi, yt, ipcam)', default='webcam',
                choices=['webcam', 'rpi', 'ipcam', 'yt (proximamente)'])

ap.add_argument('-id', '--id', help='ingresa la url o id de la webcam', default='ERROR')
# ap.add_argument('-cf', '--confidence', help = 'Selecciona el nivel de confianza', default=0.7)
ap.add_argument('-m', '--model', help='Selecciona el modelo IA', default='sideam.pt')

args = vars(ap.parse_args())

fuente = args['fuente']
fid = args['id']
modelo = args['model']

if fuente == 'webcam':
    fid = int(fid)
    if fid not in webcam_avaliable_fid:
        while fid not in webcam_avaliable_fid:
            fid = 'ERROR'
            print('ERROR: ID de webcam no existe o no esta disponible\n')
            fid = int(input(f'Ingrese un id de webcam entre los siguientes {webcam_avaliable_fid}: '))
        print(f'El ID {fid} ingresado es correcto\n')

if fid == 'ERROR':
    if fuente == 'ipcam':
        raise Exception('ERROR, recuerda introducir la url usando --id url_camara_ip')


print(f'Usando {fuente} como fuente de imagen')

if fuente == 'rpi':
    image_hub = imagezmq.ImageHub()
elif fuente == 'ipcam':
    stream = cv2.VideoCapture(fid)
    print('Conectado a la cámara ip')
elif fuente == 'webcam':
    webcam_source = fid
    print('webcam detectada')

model_dir = f'./modelos/{modelo}'

detector = MugDetection(capture_index=webcam_source, model_name=model_dir)
detector()
