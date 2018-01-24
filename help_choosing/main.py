#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import os
from search import *
from check import *

def cls():
    os.system('cls' if os.name=='nt' else 'clear')



'''
def warunek(place_choice, hero_choice, time_choice, topic_choice, volume_choice):
    
   if hero_choice == "dziewczyna" or hero_choice == "obojętnie" and place_choice == "miasto" or place_choice == "obojętnie" and time_choice == "współczesne" or time_choice == "obojętnie" and topic_choice == "dystopia" or topic_choice == "obojętnie" and volume_choice == "3" or:
            
            hero = hero_choice;
            place = place_choice;
            time = time_choice;
            topic = topic_choice;
            volume = volume_choice;
            print();
            SearchInFantastykaTable(hero,place,time,topic, volume);
  '''  
    

      
      

print ("Witaj, ten program pomoże Tobie w wyborze książki ");
print ("######################################################");
print("");

while True:
   print("");
   print ("przygoda fantastyka kryminal obojętnie");
   print("");
   genre = input("Podaj nazwę gatunku, który Ciebie interesuje: ");
   print("");
   cls()
   if CheckGenre(genre) == True: break

if genre == "obojętnie":
   while True:
        print("-----------------------------------------------------------------------------------------");
        print ("dziewczyna  chłopak    wielu ");
        print ("zwierzę    obojętnie");
        print("-----------------------------------------------------------------------------------------");
        hero = input("Wybierz, kim ma być bohater ");
        cls()
        if CheckHero(hero) == True: break
   while True:
        print("-----------------------------------------------------------------------------------------");
        print ("miasto     Ameryka Północna      wyspy       pociąg ");
        print ("Europa      łódź podwodna       statek       różne    obojętnie");
        print("-----------------------------------------------------------------------------------------");
        place = input("Podaj miejsce, które ma być zawarte w poszukiwanej książce ");
        cls()
        if CheckPlace(place) == True: break
        print("");
   while True:
        print("-----------------------------------------------------------------------------------------");
        print ("współczesne     dawne          różne");
        print("nieokreślone     przyszłość     obojętnie");
        print("-----------------------------------------------------------------------------------------");
        time = input("Napisz, w jakich czasach ma się dziać akcja ");
        cls()
        if CheckTime(time) == True: break
        print("");
   while True:
        print("-----------------------------------------------------------------------------------------");
        print ("podróż        przyjaźń     przygody      przeznaczenie  karykatura      mitologia       ");
        print("sprawiedliwość tajemnica    powrotu        dystopia        mafia         morderstwo        obojętnie      ");
        print("-----------------------------------------------------------------------------------------");
        topic = input ("Jaki motyw powinien zostać poruszony ");
        cls()
        if CheckTopic(topic) == True: break
        print("");
   while True:
        print("-----------------------------------------------------------------------------------------");
        print("1   3   5   7   9   41  obojętnie")
        print("-----------------------------------------------------------------------------------------");
        volume = input("Z ilu tomów ma się składać seria ");
        cls()
        if CheckVolume(volume) == True: break
        print("");
   print("Oto Twój wybór z gatunku przygoda, życzymy miłej lektury. ");
   print("");
   SearchInPrzygodaTable(hero, place, time, topic, volume)

   print("Oto Twój wybór z gatunku fantastyka, życzymy miłej lektury. ");
   print("");
   SearchInFantastykaTable(hero, place, time, topic, volume)

   print("Oto Twój wybór z gatunku kryminał, życzymy miłej lektury. ");
   print("");
   SearchInKryminalTable(hero, place, time, topic, volume)

