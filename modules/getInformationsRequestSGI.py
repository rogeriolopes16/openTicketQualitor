import urllib3
urllib3.disable_warnings()
from modules.getDataBase import *

gdb = GetDataBase()

class InformationsRequestSGI:
    def __init__(self):
        pass

    def getInformationsRequestSGI(self,tarefa, empresa, gestor):
        blazon = gdb.blazon_payload(tarefa)

        script = "Chamado aberto via SGI para criação de GH.\n\n"
        script += "TIPO DE SOLICITAÇÃO: INCLUSÃO DE GH\n"
        script += "EMPRESA: " + empresa + "\n"
        script += "DESCRIÇÃO DO GH: " + blazon['account']['Banco'] + "\n"
        script += "DESCRIÇÃO DO GH: " + str(gestor) + "\n"
        script += "RESPONSÁVEL PELO GH: " + str(gestor) + "\n"
        script += "ÁREA ACIMA: " + str(gestor) + "\n"
        script += "OBSERVAÇÃO: " + str(gestor) + ""

        return script