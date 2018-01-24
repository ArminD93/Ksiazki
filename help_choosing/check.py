def CheckGenre(genre):       
            if genre == "fantastyka":                   return True
                
            elif genre == "przygoda":                   return True
            elif genre == "kryminal":                   return True
            elif genre == "obojętnie":                  return True

            else:print("Wybierz jeden z trzech gatunków: przygoda, fantastyka, kryminal");
                
def CheckHero(hero):       
            if hero == "dziewczyna":             return True
                
            elif hero == "chłopak":              return True
            elif hero == "dzieci":               return True
            elif hero == "zwierzę":              return True
            elif hero == "wielu":                return True
            elif hero == "obojętnie":            return True

            else: print("Wybierz jednego bohatera z powyższych opcji");

def CheckPlace(place):       
            if place == "miasto": return True
                
            elif place == "Ameryka Północna":    return True
            elif place == "wyspy":               return True
            elif place == "pociąg":              return True
            elif place == "Europa":              return True
            elif place == "łódź podwodna":       return True
            elif place == "statek":              return True
            elif place == "różne":               return True
            elif place == "obojętnie":           return True

            else: print("Wybierz jedno miejsce z powyższych opcji");

def CheckTime(time):       
            if time == "współczesne":            return True
                
            elif time == "dawne":                return True
            elif time == "różne":                return True
            elif time == "nieokreślone":         return True
            elif time == "przyszłość":           return True
            elif time == "obojętnie":            return True
      
            else: print("Wybierz jednego bohatera z powyższych opcji");


def CheckTopic(topic):       
            if topic== "miasto":                return True
                
            elif topic == "podróż":              return True
            elif topic == "przyjaźń":            return True
            elif topic == "przygody":            return True
            elif topic == "powrotu":             return True
            elif topic == "przeznaczenie":       return True
            elif topic == "karykatura":          return True
            elif topic == "mitologia":           return True
            elif topic == "sprawiedliwość":      return True
            elif topic == "tajemnica":           return True
            elif topic == "dystopia":            return True
            elif topic == "mafia":               return True
            elif topic == "morderstwo":          return True
            elif topic == "obojętnie":           return True

            else: print("Wybierz jeden motyw z powyższych opcji");

def CheckVolume(volume):       
            if volume == "1":                    return True
                
            elif volume == "3":                  return True
            elif volume == "5":                  return True
            elif volume == "7":                  return True
            elif volume == "9":                  return True
            elif volume == "41":                 return True
            elif volume == "obojętnie":          return True
      
            else: print("Wybierz liczbę tomów z powyższych opcji");
