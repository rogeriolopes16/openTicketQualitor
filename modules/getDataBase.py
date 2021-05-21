import cx_Oracle
import mysql.connector
import json
from settings.credentials import *
from settings.parameters import *
from settings.db import *

#--------------------------- Abrindo conexão com Oracle ---------------------------
conn = cx_Oracle.connect(user=CRD_USER_DB_QUALITOR, password=CRD_PWD_DB_QUALITOR, dsn=PAR_QUALITOR_TNS)
c = conn.cursor()

# --------------------------- Abrindo conexão com MYSql Blazon ---------------------------
db = mysql.connector.connect(user=CRD_USER_DB_BLAZON, passwd=CRD_PWD_DB_BLAZON, host=PAR_BLAZON_IP,db=PAR_BLAZON_DB_NAME)
cursor_blazon = db.cursor()

class GetDataBase():
    def __init__(self):
        pass

    def blazon(self):
        cursor_blazon.execute(SELECT_BLAZON)
        db.close()
        return cursor_blazon.fetchall()

    def blazon_payload(self, tarefa):
        cursor_blazon.execute("select b.payload from BlazonRequest b, ProvisioningEntry p, Task t where b.provisioningEntryId = p.id and p.id = t.createdByObjectId and t.id = " + str(tarefa))
        blazon = cursor_blazon.fetchall()
        blazon = str(json.loads(json.dumps(blazon))[0][0])
        db.close()
        return json.loads(blazon)

    def contact_qualitor(self, contact):
        # --------------------------- Abrindo conexão com Qualitor ---------------------------
        conn = cx_Oracle.connect(user=CRD_USER_DB_QUALITOR, password=CRD_PWD_DB_QUALITOR, dsn=PAR_QUALITOR_TNS)
        c = conn.cursor()
        c.execute("select cl.nmcliente, co.cdcliente, co.cdcontato, co.nmcontato from ad_contato co, ad_cliente cl "
                  "where co.cdcliente = cl.cdcliente and co.idativo = 'Y' and co.nmcontato = '"+contact+"' and rownum = 1")
        return c.fetchall()