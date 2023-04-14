
import  sqlite3

conn = sqlite3.connect('C:\\Users\\Natanael Matos\\OneDrive\\Área de Trabalho\\curando\\dados.db',  check_same_thread=False)
cursor = conn.cursor()

def veri_login(username, email):

    login_ok = False
    
    try:
        
        cursor.execute("SELECT * FROM usuarios WHERE email = ?", (email,))
        
        user = cursor.fetchone()
        print(user)
        if user:
            if user[1] == username and user[2] == email:
                conn.commit()
                user  = cursor.execute("""SELECT * FROM usuarios  WHERE   email  = ?""",(email))
                print(user)
                login_ok= True
                return login_ok
                
        else:
            login_ok = False
            return login_ok         
    except  Exception:
        conn.rollback()
        login_ok = False


