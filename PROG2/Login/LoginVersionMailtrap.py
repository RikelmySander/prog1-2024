import sqlite3
import smtplib
import random
import string
from email.message import EmailMessage

def conectar_banco():
    return sqlite3.connect("dbLogin.db")

def verificar_login(login, senha):
    conn = conectar_banco()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM usuarios WHERE login = ? AND senha = ?", (login, senha))
    usuario = cursor.fetchone()
    conn.close()
    return usuario is not None

def solicitar_login():
    tentativas = 5
    while tentativas > 0:
        login = input("Login: ")
        senha = input("Senha: ")

        if verificar_login(login, senha):
            print("✅ Acesso Permitido")
            return
        else:
            tentativas -= 1
            print(f"❌ Acesso Negado. Tentativas restantes: {tentativas}")
    print("⚠️ Número máximo de tentativas excedido.")

def gerar_codigo():
    return ''.join(random.choices(string.ascii_letters + string.digits, k=6))

def enviar_email(email, codigo):
    SMTP_SERVER = "sandbox.smtp.mailtrap.io"
    SMTP_PORT = 2525
    USERNAME = "ed929ee5963f44"
    PASSWORD = "fc03f218f4f3e5"

    try:
        msg = EmailMessage()
        msg["Subject"] = "Código de Recuperação"
        msg["From"] = "sistema@seudominio.com"
        msg["To"] = email
        msg.set_content(f"Seu código de recuperação é: {codigo}", charset="utf-8")

        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.set_debuglevel(1)
            server.login(USERNAME, PASSWORD)
            server.send_message(msg)

        print("📧 E-mail enviado com sucesso!")
    except Exception as e:
        print("❌ Erro ao enviar e-mail:", e)

def recuperar_senha():
    login = input("Informe seu login: ")
    conn = conectar_banco()
    cursor = conn.cursor()
    cursor.execute("SELECT email FROM usuarios WHERE login = ?", (login,))
    usuario = cursor.fetchone()

    if usuario:
        email = usuario[0]
        codigo = gerar_codigo()
        cursor.execute("UPDATE usuarios SET codigo_recuperacao = ? WHERE login = ?", (codigo, login))
        conn.commit()
        conn.close()

        enviar_email(email, codigo)

        codigo_digitado = input("Digite o código enviado ao seu e-mail: ")
        if codigo_digitado == codigo:
            nova_senha = input("Digite sua nova senha: ")
            conn = conectar_banco()
            cursor = conn.cursor()
            cursor.execute("UPDATE usuarios SET senha = ?, codigo_recuperacao = NULL WHERE login = ?", (nova_senha, login))
            conn.commit()
            conn.close()
            print("🔐 Senha alterada com sucesso!")
        else:
            print("❌ Código incorreto!")
    else:
        print("⚠️ Login não encontrado.")

def menu():
    while True:
        print("\n=== Sistema de Login ===")
        print("1. Login")
        print("2. Esqueci a senha")
        print("3. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            solicitar_login()
        elif opcao == "2":
            recuperar_senha()
        elif opcao == "3":
            print("Encerrando o programa...")
            break
        else:
            print("❌ Opção inválida!")

if __name__ == "__main__":
    menu()