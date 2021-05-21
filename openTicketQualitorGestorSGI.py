import urllib3
urllib3.disable_warnings()
from datetime import datetime
from modules.pyQualitor import PyQualitor
from modules.getDataBase import *

print(str(datetime.now().strftime('%d/%m/%Y-%H:%M:%S')+': Inicio da atividade'))

#--------------------------- Lê arquivo de controle de chamados já enviados ---------------------------
sendControl = open('/control/sendControl.txt', 'r').readlines()
list_sendControl = []

for n in sendControl:
    list_sendControl.append(n.rstrip())

gdb = GetDataBase()

for tarefas in gdb.blazon():
    if str(tarefas[0]) not in list_sendControl:
        print(tarefas)
        contato_qualitor = gdb.contact_qualitor(tarefas[1])
        print(contato_qualitor)

        if contato_qualitor == []:
            cliente = '11'
            contato = '2164'
        else:
            cliente = str(contato_qualitor[0][1])
            contato = str(contato_qualitor[0][2])

        PyQualitor.openQualitor(None,cliente, contato, tarefas)

print(str(datetime.now().strftime('%d/%m/%Y-%H:%M:%S')+': Fim da atividade'))