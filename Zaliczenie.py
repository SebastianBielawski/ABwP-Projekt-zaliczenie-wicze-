from cryptography.fernet import Fernet
import sqlite3

# 1. Moduł szyfrowania (AES symulowany za pomocą Fernet)
def simple_encryption():
    print("Proste szyfrowanie")

    # Generowanie klucza
    key = Fernet.generate_key()
    cipher = Fernet(key)
    print(f"Klucz: {key.decode()}")

    # Szyfrowanie wiadomości
    message = "Dzień dobry, cześć i czołem".encode()
    encrypted_message = cipher.encrypt(message)
    print(f"Zaszyfrowana wiadomość: {encrypted_message.decode()}")

    # Odszyfrowanie wiadomości
    decrypted_message = cipher.decrypt(encrypted_message)
    print(f"Odszyfrowana wiadomość: {decrypted_message.decode()}\n")


# 2. Moduł SQL Injection
def simple_sql_injection():
    print("Prosta demonstracja SQL Injection")

    # Tworzenie bazy danych w pamięci
    conn = sqlite3.connect(":memory:")
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE users (username TEXT, password TEXT)")
    cursor.execute("INSERT INTO users VALUES ('admin', '1234')")
    conn.commit()

    # Przykład podatności na SQL Injection
    print("Atak SQL Injection...")
    username_input = "admin' OR '1'='1"
    query = f"SELECT * FROM users WHERE username = '{username_input}'"
    print(f"Zapytanie: {query}")
    cursor.execute(query)
    rows = cursor.fetchall()

    if rows:
        print("SQL Injection udane! Zwrócone dane:")
        for row in rows:
            print(row)
    else:
        print("Brak wyników.")

    # Zabezpieczenie przed SQL Injection
    print("\nZabezpieczenie przed SQL Injection...")
    secure_username = "admin"
    cursor.execute("SELECT * FROM users WHERE username = ?", (secure_username,))
    rows = cursor.fetchall()

    if rows:
        print("Zabezpieczenie działa! Zwrócone dane:")
        for row in rows:
            print(row)
    else:
        print("Nie znaleziono użytkownika.")

    conn.close()

# Uruchomienie
if __name__ == "__main__":
    simple_encryption()   # Moduł szyfrowania
    simple_sql_injection()  # Moduł SQL Injection
