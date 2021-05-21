from zeep import Client
from zeep.transports import Transport
from requests import Session
from datetime import datetime
from settings.parameters import *
from settings.credentials import *
from modules.getInformationsRequestSGI import InformationsRequestSGI


class PyQualitor:
    def __init__(self):
        pass

    def openQualitor(self, cliente, contato, tarefas):
        session = Session()
        session.verify = False
        transport = Transport(session=session)
        wsdl = WSDL
        client = Client(wsdl, transport=transport)
        wsAuth = client.service.login(CRD_USER_CONT_QUALITOR,CRD_PWD_CONT_QUALITOR,'1')

        #Cria XML de transporte para WS
        wsXML = ""
        wsXML += "<?xml version='1.0' encoding='ISO-8859-1'?>\n"
        wsXML += "<wsqualitor>\n"
        wsXML += "   <contents>\n"
        wsXML += "       <data>\n"
        wsXML += "           <cdperfilchamado>168571</cdperfilchamado>\n"
        wsXML += "           <cdcliente>" + cliente + "</cdcliente>\n"
        wsXML += "           <cdcontato>" + contato + "</cdcontato>\n"
        wsXML += "           <nmtitulochamado>Criação de GH para o gestor " + str(tarefas[1]) + "</nmtitulochamado>\n"
        wsXML += "           <dschamado>\n"
        wsXML += "              "+ InformationsRequestSGI.getInformationsRequestSGI(None, 282418, str(tarefas[3]), str(tarefas[1])) + "\n"
        wsXML += "           </dschamado>\n"
        wsXML += "       </data>\n"
        wsXML += "       <informacoesadicionais>\n"
        wsXML += "          <vlinformacaoadicional48>" + str(tarefas[3]) + "</vlinformacaoadicional48>\n"
        wsXML += "          <vlinformacaoadicional7></vlinformacaoadicional7>\n"
        wsXML += "       </informacoesadicionais>\n"
        wsXML += "   </contents>\n"
        wsXML += "</wsqualitor>"

        wsRetorno = ''

        try:
            wsRetorno = client.service.addTicketByTemplate(wsAuth, wsXML)
            log = open('/control/logExec.txt', 'a')
            log.writelines(str(datetime.now().strftime('%d/%m/%Y-%H:%M:%S') + ": SUCESSO na abertura do chamado --> " + wsRetorno + "\n"))
            log.close()
            sendcontrol = open('/control/sendControl.txt', 'a')
            sendcontrol.writelines(str(tarefas[0])+"\n")
            sendcontrol.close()
        except:
            log = open('/control/logExec.txt', 'a')
            log.writelines(str(datetime.now().strftime('%d/%m/%Y-%H:%M:%S') + ": ERRO na abertura do chamado --> " + wsRetorno + "\n"))
            log.close()