#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import sqlite3

# utworzenie połączenia z bazą przechowywaną na dysku
# lub w pamięci (':memory:')
con = sqlite3.connect('ksiazki.db')

# dostęp do kolumn przez indeksy i przez nazwy
con.row_factory = sqlite3.Row

# utworzenie obiektu kursora
cur = con.cursor()



# pobieranie danych z bazy
def czytajdane():
    """Funkcja pobiera i wyświetla dane z bazy."""
    cur.execute(
        """
        SELECT id,tytul,bohater,miejsce FROM fantastyka
        """)
    ksiazki = cur.fetchall()
    for pozycja in ksiazki:
        print(pozycja['id'], pozycja['tytul'], pozycja['bohater'], pozycja['miejsce'])
    print()

def czytajdane2():
    """Funkcja pobiera i wyświetla dane z bazy."""
    cur.execute(
        """
        SELECT id,tytul,bohater,miejsce FROM przygoda
        """)
    ksiazki = cur.fetchall()
    for pozycja in ksiazki:
        print(pozycja['id'], pozycja['tytul'], pozycja['bohater'], pozycja['miejsce'])
    print()

def czytajdane3():
    """Funkcja pobiera i wyświetla dane z bazy."""
    cur.execute(
        """
        SELECT id,tytul,bohater,miejsce FROM kryminal
        """)
    ksiazki = cur.fetchall()
    for pozycja in ksiazki:
        print(pozycja['id'], pozycja['tytul'], pozycja['bohater'], pozycja['miejsce'])
    print()
    


czytajdane()
czytajdane2()
czytajdane3()





con.close()

