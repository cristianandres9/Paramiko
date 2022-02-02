from http import client
from unittest import result
import json
import paramiko
import time



HOST = ""
HOST2 = ""
USER = ''
PASSWORD = ''
SEPARADOR = '========================================================================================================================='

if __name__ == '__main__':
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(HOST, username=USER, password=PASSWORD)

    print(HOST)
    stdin, stdout, stderr = client.exec_command('./rutinacentreon.sh')
    time.sleep(1)
    rutina = stdout.read().decode()
    print(rutina)
    
    #tirar segundo comando no funciona
    stdin, stdout, stderr = client.exec_command('ls')
    time.sleep(1)
    listar = stdout.read().decode()

    print('============================================')
    #Crear un archivo plano y guardar la salida
    file = open('estetalvez.txt', 'w')
    file.write(''.join(rutina))
    file.write(''.join(SEPARADOR))
    file.close() 