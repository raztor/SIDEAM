import os
import shutil
import subprocess
import sys, time, threading

def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])
stop_loader = False
def the_process_function():
    while True:
        n = 20
        for i in range(n):
            time.sleep(1)
            sys.stdout.write('\r'+'loading...  process '+str(i)+'/'+str(n)+' '+ '{:.2f}'.format(i/n*100)+'%')
            sys.stdout.flush()
        sys.stdout.write('\r'+'loading... finished               \n')
        if stop_loader:
            break


def animated_loading():
    chars = "/—\|"
    for char in chars:
        sys.stdout.write('\r'+'loading...'+char)
        time.sleep(.1)
        sys.stdout.flush()

the_process = threading.Thread(name='Copiando', target=the_process_function)




destiny_folder = os.path.expanduser('~/Documents/SIDEAM-Trainer')

def copiar():
    print('Iniciando Copiado')
    print('')
    the_process.start()
    original = r'./yolov5-master'
    target = destiny_folder
    shutil.copytree(original, target)
    return 'Copia lista'


print(copiar())