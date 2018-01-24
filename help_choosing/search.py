import sqlite3

# utworzenie połączenia z bazą przechowywaną na dysku
# lub w pamięci (':memory:')
con = sqlite3.connect('ksiazki.db')

# dostęp do kolumn przez indeksy i przez nazwy
con.row_factory = sqlite3.Row

# utworzenie obiektu kursora
cur = con.cursor()



# pobieranie danych z bazy

def SearchInFantastykaTable(hero, place, time, topic, volume): 
    if hero == "obojętnie" and place == "obojętnie" and time == "obojętnie" and topic == "obojętnie" and volume == "obojętnie": #każdy parametr                                    = "obojętnie"
           cur.execute(
                        """
                        SELECT tytul, bohater, miejsce, czasy, motyw, liczba_tomow FROM fantastyka
                        """)
           ksiazki = cur.fetchall()
           for pozycja in ksiazki:
                print( pozycja['tytul'])
           print()
    elif hero == "obojętnie" and place == "obojętnie" and time == "obojętnie" and topic == "obojętnie":                         #parametr volume                                  != "obojętnie"
           cur.execute(
                        """
                        SELECT tytul, bohater, miejsce, czasy, motyw, liczba_tomow FROM fantastyka WHERE liczba_tomow = ? 
                        """, (volume, ))
           ksiazki = cur.fetchall()
           for pozycja in ksiazki:
                print(pozycja['tytul'])
           print()   
    elif hero == "obojętnie" and place == "obojętnie" and time == "obojętnie" and volume == "obojętnie":                        #parametr topic                                   != "obojętnie"
           cur.execute(
                        """
                        SELECT tytul, bohater, miejsce, czasy, motyw, liczba_tomow FROM fantastyka WHERE motyw = ? 
                        """, (topic,))
           ksiazki = cur.fetchall()
           for pozycja in ksiazki:
                print(pozycja['tytul'])
           print()  
    elif hero == "obojętnie" and place == "obojętnie" and topic == "obojętnie" and volume == "obojętnie":                       #parametr time                                    != "obojętnie"
           cur.execute(
                        """
                        SELECT tytul, bohater, miejsce, czasy, motyw, liczba_tomow FROM fantastyka WHERE czasy = ? 
                        """, (time,))
           ksiazki = cur.fetchall()
           for pozycja in ksiazki:
                print(pozycja['tytul'])
           print() 
    elif hero == "obojętnie" and time == "obojętnie"  and topic == "obojętnie" and volume == "obojętnie":                       #parametr place                                   != "obojętnie"
           cur.execute(
                        """
                        SELECT tytul, bohater, miejsce, czasy, motyw, liczba_tomow FROM fantastyka WHERE miejsce= ?
                        """, (place,))
           ksiazki = cur.fetchall()
           for pozycja in ksiazki:
                print(pozycja['tytul'])
           print()  

    elif place == "obojętnie" and time == "obojętnie"  and topic == "obojętnie" and volume == "obojętnie":                       #parametr hero                                    != "obojętnie"
           cur.execute(
                        """
                        SELECT tytul, bohater, miejsce, czasy, motyw, liczba_tomow FROM fantastyka WHERE bohater = ?
                        """, (hero,))
           ksiazki = cur.fetchall()
           for pozycja in ksiazki:
                print(pozycja['tytul'])
           print() 

   
    
    elif hero == "obojętnie"  and time == "obojętnie"  and volume == "obojętnie":                                               #parametr topic   && place                        != "obojętnie"
           cur.execute(
                        """
                        SELECT tytul, bohater, miejsce, czasy, motyw, liczba_tomow FROM fantastyka WHERE miejsce= ? AND  motyw= ?
                        """, (place, topic))
           ksiazki = cur.fetchall()
           for pozycja in ksiazki:
                print(pozycja['tytul'])
           print()     
    elif place == "obojętnie" and time == "obojętnie"  and topic == "obojętnie":                                                #parametr volume  && hero                         != "obojętnie"
           cur.execute(
                        """
                        SELECT tytul, bohater, miejsce, czasy, motyw, liczba_tomow FROM fantastyka WHERE miejsce= ? AND  motyw= ?
                        """, (place, topic ))
           ksiazki = cur.fetchall()
           for pozycja in ksiazki:
                print(pozycja['tytul'])
           print()   
    elif hero == "obojętnie" and time == "obojętnie"   and topic == "obojętnie":                                                #parametr volume  && place                        != "obojętnie"
           cur.execute(
                        """
                        SELECT tytul, bohater, miejsce, czasy, motyw, liczba_tomow FROM fantastyka WHERE miejsce= ? AND liczba_tomow =?
                        """, (place, volume))
           ksiazki = cur.fetchall()
           for pozycja in ksiazki:
                print(pozycja['tytul'])
           print()  
    elif hero == "obojętnie" and place == "obojętnie"  and topic == "obojętnie":                                                #parametr volume  && time                         != "obojętnie"
           cur.execute(
                        """
                        SELECT tytul, bohater, miejsce, czasy, motyw, liczba_tomow FROM fantastyka WHERE czasy= ? AND liczba_tomow =? 
                        """, (time, volume))
           ksiazki = cur.fetchall()
           for pozycja in ksiazki:
                print(pozycja['tytul'])
           print() 
    elif hero == "obojętnie" and place == "obojętnie"  and time == "obojętnie":                                                 #parametr volume  && topic                        != "obojętnie"
           cur.execute(
                        """
                        SELECT tytul, bohater, miejsce, czasy, motyw, liczba_tomow FROM fantastyka WHERE motyw= ? AND liczba_tomow =?
                        """, (topic, volume))
           ksiazki = cur.fetchall()
           for pozycja in ksiazki:
                print(pozycja['tytul'])
           print() 
    elif place == "obojętnie" and topic == "obojętnie" and volume == "obojętnie":                                               #parametr time    && hero                         != "obojętnie"
           cur.execute(
                        """
                        SELECT tytul, bohater, miejsce, czasy, motyw, liczba_tomow FROM fantastyka WHERE bohater= ? AND czasy= ?
                        """, (hero, time ))
           ksiazki = cur.fetchall()
           for pozycja in ksiazki:
                print(pozycja['tytul'] )
           print()   
    elif hero == "obojętnie" and topic == "obojętnie" and volume == "obojętnie":                                                #parametr time    && place                        != "obojętnie"
           cur.execute(
                        """
                        SELECT tytul, bohater, miejsce, czasy, motyw, liczba_tomow FROM fantastyka WHERE miejsce= ? AND czasy= ?
                        """, (place, time))
           ksiazki = cur.fetchall()
           for pozycja in ksiazki:
                print(pozycja['tytul'] )
           print()  
    elif hero == "obojętnie" and place == "obojętnie" and volume == "obojętnie":                                                #parametr time    && topic                        != "obojętnie"
           cur.execute(
                        """
                        SELECT tytul, bohater, miejsce, czasy, motyw, liczba_tomow FROM fantastyka WHERE  czasy= ? AND  motyw= ?
                        """, (time,topic))
           ksiazki = cur.fetchall()
           for pozycja in ksiazki:
                print(pozycja['tytul'] )
           print() 
    elif time == "obojętnie" and topic == "obojętnie" and volume == "obojętnie":                                                #parametr place   && hero                         != "obojętnie"
           cur.execute(
                        """
                        SELECT tytul, bohater, miejsce, czasy, motyw, liczba_tomow FROM fantastyka WHERE bohater= ? AND  miejsce= ?
                        """, (hero, place))
           ksiazki = cur.fetchall()
           for pozycja in ksiazki:
                print(pozycja['tytul'])
           print()       
    elif time == "obojętnie" and topic == "obojętnie" and volume == "obojętnie":                                                #parametr hero    && place                        != "obojętnie"
           cur.execute(
                        """
                        SELECT tytul, bohater, miejsce, czasy, motyw, liczba_tomow FROM fantastyka WHERE bohater= ? AND  miejsce= ? 
                        """, (hero, place ))
           ksiazki = cur.fetchall()
           for pozycja in ksiazki:
                print(pozycja['tytul'] )
           print()   
    elif place == "obojętnie" and time == "obojętnie" and volume == "obojętnie":                                                #parametr hero    && topic                        != "obojętnie"
           cur.execute(
                        """
                        SELECT tytul, bohater, miejsce, czasy, motyw, liczba_tomow FROM fantastyka WHERE bohater= ? AND motyw= ?  
                        """, (hero, topic))
           ksiazki = cur.fetchall()
           for pozycja in ksiazki:
                print(pozycja['tytul'] )
           print() 
    elif place == "obojętnie" and time == "obojętnie" and topic == "obojętnie":                                                 #parametr hero    && volume                       != "obojętnie"
           cur.execute(
                        """
                        SELECT tytul, bohater, miejsce, czasy, motyw, liczba_tomow FROM fantastyka WHERE bohater= ? AND liczba_tomow =?
                        """, (hero, volume))
           ksiazki = cur.fetchall()
           for pozycja in ksiazki:
                print(pozycja['tytul'] )
           print() 



    elif hero == "obojętnie"   and place == "obojętnie" :                                                                       #parametr topic   && volume  && time              != "obojętnie"
           cur.execute(
                        """
                        SELECT tytul, bohater, miejsce, czasy, motyw, liczba_tomow FROM fantastyka WHERE czasy= ? AND  motyw= ? AND liczba_tomow =?
                        """, (time,topic,volume ))
           ksiazki = cur.fetchall()
           for pozycja in ksiazki:
                print(pozycja['tytul'] )
           print()   
    elif time == "obojętnie"   and volume == "obojętnie":                                                                       #parametr topic   && hero    && place             != "obojętnie"
           cur.execute(
                        """
                        SELECT tytul, bohater, miejsce, czasy, motyw, liczba_tomow FROM fantastyka WHERE bohater= ? AND  miejsce= ? AND  motyw= ? 
                        """, (hero, place, topic))
           ksiazki = cur.fetchall()
           for pozycja in ksiazki:
                print(pozycja['tytul'] )
           print()  
    elif place == "obojętnie"  and time == "obojętnie":                                                                         #parametr topic   && hero    && volume            != "obojętnie"
           cur.execute(
                        """
                        SELECT tytul, bohater, miejsce, czasy, motyw, liczba_tomow FROM fantastyka WHERE bohater= ? AND  motyw= ? AND liczba_tomow =? 
                        """, (hero, topic, volume))
           ksiazki = cur.fetchall()
           for pozycja in ksiazki:
                print(pozycja['tytul'] )
           print() 
    elif hero == "obojętnie"   and volume == "obojętnie":                                                                       #parametr topic   && time    && place             != "obojętnie"
           cur.execute(
                        """
                        SELECT tytul, bohater, miejsce, czasy, motyw, liczba_tomow FROM fantastyka WHERE miejsce= ? AND czasy= ? AND  motyw= ? 
                        """, (place, time, topic))
           ksiazki = cur.fetchall()
           for pozycja in ksiazki:
                print(pozycja['tytul'] )
           print()  
    elif time == "obojętnie"   and topic == "obojętnie":                                                                        #parametr volume  && hero    && place             != "obojętnie"
           cur.execute(
                        """
                        SELECT tytul, bohater, miejsce, czasy, motyw, liczba_tomow FROM fantastyka WHERE bohater= ? AND  miejsce= ? AND liczba_tomow =? 
                        """, (hero, place, volume ))
           ksiazki = cur.fetchall()
           for pozycja in ksiazki:
                print(pozycja['tytul'] )
           print()   
    elif hero == "obojętnie"   and  topic == "obojętnie":                                                                       #parametr volume  && time    && place             != "obojętnie"
           cur.execute(
                        """
                        SELECT tytul, bohater, miejsce, czasy, motyw, liczba_tomow FROM fantastyka WHERE miejsce= ? AND czasy= ? AND liczba_tomow =?
                        """, (place, time, volume))
           ksiazki = cur.fetchall()
           for pozycja in ksiazki:
                print(pozycja['tytul'] )
           print()  
    elif hero == "obojętnie"   and  time == "obojętnie" :                                                                       #parametr volume  && place   && topic             != "obojętnie"
           cur.execute(
                        """
                        SELECT tytul, bohater, miejsce, czasy, motyw, liczba_tomow FROM fantastyka WHERE miejsce= ? AND  motyw= ? AND liczba_tomow =?
                        """, (place, topic, volume))
           ksiazki = cur.fetchall()
           for pozycja in ksiazki:
                print(pozycja['tytul'] )
           print() 
    elif place == "obojętnie"  and topic == "obojętnie":                                                                        #parametr volume  && time    && hero              != "obojętnie"
           cur.execute(
                        """
                        SELECT tytul, bohater, miejsce, czasy, motyw, liczba_tomow FROM fantastyka WHERE bohater= ? AND czasy= ? AND liczba_tomow =?
                        """, (hero, time, volume))
           ksiazki = cur.fetchall()
           for pozycja in ksiazki:
                print(pozycja['tytul'] )
           print() 
    elif topic == "obojętnie" and volume == "obojętnie":                                                                        #parametr time    && hero    && place             != "obojętnie"
           cur.execute(
                        """
                        SELECT tytul, bohater, miejsce, czasy, motyw, liczba_tomow FROM fantastyka WHERE bohater= ? AND  miejsce= ? AND czasy= ? 
                        """, (hero, place, time ))
           ksiazki = cur.fetchall()
           for pozycja in ksiazki:
                print(pozycja['tytul'] )
           print()   
    elif place == "obojętnie" and volume == "obojętnie":                                                                        #parametr time    && hero    && topic             != "obojętnie"
           cur.execute(
                        """
                        SELECT tytul, bohater, miejsce, czasy, motyw, liczba_tomow FROM fantastyka WHERE bohater= ?  AND czasy= ? AND  motyw= ?
                        """, (hero, time, topic))
           ksiazki = cur.fetchall()
           for pozycja in ksiazki:
                print(pozycja['tytul'] )
           print() 
    

    elif hero == "obojętnie":                                                                                                   #parametr place   && topic   && volume && time    != "obojętnie"
           cur.execute(
                        """
                        SELECT tytul, bohater, miejsce, czasy, motyw, liczba_tomow FROM fantastyka WHERE miejsce= ? AND czasy= ? AND  motyw= ? AND liczba_tomow =?
                        """, (place, time, topic, volume ))
           ksiazki = cur.fetchall()
           for pozycja in ksiazki:
                print(pozycja['tytul'] )
           print()   
    elif place == "obojętnie":                                                                                                  #parametr hero    && topic   && volume && time    != "obojętnie"
           cur.execute(
                        """
                        SELECT tytul, bohater, miejsce, czasy, motyw, liczba_tomow FROM fantastyka WHERE bohater= ? AND czasy= ? AND  motyw= ? AND liczba_tomow =?
                        """, (hero, time, topic, volume))
           ksiazki = cur.fetchall()
           for pozycja in ksiazki:
                print(pozycja['tytul'] )
           print()  
    elif time == "obojętnie" :                                                                                                  #parametr hero    && place   && topic && volume   != "obojętnie"
           cur.execute(
                        """
                        SELECT tytul, bohater, miejsce, czasy, motyw, liczba_tomow FROM fantastyka WHERE bohater= ? AND  miejsce= ? AND  motyw= ? AND liczba_tomow =? 
                        """, (hero, place, topic, volume))
           ksiazki = cur.fetchall()
           for pozycja in ksiazki:
                print(pozycja['tytul'] )
           print() 
    elif topic == "obojętnie":                                                                                                  #parametr hero    && place   && volume && time    != "obojętnie"
           cur.execute(
                        """
                        SELECT tytul, bohater, miejsce, czasy, motyw, liczba_tomow FROM fantastyka WHERE bohater= ? AND  miejsce= ? AND czasy= ?  AND liczba_tomow =?
                        """, (hero, place, time, volume))
           ksiazki = cur.fetchall()
           for pozycja in ksiazki:
                print(pozycja['tytul'] )
           print() 
    elif volume == "obojętnie":                                                                                                 #parametr hero    && place   && topic && time     != "obojętnie"
           cur.execute(
                        """
                        SELECT tytul, bohater, miejsce, czasy, motyw, liczba_tomow FROM fantastyka WHERE bohater= ? AND  miejsce= ? AND czasy= ? AND  motyw= ? 
                        """, (hero, place, time, topic ))
           ksiazki = cur.fetchall()
           for pozycja in ksiazki:
                print(pozycja['tytul'] )
           print()  
           
   

    else:                                                                                #wszystkie parametry dowolne                                                                                
           cur.execute(
                        """
                        SELECT tytul, bohater, miejsce, czasy, motyw, liczba_tomow FROM fantastyka WHERE bohater= ? AND  miejsce= ? AND czasy= ? AND  motyw= ? AND liczba_tomow =?
                        """, (hero, place, time, topic, volume))
           ksiazki = cur.fetchall()
           for pozycja in ksiazki:
                print(pozycja['tytul'] )
           print()  




