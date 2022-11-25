import ibm_db
import random
import string
from hashing import *

conn = ibm_db.connect("DATABASE=bludb;HOSTNAME=b0aebb68-94fa-46ec-a1fc-1c999edb6187.c3n41cmd0nqnrk39u98g.databases.appdomain.cloud;PORT=31249;SECURITY=SSL;SSLServerCertificate=DigiCertGlobalRootCA.crt;UID=xzw01423;PWD=GAp6EOTF05SHG1sM",'', '')
print("Connection Successful")
print(conn)

def signupusersdb(name, email, password):
    # key = ''.join(random.choices(string.ascii_lowercase + string.digits, k=25))
    key = ''.join(random.choices(string.ascii_lowercase +string.digits, k=25))
    print("signup")
    arr = hashing(password)
    stmt = "insert into user (NAME, PASSWORD,EMAIL,RANDOMKEY ) values ('"+name+"','"+ email+"','"+ str(arr.decode()) +"','"+ key+"' );"
    if ibm_db.exec_immediate(conn, stmt):
        return '{"result":"Done"}'
    return '{"result":"Not Found"}'


def signinusersdb(email,password):
    stmt = ibm_db.exec_immediate(conn, "select password,uid,random_key,name from user where EMAIL='"+email+"';")
    while ibm_db.fetch_row(stmt) != False:
        value = ibm_db.result(stmt, 0)
        key = ibm_db.result(stmt, 1)
        randomid = ibm_db.result(stmt, 2)
        dname = ibm_db.result(stmt,3)
        # print(value)
        r = rehashing(value,password,key,randomid,dname)
        # print(r)
        return r
    return '{"result":"Not Found"}'





