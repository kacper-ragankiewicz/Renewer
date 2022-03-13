HOW TO: 

1. Pobierz projekt za pomocą git clone do folderu w którym ma się znajdować:


    cd <nazwa folderu>
    git clone https://github.com/kacper-ragankiewicz/Renewer.git 


2. Wejdź do folderu: 


    cd \Renewer 

2.1 Stawiamy nowe wirtualne środowisko inaczej interpreter. 

2.2 Instalujemy wszystkieg potrzebne paczki za pomocą: 

    pip install -r requirements.txt 

    ...lub...

    pip install <nazwa modułu> 


3. Sprawdz w /backend/settings.py nazwe użytkownika i bazy danych oraz hasło:
    

    DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'dog', <-- NAZWA
        'USER': 'hero', <-- UŻYTKOWNIK
        'PASSWORD': '1234', <-- HASŁO
        'HOST': 'localhost',
        'PORT': '5432',
    }


3.1 Jeśli nie posiadasz postawionej bazy danych o tej nazwie w postgresie, staiwamy za pomocą: 
    
    https://www.digitalocean.com/community/tutorials/how-to-use-postgresql-with-your-django-application-on-ubuntu-14-04

4. Kiedy mamy już podłączoną baze danych do projektu, używamy:
    

    python manage.py makemigrations

    python manage.py migrate 

W ten sposób migrujemy moduły do bazy danych.

5. Nastepnie odpalamy server za pomocą: 


    python manage.py runserver


6. Tworzymy admina do naszego projektu za pomocą: 
    

    python manage.py createsuperuser 

    < ... Podążamy za pytaniami, nie trzeba podawać maila >


7. Przechodzimy do przeglądarki na adress 127.0.0.1:8000

Wyświetla się panel do Admina, logujemy sie za pomocą podanych wczesnie danych. 