if genre == "przygoda":
    while True:
        print("-----------------------------------------------------------------------------------------");
        print ("dziewczyna  chłopak    wielu ");
        print ("zwierzę    obojętnie");
        print("-----------------------------------------------------------------------------------------");
        hero = input("Wybierz, kim ma być bohater ");
        cls()
        if CheckHero(hero) == True: break
    while True:
        print("-----------------------------------------------------------------------------------------");
        print ("Ameryka Północna    wyspy      różne   ");
        print ("łódź podwodna       statek   obojętnie");
        print("-----------------------------------------------------------------------------------------");
        place = input("Podaj miejsce, które ma być zawarte w poszukiwanej książce ");
        cls()
        if CheckPlace(place) == True: break
        print("");
    while True:
        print("-----------------------------------------------------------------------------------------");
        print ("współczesne     dawne ");
        print(" obojętnie");
        print("-----------------------------------------------------------------------------------------");
        time = input("Napisz, w jakich czasach ma się dziać akcja ");
        cls()
        if CheckTime(time) == True: break
        print("");
    while True:
        print("-----------------------------------------------------------------------------------------");
        print ("podróż        przyjaźń     przygody   ");
        print("obojętnie      ");
        print("-----------------------------------------------------------------------------------------");
        topic = input ("Jaki motyw powinien zostać poruszony ");
        cls()
        if CheckTopic(topic) == True: break
        print("");
    while True:
        print("-----------------------------------------------------------------------------------------");
        print("1  5  9  obojętnie");
        print("-----------------------------------------------------------------------------------------");
        volume = input("Z ilu tomów ma się składać seria ");
        cls()
        if CheckVolume(volume) == True: break
        print("");

    print("Oto Twój wybór z gatunku przygoda, życzymy miłej lektury. ");
    print("");
    SearchInPrzygodaTable(hero, place, time, topic, volume)

if genre == "fantastyka":
   while True:
        print("-----------------------------------------------------------------------------------------");
        print ("dziewczyna  chłopak    wielu ");
        print ("obojętnie");
        print("-----------------------------------------------------------------------------------------");
        hero = input("Wybierz, kim ma być bohater ");
        cls()
        if CheckHero(hero) == True: break
   while True:
        print("-----------------------------------------------------------------------------------------");
        print ("miasto   różne   ");
        print ("obojętnie");
        print("-----------------------------------------------------------------------------------------");
        place = input("Podaj miejsce, które ma być zawarte w poszukiwanej książce ");
        cls()
        if CheckPlace(place) == True: break
        print("");
   while True:
        print("-----------------------------------------------------------------------------------------");
        print ("współczesne     dawne   ");
        print(" nieokreślone    różne   obojętnie   ");
        print("-----------------------------------------------------------------------------------------");
        time = input("Napisz, w jakich czasach ma się dziać akcja ");
        cls()
        if CheckTime(time) == True: break
        print("");
   while True:
        print("-----------------------------------------------------------------------------------------");
        print ("przyjaźń       przygody     powrotu        mitologia       ");
        print(" różne          dystopia     przeznaczenie  karykatura   obojętnie    ");
        print("-----------------------------------------------------------------------------------------");
        topic = input ("Jaki motyw powinien zostać poruszony ");
        cls()
        if CheckTopic(topic) == True: break
        print("");
   while True:
        print("-----------------------------------------------------------------------------------------");
        print("1  3  5  7  41  obojętnie");
        print("-----------------------------------------------------------------------------------------");
        volume = input("Z ilu tomów ma się składać seria ");
        cls()
        if CheckVolume(volume) == True: break
        print("");

   print("Oto Twój wybór z gatunku fantastyka, życzymy miłej lektury. ");
   print("");
   SearchInFantastykaTable(hero, place, time, topic, volume)


if genre == "kryminal":
   while True:
        print("-----------------------------------------------------------------------------------------");
        print ("dziewczyna  chłopak    wielu ");
        print ("obojętnie");
        print("-----------------------------------------------------------------------------------------");
        hero = input("Wybierz, kim ma być bohater ");
        cls()
        if CheckHero(hero) == True: break
   while True:
        print("-----------------------------------------------------------------------------------------");
        print ("Europa       Ameryka Północna ");
        print ("pociąg       obojętnie");
        print("-----------------------------------------------------------------------------------------");
        place = input("Podaj miejsce, które ma być zawarte w poszukiwanej książce ");
        cls()
        if CheckPlace(place) == True: break
        print("");
   while True:
        print("-----------------------------------------------------------------------------------------");
        print ("współczesne     dawne   ");
        print(" obojętnie   ");
        print("-----------------------------------------------------------------------------------------");
        time = input("Napisz, w jakich czasach ma się dziać akcja ");
        cls()
        if CheckTime(time) == True: break
        print("");
   while True:
        print("-----------------------------------------------------------------------------------------");
        print ("sprawiedliwość       tajemnica          ");
        print(" morderstwo           mafia         obojętnie    ");
        print("-----------------------------------------------------------------------------------------");
        topic = input ("Jaki motyw powinien zostać poruszony ");
        cls()
        if CheckTopic(topic) == True: break
        print("");
 
   print("Oto Twój wybór z gatunku kryminał, życzymy miłej lektury. ");
   print("");
   SearchInKryminalTable(hero, place, time, topic, volume)





con.close()

