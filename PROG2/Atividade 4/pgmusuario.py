## Gravando a senha de forma criptografada usando hash 256
from hashlib import sha256
import sqlite3
conn = sqlite3.connect("dbEmpresa.db")
while True:
    print("   CADASTRO DE USUÁRIO  ")
    vid    = input("ID: ")
    vnome  = input("NOME: ")
    vcpf   = input("CPF: ")
    vemail = input("E-MAIL: ")
    vlogin = input("Login: ")
    vsenha = input("Senha: ")
    #Obtém hash da senha informada para gravar no banco
    vsenha = sha256(vsenha.encode('utf-8')).hexdigest()
    
    vconfirma = input("Deseja cadastrar? (s/n)")
    if vconfirma.upper() == "S":
        conn.execute('''insert into usuario values (?,?,?,?,?,?)''',
                     (vid,vnome,vcpf,vemail,vlogin,vsenha))
        conn.commit()
    else:
       print("Não será gravado!")
    vcontinua = input("Digite s para continuar ou n para sair: ")
    if vcontinua.upper() != "S":
       break  
conn.close()
quit()
