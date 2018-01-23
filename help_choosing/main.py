#! /usr/bin/env python3
# -*- coding: utf-8 -*-


from functions import *




    


def warunek(genre, place_choice, hero_choice, time_choice, topic_choice, volume_choice):
    if genre == "fantastyka" and place_choice == "miasto" or place_choice == "obojętnie" and hero_choice == "dziewczyna" or hero_choice == "obojętnie" and time_choice == "współczesne" or time_choice == "obojętnie" and topic_choice == "dystopia" or topic_choice == "obojętnie" and volume_choice < "5":
        print ("Wybrałeś fantastykę w Europie, gdzie bohaterem jest dziewczyna a akcja dzieje się w czasach współczesnych a tematem jest mitologia liczba tomów jest większa lub równa 5")
        hero = hero_choice;
        place = place_choice;
        time = time_choice;
        topic = topic_choice;
        volume = volume_choice;
        print();
        SearchInFantastykaTable(hero,place,time,topic, volume);
        print(hero);
        print(place);
        print(time);
        print(topic);
        print(genre);
        print(volume);
    elif genre == "przygoda" and place_choice == "różne" and hero_choice == "chłopak" and time_choice == "współczesne" and topic_choice == "podróż" and volume_choice > "5":
       
        hero = hero_choice;
        place = place_choice;
        time = time_choice;
        topic = topic_choice;
        volume = volume_choice;
        print();
        SearchInPrzygodaTable(hero,place,time,topic,volume);
        print(hero);
        print(place);
        print(time);
        print(topic);
        print(genre);
        print(volume);
    elif genre == "kryminal" and place_choice == "pociąg" and hero_choice == "wielu" and time_choice == "dawne" and topic_choice == "tajemnica" and volume_choice < "5":
       
        hero = hero_choice;
        place = place_choice;
        time = time_choice;
        topic = topic_choice;
        volume = volume_choice;
        print();
        SearchInKryminalTable(hero,place,time,topic,volume);
        print(hero);
        print(place);
        print(time);
        print(topic);
        print(genre);
        print(volume);
      



print ("Witaj, ten program pomoże Tobie w wyborze książki ");
print ("######################################################");
print("");
genre = input("Podaj nazwę gatunku, który Ciebie interesuje: ");
print("");
print ("dziewczyna  chłopak   kobieta        mężczyzna  wielu ");
print ("dzieci      postacie  fantastyczne   zwierzę    obojętnie");
print("-------------------------------------------------------");
hero_choice = input("Wybierz, kim ma być bohater ");
print("");
place_choice = input("Podaj miejsce, które ma być zawarte w poszukiwanej książce ");
print("");
time_choice = input("Napisz, w jakich czasach ma się dziać akcja ");
print("");
topic_choice = input ("Jaki motyw powinien zostać poruszony ");
print("");
volume_choice = input("Z ilu tomów ma się składać seria ");
print("");




print("Oto Twój wybór, życzymy miłej lektury. ");

warunek(genre,place_choice,hero_choice,time_choice,topic_choice,volume_choice);

#SearchInFantastykaTable(hero,place,time,topic);

con.close()