def SearchInPrzygodaTable(hero, place, time, topic, volume): 
    if hero == "obojętnie" and place == "obojętnie" and time == "obojętnie" and topic == "obojętnie" and volume == "obojętnie": #każdy parametr                                    = "obojętnie"
           cur.execute(
                        """
                        SELECT tytul, bohater, miejsce, czasy, motyw, liczba_tomow FROM przygoda
                        """)
           ksiazki = cur.fetchall()
           for pozycja in ksiazki:
                print( pozycja['tytul'])
           print()
    elif hero == "obojętnie" and place == "obojętnie" and time == "obojętnie" and topic == "obojętnie":                         #parametr volume                                  != "obojętnie"
           cur.execute(
                        """
                        SELECT tytul, bohater, miejsce, czasy, motyw, liczba_tomow FROM przygoda WHERE liczba_tomow = ? 
                        """, (volume, ))
           ksiazki = cur.fetchall()
           for pozycja in ksiazki:
                print(pozycja['tytul'])
           print()   
    elif hero == "obojętnie" and place == "obojętnie" and time == "obojętnie" and volume == "obojętnie":                        #parametr topic                                   != "obojętnie"
           cur.execute(
                        """
                        SELECT tytul, bohater, miejsce, czasy, motyw, liczba_tomow FROM przygoda WHERE motyw = ? 
                        """, (topic,))
           ksiazki = cur.fetchall()
           for pozycja in ksiazki:
                print(pozycja['tytul'])
           print()  
    elif hero == "obojętnie" and place == "obojętnie" and topic == "obojętnie" and volume == "obojętnie":                       #parametr time                                    != "obojętnie"
           cur.execute(
                        """
                        SELECT tytul, bohater, miejsce, czasy, motyw, liczba_tomow FROM przygoda WHERE czasy = ? 
                        """, (time,))
           ksiazki = cur.fetchall()
           for pozycja in ksiazki:
                print(pozycja['tytul'])
           print() 
    elif hero == "obojętnie" and time == "obojętnie"  and topic == "obojętnie" and volume == "obojętnie":                       #parametr place                                   != "obojętnie"
           cur.execute(
                        """
                        SELECT tytul, bohater, miejsce, czasy, motyw, liczba_tomow FROM przygoda WHERE miejsce= ?
                        """, (place,))
           ksiazki = cur.fetchall()
           for pozycja in ksiazki:
                print(pozycja['tytul'])
           print()  

    elif place == "obojętnie" and time == "obojętnie"  and topic == "obojętnie" and volume == "obojętnie":                       #parametr hero                                    != "obojętnie"
           cur.execute(
                        """
                        SELECT tytul, bohater, miejsce, czasy, motyw, liczba_tomow FROM przygoda WHERE bohater = ?
                        """, (hero,))
           ksiazki = cur.fetchall()
           for pozycja in ksiazki:
                print(pozycja['tytul'])
           print() 

   
    
    elif hero == "obojętnie"  and time == "obojętnie"  and volume == "obojętnie":                                               #parametr topic   && place                        != "obojętnie"
           cur.execute(
                        """
                        SELECT tytul, bohater, miejsce, czasy, motyw, liczba_tomow FROM przygoda WHERE miejsce= ? AND  motyw= ?
                        """, (place, topic))
           ksiazki = cur.fetchall()
           for pozycja in ksiazki:
                print(pozycja['tytul'])
           print()     
    elif place == "obojętnie" and time == "obojętnie"  and topic == "obojętnie":                                                #parametr volume  && hero                         != "obojętnie"
           cur.execute(
                        """
                        SELECT tytul, bohater, miejsce, czasy, motyw, liczba_tomow FROM przygoda WHERE miejsce= ? AND  motyw= ?
                        """, (place, topic ))
           ksiazki = cur.fetchall()
           for pozycja in ksiazki:
                print(pozycja['tytul'])
           print()   
    elif hero == "obojętnie" and time == "obojętnie"   and topic == "obojętnie":                                                #parametr volume  && place                        != "obojętnie"
           cur.execute(
                        """
                        SELECT tytul, bohater, miejsce, czasy, motyw, liczba_tomow FROM przygoda WHERE miejsce= ? AND liczba_tomow =?
                        """, (place, volume))
           ksiazki = cur.fetchall()
           for pozycja in ksiazki:
                print(pozycja['tytul'])
           print()  
    elif hero == "obojętnie" and place == "obojętnie"  and topic == "obojętnie":                                                #parametr volume  && time                         != "obojętnie"
           cur.execute(
                        """
                        SELECT tytul, bohater, miejsce, czasy, motyw, liczba_tomow FROM przygoda WHERE czasy= ? AND liczba_tomow =? 
                        """, (time, volume))
           ksiazki = cur.fetchall()
           for pozycja in ksiazki:
                print(pozycja['tytul'])
           print() 
    elif hero == "obojętnie" and place == "obojętnie"  and time == "obojętnie":                                                 #parametr volume  && topic                        != "obojętnie"
           cur.execute(
                        """
                        SELECT tytul, bohater, miejsce, czasy, motyw, liczba_tomow FROM przygoda WHERE motyw= ? AND liczba_tomow =?
                        """, (topic, volume))
           ksiazki = cur.fetchall()
           for pozycja in ksiazki:
                print(pozycja['tytul'])
           print() 
    elif place == "obojętnie" and topic == "obojętnie" and volume == "obojętnie":                                               #parametr time    && hero                         != "obojętnie"
           cur.execute(
                        """
                        SELECT tytul, bohater, miejsce, czasy, motyw, liczba_tomow FROM przygoda WHERE bohater= ? AND czasy= ?
                        """, (hero, time ))
           ksiazki = cur.fetchall()
           for pozycja in ksiazki:
                print(pozycja['tytul'] )
           print()   
    elif hero == "obojętnie" and topic == "obojętnie" and volume == "obojętnie":                                                #parametr time    && place                        != "obojętnie"
           cur.execute(
                        """
                        SELECT tytul, bohater, miejsce, czasy, motyw, liczba_tomow FROM przygoda WHERE miejsce= ? AND czasy= ?
                        """, (place, time))
           ksiazki = cur.fetchall()
           for pozycja in ksiazki:
                print(pozycja['tytul'] )
           print()  
    elif hero == "obojętnie" and place == "obojętnie" and volume == "obojętnie":                                                #parametr time    && topic                        != "obojętnie"
           cur.execute(
                        """
                        SELECT tytul, bohater, miejsce, czasy, motyw, liczba_tomow FROM przygoda WHERE  czasy= ? AND  motyw= ?
                        """, (time,topic))
           ksiazki = cur.fetchall()
           for pozycja in ksiazki:
                print(pozycja['tytul'] )
           print() 
    elif time == "obojętnie" and topic == "obojętnie" and volume == "obojętnie":                                                #parametr place   && hero                         != "obojętnie"
           cur.execute(
                        """
                        SELECT tytul, bohater, miejsce, czasy, motyw, liczba_tomow FROM przygoda WHERE bohater= ? AND  miejsce= ?
                        """, (hero, place))
           ksiazki = cur.fetchall()
           for pozycja in ksiazki:
                print(pozycja['tytul'])
           print()       
    elif time == "obojętnie" and topic == "obojętnie" and volume == "obojętnie":                                                #parametr hero    && place                        != "obojętnie"
           cur.execute(
                        """
                        SELECT tytul, bohater, miejsce, czasy, motyw, liczba_tomow FROM przygoda WHERE bohater= ? AND  miejsce= ? 
                        """, (hero, place ))
           ksiazki = cur.fetchall()
           for pozycja in ksiazki:
                print(pozycja['tytul'] )
           print()   
    elif place == "obojętnie" and time == "obojętnie" and volume == "obojętnie":                                                #parametr hero    && topic                        != "obojętnie"
           cur.execute(
                        """
                        SELECT tytul, bohater, miejsce, czasy, motyw, liczba_tomow FROM przygoda WHERE bohater= ? AND motyw= ?  
                        """, (hero, topic))
           ksiazki = cur.fetchall()
           for pozycja in ksiazki:
                print(pozycja['tytul'] )
           print() 
    elif place == "obojętnie" and time == "obojętnie" and topic == "obojętnie":                                                 #parametr hero    && volume                       != "obojętnie"
           cur.execute(
                        """
                        SELECT tytul, bohater, miejsce, czasy, motyw, liczba_tomow FROM przygoda WHERE bohater= ? AND liczba_tomow =?
                        """, (hero, volume))
           ksiazki = cur.fetchall()
           for pozycja in ksiazki:
                print(pozycja['tytul'] )
           print() 



    elif hero == "obojętnie"   and place == "obojętnie" :                                                                       #parametr topic   && volume  && time              != "obojętnie"
           cur.execute(
                        """
                        SELECT tytul, bohater, miejsce, czasy, motyw, liczba_tomow FROM przygoda WHERE czasy= ? AND  motyw= ? AND liczba_tomow =?
                        """, (time,topic,volume ))
           ksiazki = cur.fetchall()
           for pozycja in ksiazki:
                print(pozycja['tytul'] )
           print()   
    elif time == "obojętnie"   and volume == "obojętnie":                                                                       #parametr topic   && hero    && place             != "obojętnie"
           cur.execute(
                        """
                        SELECT tytul, bohater, miejsce, czasy, motyw, liczba_tomow FROM przygoda WHERE bohater= ? AND  miejsce= ? AND  motyw= ? 
                        """, (hero, place, topic))
           ksiazki = cur.fetchall()
           for pozycja in ksiazki:
                print(pozycja['tytul'] )
           print()  
    elif place == "obojętnie"  and time == "obojętnie":                                                                         #parametr topic   && hero    && volume            != "obojętnie"
           cur.execute(
                        """
                        SELECT tytul, bohater, miejsce, czasy, motyw, liczba_tomow FROM przygoda WHERE bohater= ? AND  motyw= ? AND liczba_tomow =? 
                        """, (hero, topic, volume))
           ksiazki = cur.fetchall()
           for pozycja in ksiazki:
                print(pozycja['tytul'] )
           print() 
    elif hero == "obojętnie"   and volume == "obojętnie":                                                                       #parametr topic   && time    && place             != "obojętnie"
           cur.execute(
                        """
                        SELECT tytul, bohater, miejsce, czasy, motyw, liczba_tomow FROM przygoda WHERE miejsce= ? AND czasy= ? AND  motyw= ? 
                        """, (place, time, topic))
           ksiazki = cur.fetchall()
           for pozycja in ksiazki:
                print(pozycja['tytul'] )
           print()  
    elif time == "obojętnie"   and topic == "obojętnie":                                                                        #parametr volume  && hero    && place             != "obojętnie"
           cur.execute(
                        """
                        SELECT tytul, bohater, miejsce, czasy, motyw, liczba_tomow FROM przygoda WHERE bohater= ? AND  miejsce= ? AND liczba_tomow =? 
                        """, (hero, place, volume ))
           ksiazki = cur.fetchall()
           for pozycja in ksiazki:
                print(pozycja['tytul'] )
           print()   
    elif hero == "obojętnie"   and  topic == "obojętnie":                                                                       #parametr volume  && time    && place             != "obojętnie"
           cur.execute(
                        """
                        SELECT tytul, bohater, miejsce, czasy, motyw, liczba_tomow FROM przygoda WHERE miejsce= ? AND czasy= ? AND liczba_tomow =?
                        """, (place, time, volume))
           ksiazki = cur.fetchall()
           for pozycja in ksiazki:
                print(pozycja['tytul'] )
           print()  
    elif hero == "obojętnie"   and  time == "obojętnie" :                                                                       #parametr volume  && place   && topic             != "obojętnie"
           cur.execute(
                        """
                        SELECT tytul, bohater, miejsce, czasy, motyw, liczba_tomow FROM przygoda WHERE miejsce= ? AND  motyw= ? AND liczba_tomow =?
                        """, (place, topic, volume))
           ksiazki = cur.fetchall()
           for pozycja in ksiazki:
                print(pozycja['tytul'] )
           print() 
    elif place == "obojętnie"  and topic == "obojętnie":                                                                        #parametr volume  && time    && hero              != "obojętnie"
           cur.execute(
                        """
                        SELECT tytul, bohater, miejsce, czasy, motyw, liczba_tomow FROM przygoda WHERE bohater= ? AND czasy= ? AND liczba_tomow =?
                        """, (hero, time, volume))
           ksiazki = cur.fetchall()
           for pozycja in ksiazki:
                print(pozycja['tytul'] )
           print() 
    elif topic == "obojętnie" and volume == "obojętnie":                                                                        #parametr time    && hero    && place             != "obojętnie"
           cur.execute(
                        """
                        SELECT tytul, bohater, miejsce, czasy, motyw, liczba_tomow FROM przygoda WHERE bohater= ? AND  miejsce= ? AND czasy= ? 
                        """, (hero, place, time ))
           ksiazki = cur.fetchall()
           for pozycja in ksiazki:
                print(pozycja['tytul'] )
           print()   
    elif place == "obojętnie" and volume == "obojętnie":                                                                        #parametr time    && hero    && topic             != "obojętnie"
           cur.execute(
                        """
                        SELECT tytul, bohater, miejsce, czasy, motyw, liczba_tomow FROM przygoda WHERE bohater= ?  AND czasy= ? AND  motyw= ?
                        """, (hero, time, topic))
           ksiazki = cur.fetchall()
           for pozycja in ksiazki:
                print(pozycja['tytul'] )
           print() 
    

    elif hero == "obojętnie":                                                                                                   #parametr place   && topic   && volume && time    != "obojętnie"
           cur.execute(
                        """
                        SELECT tytul, bohater, miejsce, czasy, motyw, liczba_tomow FROM przygoda WHERE miejsce= ? AND czasy= ? AND  motyw= ? AND liczba_tomow =?
                        """, (place, time, topic, volume ))
           ksiazki = cur.fetchall()
           for pozycja in ksiazki:
                print(pozycja['tytul'] )
           print()   
    elif place == "obojętnie":                                                                                                  #parametr hero    && topic   && volume && time    != "obojętnie"
           cur.execute(
                        """
                        SELECT tytul, bohater, miejsce, czasy, motyw, liczba_tomow FROM przygoda WHERE bohater= ? AND czasy= ? AND  motyw= ? AND liczba_tomow =?
                        """, (hero, time, topic, volume))
           ksiazki = cur.fetchall()
           for pozycja in ksiazki:
                print(pozycja['tytul'] )
           print()  
    elif time == "obojętnie" :                                                                                                  #parametr hero    && place   && topic && volume   != "obojętnie"
           cur.execute(
                        """
                        SELECT tytul, bohater, miejsce, czasy, motyw, liczba_tomow FROM przygoda WHERE bohater= ? AND  miejsce= ? AND  motyw= ? AND liczba_tomow =? 
                        """, (hero, place, topic, volume))
           ksiazki = cur.fetchall()
           for pozycja in ksiazki:
                print(pozycja['tytul'] )
           print() 
    elif topic == "obojętnie":                                                                                                  #parametr hero    && place   && volume && time    != "obojętnie"
           cur.execute(
                        """
                        SELECT tytul, bohater, miejsce, czasy, motyw, liczba_tomow FROM przygoda WHERE bohater= ? AND  miejsce= ? AND czasy= ?  AND liczba_tomow =?
                        """, (hero, place, time, volume))
           ksiazki = cur.fetchall()
           for pozycja in ksiazki:
                print(pozycja['tytul'] )
           print() 
    elif volume == "obojętnie":                                                                                                 #parametr hero    && place   && topic && time     != "obojętnie"
           cur.execute(
                        """
                        SELECT tytul, bohater, miejsce, czasy, motyw, liczba_tomow FROM przygoda WHERE bohater= ? AND  miejsce= ? AND czasy= ? AND  motyw= ? 
                        """, (hero, place, time, topic ))
           ksiazki = cur.fetchall()
           for pozycja in ksiazki:
                print(pozycja['tytul'] )
           print()  
           
   

    else:                                                                                #wszystkie parametry dowolne                                                                                
           cur.execute(
                        """
                        SELECT tytul, bohater, miejsce, czasy, motyw, liczba_tomow FROM przygoda WHERE bohater= ? AND  miejsce= ? AND czasy= ? AND  motyw= ? AND liczba_tomow =?
                        """, (hero, place, time, topic, volume))
           ksiazki = cur.fetchall()
           for pozycja in ksiazki:
                print(pozycja['tytul'] )
           print()  




