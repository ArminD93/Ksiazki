#! /usr/bin/env python3
# -*- coding: utf-8 -*-


from functions import *




    


def warunek(genre, place, hero, time, topic, volume):
    if genre == "fantastyka" and place == "miasto" and hero == "dziewczyna" or hero == "obojętnie" and time == "współczesne" and topic == "dystopia" and volume < "5":
        print ("Wybrałeś fantastykę w Europie, gdzie bohaterem jest dziewczyna a akcja dzieje się w czasach współczesnych a tematem jest mitologia liczba tomów jest większa lub równa 5")
        SearchInFantastykaTable(hero,place,time,topic);

    elif genre == "przygoda" and place == "Ameryka Północna" and hero == "chłopak" and time == "dawne" and topic == "podróż" and volume < "5":
        print ("Wybrałeś przygodę w Ameryce, gdzie bohaterem jest chłopak a akcja dzieje się w czasach dawnych a tematem jest podróż liczba tomów jest mniejsza od 5")
        SearchInPrzygodaTable(hero,place,time,topic);
    elif genre == "kryminal" and place == "Ameryka Północna" and hero == "chłopak" and time == "dawne" and topic == "podróż" and volume < "5":
        print ("Wybrałeś przygodę w Ameryce, gdzie bohaterem jest chłopak a akcja dzieje się w czasach dawnych a tematem jest podróż liczba tomów jest mniejsza od 5")
        SearchInKryminalTable(hero,place,time,topic);
         



print ("Witaj, ten program pomoże Tobie w wyborze książki ");
print ("######################################################");
print("");
genre = input("Podaj nazwę gatunku, który Ciebie interesuje: ");
print("");
print ("dziewczyna  chłopak   kobieta        mężczyzna  wielu ");
print ("dzieci      postacie  fantastyczne   zwierzę    obojętnie");
print("-------------------------------------------------------");
hero = input("Wybierz, kim ma być bohater ");
print("");
place = input("Podaj miejsce, które ma być zawarte w poszukiwanej książce ");
print("");
time = input("Napisz, w jakich czasach ma się dziać akcja ");
print("");
topic = input ("Jaki motyw powinien zostać poruszony ");
print("");
volume = input("Z ilu tomów ma się składać seria ");
print("");




print("Oto Twój wybór, życzymy miłej lektury. ");

warunek(genre,place,hero,time,topic,volume);


con.close()

