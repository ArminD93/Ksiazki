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
        SELECT * FROM fantastyka
        """)
    ksiazki = cur.fetchall()
    for pozycja in ksiazki:
        print(pozycja['id'], pozycja['tytul'], pozycja['bohater'], pozycja['miejsce'])
    print()



def bohater(hero):
    cur.execute(
        """
        SELECT bohater FROM fantastyka  WHERE bohater = ?
        """, (hero,) )
    ksiazki = cur.fetchall()
    for pozycja in ksiazki:
        print(pozycja['bohater'])
   
    cur.execute(
        """
        SELECT bohater FROM przygoda WHERE bohater=?
        """, (hero,) )
    ksiazki = cur.fetchall()
    for pozycja in ksiazki:
        print(pozycja['bohater'])
    print()
    





print ("Witaj, ten program pomoże Tobie w wyborze książki ");
print ("######################################################");
#gatunek = input("Podaj numer gatunku, który Ciebie interesuje: ");

print ("Wybierz:");
print ("1:dziewczyna 2:chłopak 3:kobieta 4:mężczyzna");
print ("5:dzieci 6:postacie fantastyczne 7:wielu 8:zwierzę");
print();
hero_nr = input("Wybierz numer odpowiadający dla bohatera: ");


if hero_nr == 1:
    hero="dziewczyna";
elif hero_nr == 2:
    hero="chłopak";

print(hero);



#print("Oto Twój wybór, życzymy miłej lektury. ");

#bohater(hero)




con.close()