def SearchInKryminalTable(hero, place, time, topic, volume): 
    if hero == "obojętnie" and place == "obojętnie" and time == "obojętnie" and topic == "obojętnie" and volume == "obojętnie": #każdy parametr                                    = "obojętnie"
           cur.execute(
                        """
                        SELECT tytul, bohater, miejsce, czasy, motyw, liczba_tomow FROM kryminal
                        """)
           ksiazki = cur.fetchall()
           for pozycja in ksiazki:
                print( pozycja['tytul'])
           print()
    elif hero == "obojętnie" and place == "obojętnie" and time == "obojętnie" and topic == "obojętnie":                         #parametr volume                                  != "obojętnie"
           cur.execute(
                        """
                        SELECT tytul, bohater, miejsce, czasy, motyw, liczba_tomow FROM kryminal WHERE liczba_tomow = ? 
                        """, (volume, ))
           ksiazki = cur.fetchall()
           for pozycja in ksiazki:
                print(pozycja['tytul'])
           print()   
    elif hero == "obojętnie" and place == "obojętnie" and time == "obojętnie" and volume == "obojętnie":                        #parametr topic                                   != "obojętnie"
           cur.execute(
                        """
                        SELECT tytul, bohater, miejsce, czasy, motyw, liczba_tomow FROM kryminal WHERE motyw = ? 
                        """, (topic,))
           ksiazki = cur.fetchall()
           for pozycja in ksiazki:
                print(pozycja['tytul'])
           print()  
    elif hero == "obojętnie" and place == "obojętnie" and topic == "obojętnie" and volume == "obojętnie":                       #parametr time                                    != "obojętnie"
           cur.execute(
                        """
                        SELECT tytul, bohater, miejsce, czasy, motyw, liczba_tomow FROM kryminal WHERE czasy = ? 
                        """, (time,))
           ksiazki = cur.fetchall()
           for pozycja in ksiazki:
                print(pozycja['tytul'])
           print() 
    elif hero == "obojętnie" and time == "obojętnie"  and topic == "obojętnie" and volume == "obojętnie":                       #parametr place                                   != "obojętnie"
           cur.execute(
                        """
                        SELECT tytul, bohater, miejsce, czasy, motyw, liczba_tomow FROM kryminal WHERE miejsce= ?
                        """, (place,))
           ksiazki = cur.fetchall()
           for pozycja in ksiazki:
                print(pozycja['tytul'])
           print()  

    elif place == "obojętnie" and time == "obojętnie"  and topic == "obojętnie" and volume == "obojętnie":                       #parametr hero                                    != "obojętnie"
           cur.execute(
                        """
                        SELECT tytul, bohater, miejsce, czasy, motyw, liczba_tomow FROM kryminal WHERE bohater = ?
                        """, (hero,))
           ksiazki = cur.fetchall()
           for pozycja in ksiazki:
                print(pozycja['tytul'])
           print() 

   
    
    elif hero == "obojętnie"  and time == "obojętnie"  and volume == "obojętnie":                                               #parametr topic   && place                        != "obojętnie"
           cur.execute(
                        """
                        SELECT tytul, bohater, miejsce, czasy, motyw, liczba_tomow FROM kryminal WHERE miejsce= ? AND  motyw= ?
                        """, (place, topic))
           ksiazki = cur.fetchall()
           for pozycja in ksiazki:
                print(pozycja['tytul'])
           print()     
    elif place == "obojętnie" and time == "obojętnie"  and topic == "obojętnie":                                                #parametr volume  && hero                         != "obojętnie"
           cur.execute(
                        """
                        SELECT tytul, bohater, miejsce, czasy, motyw, liczba_tomow FROM kryminal WHERE miejsce= ? AND  motyw= ?
                        """, (place, topic ))
           ksiazki = cur.fetchall()
           for pozycja in ksiazki:
                print(pozycja['tytul'])
           print()   
    elif hero == "obojętnie" and time == "obojętnie"   and topic == "obojętnie":                                                #parametr volume  && place                        != "obojętnie"
           cur.execute(
                        """
                        SELECT tytul, bohater, miejsce, czasy, motyw, liczba_tomow FROM kryminal WHERE miejsce= ? AND liczba_tomow =?
                        """, (place, volume))
           ksiazki = cur.fetchall()
           for pozycja in ksiazki:
                print(pozycja['tytul'])
           print()  
    elif hero == "obojętnie" and place == "obojętnie"  and topic == "obojętnie":                                                #parametr volume  && time                         != "obojętnie"
           cur.execute(
                        """
                        SELECT tytul, bohater, miejsce, czasy, motyw, liczba_tomow FROM kryminal WHERE czasy= ? AND liczba_tomow =? 
                        """, (time, volume))
           ksiazki = cur.fetchall()
           for pozycja in ksiazki:
                print(pozycja['tytul'])
           print() 
    elif hero == "obojętnie" and place == "obojętnie"  and time == "obojętnie":                                                 #parametr volume  && topic                        != "obojętnie"
           cur.execute(
                        """
                        SELECT tytul, bohater, miejsce, czasy, motyw, liczba_tomow FROM kryminal WHERE motyw= ? AND liczba_tomow =?
                        """, (topic, volume))
           ksiazki = cur.fetchall()
           for pozycja in ksiazki:
                print(pozycja['tytul'])
           print() 
    elif place == "obojętnie" and topic == "obojętnie" and volume == "obojętnie":                                               #parametr time    && hero                         != "obojętnie"
           cur.execute(
                        """
                        SELECT tytul, bohater, miejsce, czasy, motyw, liczba_tomow FROM kryminal WHERE bohater= ? AND czasy= ?
                        """, (hero, time ))
           ksiazki = cur.fetchall()
           for pozycja in ksiazki:
                print(pozycja['tytul'] )
           print()   
    elif hero == "obojętnie" and topic == "obojętnie" and volume == "obojętnie":                                                #parametr time    && place                        != "obojętnie"
           cur.execute(
                        """
                        SELECT tytul, bohater, miejsce, czasy, motyw, liczba_tomow FROM kryminal WHERE miejsce= ? AND czasy= ?
                        """, (place, time))
           ksiazki = cur.fetchall()
           for pozycja in ksiazki:
                print(pozycja['tytul'] )
           print()  
    elif hero == "obojętnie" and place == "obojętnie" and volume == "obojętnie":                                                #parametr time    && topic                        != "obojętnie"
           cur.execute(
                        """
                        SELECT tytul, bohater, miejsce, czasy, motyw, liczba_tomow FROM kryminal WHERE  czasy= ? AND  motyw= ?
                        """, (time,topic))
           ksiazki = cur.fetchall()
           for pozycja in ksiazki:
                print(pozycja['tytul'] )
           print() 
    elif time == "obojętnie" and topic == "obojętnie" and volume == "obojętnie":                                                #parametr place   && hero                         != "obojętnie"
           cur.execute(
                        """
                        SELECT tytul, bohater, miejsce, czasy, motyw, liczba_tomow FROM kryminal WHERE bohater= ? AND  miejsce= ?
                        """, (hero, place))
           ksiazki = cur.fetchall()
           for pozycja in ksiazki:
                print(pozycja['tytul'])
           print()       
    elif time == "obojętnie" and topic == "obojętnie" and volume == "obojętnie":                                                #parametr hero    && place                        != "obojętnie"
           cur.execute(
                        """
                        SELECT tytul, bohater, miejsce, czasy, motyw, liczba_tomow FROM kryminal WHERE bohater= ? AND  miejsce= ? 
                        """, (hero, place ))
           ksiazki = cur.fetchall()
           for pozycja in ksiazki:
                print(pozycja['tytul'] )
           print()   
    elif place == "obojętnie" and time == "obojętnie" and volume == "obojętnie":                                                #parametr hero    && topic                        != "obojętnie"
           cur.execute(
                        """
                        SELECT tytul, bohater, miejsce, czasy, motyw, liczba_tomow FROM kryminal WHERE bohater= ? AND motyw= ?  
                        """, (hero, topic))
           ksiazki = cur.fetchall()
           for pozycja in ksiazki:
                print(pozycja['tytul'] )
           print() 
    elif place == "obojętnie" and time == "obojętnie" and topic == "obojętnie":                                                 #parametr hero    && volume                       != "obojętnie"
           cur.execute(
                        """
                        SELECT tytul, bohater, miejsce, czasy, motyw, liczba_tomow FROM kryminal WHERE bohater= ? AND liczba_tomow =?
                        """, (hero, volume))
           ksiazki = cur.fetchall()
           for pozycja in ksiazki:
                print(pozycja['tytul'] )
           print() 



    elif hero == "obojętnie"   and place == "obojętnie" :                                                                       #parametr topic   && volume  && time              != "obojętnie"
           cur.execute(
                        """
                        SELECT tytul, bohater, miejsce, czasy, motyw, liczba_tomow FROM kryminal WHERE czasy= ? AND  motyw= ? AND liczba_tomow =?
                        """, (time,topic,volume ))
           ksiazki = cur.fetchall()
           for pozycja in ksiazki:
                print(pozycja['tytul'] )
           print()   
    elif time == "obojętnie"   and volume == "obojętnie":                                                                       #parametr topic   && hero    && place             != "obojętnie"
           cur.execute(
                        """
                        SELECT tytul, bohater, miejsce, czasy, motyw, liczba_tomow FROM kryminal WHERE bohater= ? AND  miejsce= ? AND  motyw= ? 
                        """, (hero, place, topic))
           ksiazki = cur.fetchall()
           for pozycja in ksiazki:
                print(pozycja['tytul'] )
           print()  
    elif place == "obojętnie"  and time == "obojętnie":                                                                         #parametr topic   && hero    && volume            != "obojętnie"
           cur.execute(
                        """
                        SELECT tytul, bohater, miejsce, czasy, motyw, liczba_tomow FROM kryminal WHERE bohater= ? AND  motyw= ? AND liczba_tomow =? 
                        """, (hero, topic, volume))
           ksiazki = cur.fetchall()
           for pozycja in ksiazki:
                print(pozycja['tytul'] )
           print() 
    elif hero == "obojętnie"   and volume == "obojętnie":                                                                       #parametr topic   && time    && place             != "obojętnie"
           cur.execute(
                        """
                        SELECT tytul, bohater, miejsce, czasy, motyw, liczba_tomow FROM kryminal WHERE miejsce= ? AND czasy= ? AND  motyw= ? 
                        """, (place, time, topic))
           ksiazki = cur.fetchall()
           for pozycja in ksiazki:
                print(pozycja['tytul'] )
           print()  
    elif time == "obojętnie"   and topic == "obojętnie":                                                                        #parametr volume  && hero    && place             != "obojętnie"
           cur.execute(
                        """
                        SELECT tytul, bohater, miejsce, czasy, motyw, liczba_tomow FROM kryminal WHERE bohater= ? AND  miejsce= ? AND liczba_tomow =? 
                        """, (hero, place, volume ))
           ksiazki = cur.fetchall()
           for pozycja in ksiazki:
                print(pozycja['tytul'] )
           print()   
    elif hero == "obojętnie"   and  topic == "obojętnie":                                                                       #parametr volume  && time    && place             != "obojętnie"
           cur.execute(
                        """
                        SELECT tytul, bohater, miejsce, czasy, motyw, liczba_tomow FROM kryminal WHERE miejsce= ? AND czasy= ? AND liczba_tomow =?
                        """, (place, time, volume))
           ksiazki = cur.fetchall()
           for pozycja in ksiazki:
                print(pozycja['tytul'] )
           print()  
    elif hero == "obojętnie"   and  time == "obojętnie" :                                                                       #parametr volume  && place   && topic             != "obojętnie"
           cur.execute(
                        """
                        SELECT tytul, bohater, miejsce, czasy, motyw, liczba_tomow FROM kryminal WHERE miejsce= ? AND  motyw= ? AND liczba_tomow =?
                        """, (place, topic, volume))
           ksiazki = cur.fetchall()
           for pozycja in ksiazki:
                print(pozycja['tytul'] )
           print() 
    elif place == "obojętnie"  and topic == "obojętnie":                                                                        #parametr volume  && time    && hero              != "obojętnie"
           cur.execute(
                        """
                        SELECT tytul, bohater, miejsce, czasy, motyw, liczba_tomow FROM kryminal WHERE bohater= ? AND czasy= ? AND liczba_tomow =?
                        """, (hero, time, volume))
           ksiazki = cur.fetchall()
           for pozycja in ksiazki:
                print(pozycja['tytul'] )
           print() 
    elif topic == "obojętnie" and volume == "obojętnie":                                                                        #parametr time    && hero    && place             != "obojętnie"
           cur.execute(
                        """
                        SELECT tytul, bohater, miejsce, czasy, motyw, liczba_tomow FROM kryminal WHERE bohater= ? AND  miejsce= ? AND czasy= ? 
                        """, (hero, place, time ))
           ksiazki = cur.fetchall()
           for pozycja in ksiazki:
                print(pozycja['tytul'] )
           print()   
    elif place == "obojętnie" and volume == "obojętnie":                                                                        #parametr time    && hero    && topic             != "obojętnie"
           cur.execute(
                        """
                        SELECT tytul, bohater, miejsce, czasy, motyw, liczba_tomow FROM kryminal WHERE bohater= ?  AND czasy= ? AND  motyw= ?
                        """, (hero, time, topic))
           ksiazki = cur.fetchall()
           for pozycja in ksiazki:
                print(pozycja['tytul'] )
           print() 
    

    elif hero == "obojętnie":                                                                                                   #parametr place   && topic   && volume && time    != "obojętnie"
           cur.execute(
                        """
                        SELECT tytul, bohater, miejsce, czasy, motyw, liczba_tomow FROM kryminal WHERE miejsce= ? AND czasy= ? AND  motyw= ? AND liczba_tomow =?
                        """, (place, time, topic, volume ))
           ksiazki = cur.fetchall()
           for pozycja in ksiazki:
                print(pozycja['tytul'] )
           print()   
    elif place == "obojętnie":                                                                                                  #parametr hero    && topic   && volume && time    != "obojętnie"
           cur.execute(
                        """
                        SELECT tytul, bohater, miejsce, czasy, motyw, liczba_tomow FROM kryminal WHERE bohater= ? AND czasy= ? AND  motyw= ? AND liczba_tomow =?
                        """, (hero, time, topic, volume))
           ksiazki = cur.fetchall()
           for pozycja in ksiazki:
                print(pozycja['tytul'] )
           print()  
    elif time == "obojętnie" :                                                                                                  #parametr hero    && place   && topic && volume   != "obojętnie"
           cur.execute(
                        """
                        SELECT tytul, bohater, miejsce, czasy, motyw, liczba_tomow FROM kryminal WHERE bohater= ? AND  miejsce= ? AND  motyw= ? AND liczba_tomow =? 
                        """, (hero, place, topic, volume))
           ksiazki = cur.fetchall()
           for pozycja in ksiazki:
                print(pozycja['tytul'] )
           print() 
    elif topic == "obojętnie":                                                                                                  #parametr hero    && place   && volume && time    != "obojętnie"
           cur.execute(
                        """
                        SELECT tytul, bohater, miejsce, czasy, motyw, liczba_tomow FROM kryminal WHERE bohater= ? AND  miejsce= ? AND czasy= ?  AND liczba_tomow =?
                        """, (hero, place, time, volume))
           ksiazki = cur.fetchall()
           for pozycja in ksiazki:
                print(pozycja['tytul'] )
           print() 
    elif volume == "obojętnie":                                                                                                 #parametr hero    && place   && topic && time     != "obojętnie"
           cur.execute(
                        """
                        SELECT tytul, bohater, miejsce, czasy, motyw, liczba_tomow FROM kryminal WHERE bohater= ? AND  miejsce= ? AND czasy= ? AND  motyw= ? 
                        """, (hero, place, time, topic ))
           ksiazki = cur.fetchall()
           for pozycja in ksiazki:
                print(pozycja['tytul'] )
           print()  
           
   

    else:                                                                                #wszystkie parametry dowolne                                                                                
           cur.execute(
                        """
                        SELECT tytul, bohater, miejsce, czasy, motyw, liczba_tomow FROM kryminal WHERE bohater= ? AND  miejsce= ? AND czasy= ? AND  motyw= ? AND liczba_tomow =?
                        """, (hero, place, time, topic, volume))
           ksiazki = cur.fetchall()
           for pozycja in ksiazki:
                print(pozycja['tytul'] )
           print()  