from app import app
from flask import  make_response, render_template, request
import sqlite3

# Conexão com o banco de dados SQLite3
conn = sqlite3.connect('dados.db',  check_same_thread=False)
cursor = conn.cursor()


# Cria a tabela no banco de dados, caso ainda não exista
cursor.execute("""
    CREATE TABLE IF NOT EXISTS usuarios (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        email TEXT NOT NULL UNIQUE
    );
""")
conn.commit()  # É importante sempre realizar um commit depois de executar uma alteração no banco de dados




def tentar():
    pass

def caso_erro_já_cadastrado():
    pass 

def efetuando_cadastro(nome, email):
    # Insere o novo usuário no banco de dados
    cursor.execute("INSERT INTO usuarios (nome, email) VALUES (?, ?)", (nome, email))
    conn.commit()

    # Retorna uma mensagem de sucesso para o usuário
    return "Usuário cadastrado com sucesso!"

def veri_login(username, email):
    print(username,  email)
    login_ok = False
    
    try:
        
        cursor.execute("SELECT * FROM usuarios WHERE email = ?", (email,))
        
        user = cursor.fetchone()
        print(user)
        resultado_username = user[1]
        resultado_email = user[2]
        print(resultado_email, resultado_username)
        if user:
            if resultado_username == username and resultado_email == email:
                print(user)
                login_ok= True
                return login_ok
                
        else:
            login_ok = False
            return login_ok         
    except  Exception:
        conn.rollback()
        login_ok = False
        return login_ok
print(veri_login("natan", "natanirmao11@gmail.com"))


   