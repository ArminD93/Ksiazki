#! /usr/bin/env python3
# -*- coding: utf-8 -*-


from functions import *



def CheckGenre(genre):       
            if genre == "fantastyka":
                print("fantastyka");
                return True
                
            elif genre == "przygoda":
                print("przygoda");
                return True
            elif genre == "kryminal":
                print("kryminal");
                return True
            else:
                print("Wybierz jeden z trzech gatunków: przygoda, fantastyka, kryminal");




def warunek(genre, place_choice, hero_choice, time_choice, topic_choice, volume_choice):
    if genre == "fantastyka": 
        if place_choice == "miasto" or place_choice == "obojętnie" and hero_choice == "dziewczyna" or hero_choice == "obojętnie" and time_choice == "współczesne" or time_choice == "obojętnie" and topic_choice == "dystopia" or topic_choice == "obojętnie" and volume_choice < "5":
            print ("Wybrałeś fantastykę w Europie, gdzie bohaterem jest dziewczyna a akcja dzieje się w czasach współczesnych a tematem jest mitologia liczba tomów jest większa lub równa 5")
            hero = hero_choice;
            place = place_choice;
            time = time_choice;
            topic = topic_choice;
            volume = volume_choice;
            print();
            SearchInFantastykaTable(hero,place,time,topic, volume);
    
    if genre == "przygoda":
       if place_choice == "różne" and hero_choice == "chłopak" and time_choice == "współczesne" and topic_choice == "podróż" and volume_choice > "5":
       
            hero = hero_choice;
            place = place_choice;
            time = time_choice;
            topic = topic_choice;
            volume = volume_choice;
            print();
            SearchInPrzygodaTable(hero,place,time,topic,volume);
     
    if genre == "kryminal":
       if place_choice == "pociąg" and hero_choice == "wielu" and time_choice == "dawne" and topic_choice == "tajemnica" and volume_choice < "5":
       
            hero = hero_choice;
            place = place_choice;
            time = time_choice;
            topic = topic_choice;
            olume = volume_choice;
            print();
            SearchInKryminalTable(hero,place,time,topic,volume);
    else:
        print("Wybierz jeden z trzech gatunków: przygoda, fantastyka, kryminal");
      
      

print ("Witaj, ten program pomoże Tobie w wyborze książki ");
print ("######################################################");
print("");

while True:
   genre = input("Podaj nazwę gatunku, który Ciebie interesuje: ");
   print("");
   if CheckGenre(genre) == True: break




print("");

print ("dziewczyna  chłopak   kobieta        mężczyzna  wielu ");
print ("dzieci      postacie  fantastyczne   zwierzę    obojętnie");
print("-----------------------------------------------------------------------------------------");
hero_choice = input("Wybierz, kim ma być bohater ");

 
'''
    


print("");
print ("miasto  wymyślony świat   wyspy  pociąg ");
print ("Europa  łódź podwodna   statek   Ameryka Północna różne ");
print("-----------------------------------------------------------------------------------------");
place_choice = input("Podaj miejsce, które ma być zawarte w poszukiwanej książce ");
print("");
print ("współczesne     dawne               nieokreślone");
print("średniowiecze    postapokaliptyczne         różne");
print("-----------------------------------------------------------------------------------------");
time_choice = input("Napisz, w jakich czasach ma się dziać akcja ");
print("");
print ("podróż        przyjaźń     przeznaczenie  karykatura      mitologia     powrotu");
print("sprawiedliwość tajemnica    powrotu        dystopia        mafia         morderstwo");
print("-----------------------------------------------------------------------------------------");
topic_choice = input ("Jaki motyw powinien zostać poruszony ");
print("");
print("1   3   5   7   9   41  obojętnie")
print("-----------------------------------------------------------------------------------------");
volume_choice = input("Z ilu tomów ma się składać seria ");
print("");
'''



print("Oto Twój wybór, życzymy miłej lektury. ");

#warunek(genre,place_choice,hero_choice,time_choice,topic_choice,volume_choice);



con.close()

