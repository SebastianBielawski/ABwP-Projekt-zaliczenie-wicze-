# ABwP-Projekt-zaliczeniowy

Dokumentacja aplikacji
Sebastian Bielawski 159850
Opis funkcjonalności
Aplikacja demonstruje dwa kluczowe zagadnienia związane z bezpieczeństwem:
1.	Zastosowanie szyfrowania: Proste szyfrowanie i deszyfrowanie wiadomości przy użyciu algorytmu Fernet.
2.	Podatność na SQL Injection oraz sposób zabezpieczenia przed nim: Demonstracja udanego ataku SQL Injection i jego zabezpieczenia za pomocą zapytań z parametrami.

Struktura aplikacji
Kod jest podzielony na dwa moduły:
1.	Moduł szyfrowania (Fernet):
  o	Wykorzystuje bibliotekę cryptography do szyfrowania i deszyfrowania wiadomości.
  o	Klucz jest generowany losowo, a wiadomość zaszyfrowana i odszyfrowana przy użyciu tego samego klucza.
2.	Moduł SQL Injection:
  o	Tworzy tymczasową bazę SQLite w pamięci z tabelą użytkowników.
  o	Prezentuje dwa zapytania SQL:
    	Zapytanie podatne na SQL Injection.
    	Zapytanie zabezpieczone przed SQL Injection za pomocą zapytań z parametrami.

Wykorzystane technologie
1.	Biblioteka cryptography (Fernet):
  o	Szyfr symetryczny zapewniający poufność danych.
  o	Zastosowanie w celu demonstracji szyfrowania i deszyfrowania wiadomości.
2.	SQLite:
  o	Lekka baza danych używana do przechowywania informacji o użytkownikach.
  o	Demonstracja podatności na SQL Injection i zabezpieczenia przed tym atakiem.


Szczegóły implementacji
1. Moduł szyfrowania (Fernet)
•	Jak działa?
  o	Generowany jest klucz szyfrowania przy użyciu Fernet.generate_key().
  o	Wiadomość tekstowa jest szyfrowana metodą symetryczną (ten sam klucz używany do szyfrowania i deszyfrowania).
  o	Zaszyfrowana wiadomość zawiera zarówno szyfrogram, jak i dane potrzebne do jej odszyfrowania.
•	Przykładowe dane wejściowe i wyjściowe:
  o	Wejście: Dzień dobry, cześć i czołem
  o	Zaszyfrowana wiadomość: gAAAAABnk8eP6ikz5EUjHdAosxfk1v-S9NRcwzx8ZiZeiTOpeUfPfmPb7IhhbHCBf3TPEV9ML_oCdxkBz0V2ZXIQVWibnmWiAxQan7_MT7rLNccM9keZP-A=
  o	Odszyfrowana wiadomość: Dzień dobry, cześć i czołem
•	Ewentualne problemy:
1.	Zgubienie klucza szyfrowania:
  	Jeśli klucz szyfrowania zostanie utracony, nie ma możliwości odszyfrowania danych.
  	Rozwiązanie: Klucz należy przechowywać w bezpiecznym miejscu, np. w menedżerze kluczy lub w zaszyfrowanej bazie danych.
2.	Przechwycenie klucza przez osobę trzecią:
  	Jeśli klucz trafi w niepowołane ręce, dane mogą zostać odszyfrowane.
  	Rozwiązanie: Użycie szyfrowania asymetrycznego (np. RSA) do wymiany klucza w bardziej złożonych aplikacjach.

2. Moduł SQL Injection
•	Jak działa SQL Injection?
  o	Zapytania SQL są podatne na wstrzyknięcia kodu, jeśli dane wejściowe użytkownika są bezpośrednio wstawiane do treści zapytania.
  o	W przykładzie zapytanie:
  SELECT * FROM users WHERE username = 'admin' OR '1'='1'
  powoduje, że warunek OR '1'='1' jest zawsze prawdziwy, dzięki czemu zwracani są wszyscy użytkownicy.

•	Jak działa zabezpieczenie?
  o	Przy zabezpieczonym zapytaniu dane wejściowe użytkownika są przekazywane jako parametry:
  cursor.execute("SELECT * FROM users WHERE username = ?", (secure_username,))
  o	Zapytanie z parametrami oddziela dane od kodu SQL, co uniemożliwia modyfikację logiki zapytania przez złośliwe dane wejściowe.
•	Ewentualne problemy:
1.	Niepoprawne wykorzystanie zapytań z parametrami:
  	Jeśli zabezpieczenie nie zostanie poprawnie zaimplementowane (np. użycie formatowania ciągów zamiast parametrów), zapytanie pozostaje podatne.
  	Rozwiązanie: Zawsze używaj zapytań z parametrami lub ORM (np. SQLAlchemy) do komunikacji z bazą danych.
2.	Używanie starych wersji SQLite lub innych baz danych:
  	Starsze wersje SQLite mogą nie obsługiwać zapytań z parametrami w pełni poprawnie.
  	Rozwiązanie: Regularnie aktualizuj bazy danych do najnowszych wersji.

Przykłady problemów i rozwiązań
Problem 1: Utrata klucza szyfrowania
  •	Opis: Zaszyfrowane dane są niemożliwe do odszyfrowania bez dostępu do klucza.
  •	Rozwiązanie:
    o	Przechowywanie klucza w bezpiecznym magazynie (np. HashiCorp Vault).
    o	Automatyczne kopie zapasowe klucza.
Problem 2: SQL Injection przy ręcznym formatowaniu zapytań
  •	Opis: Wstawianie danych użytkownika do zapytania za pomocą formatowania ciągów (np. f"SELECT ...").
  •	Rozwiązanie:
    o	Używanie zapytań z parametrami, które separują dane od kodu SQL.
    o	Wdrożenie ORM (np. Django ORM, SQLAlchemy), który automatycznie zabezpiecza przed wstrzyknięciami.
Problem 3: Atak przez brutalne siłowe łamanie klucza szyfrowania
  •	Opis: Przy słabym algorytmie szyfrowania klucz może być odgadnięty metodą brute-force.
  •	Rozwiązanie:
    o	Stosowanie algorytmów o wysokiej złożoności, takich jak AES-256.
    o	Generowanie kluczy z odpowiednią losowością (np. os.urandom).
