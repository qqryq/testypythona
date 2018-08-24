#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from totomodul import ustawienia, losujliczby, pobierztypy
from totomodul import czytaj_json, zapisz_json
import time


def main(args):
    # ustawienia gry
    nick, ileliczb, maksliczba, ilerazy = ustawienia()

    # losujemy liczby
    liczby = losujliczby(ileliczb, maksliczba)

    # pobieramy typy użytkownika i sprawdzamy ile liczb trafił
    for i in range(ilerazy):
        typy = pobierztypy(ileliczb, maksliczba)
        iletraf = wyniki(set(liczby), typy)
    
    nazwapliku = nick + ".json" # nazwa pliku z historią losowań
    losowania = czytaj_json(nazwapliku)
    


    losowania.append({
        "czas": time.time(),
        "dane": (ileliczb, maksliczba),
        "wylosowane": liczby,
        "ile": iletraf
    })

    zapisz_json(nazwapliku, losowania)
    
    print("\nLosowania: ", liczby)
    return 0

def wyniki(liczby, typy):
    """Funkcaja porównujewylosowane i wytypowane liczby,
    zwraca ilość trafień"""
    trafione = set(liczby) & typy
    if trafione:
        print("\nIlość trafień: %s" % len(trafione))
        trafione = ", ".join(map(str, trafione))
        print("Trafione liczby: %s" % trafione)
    else:
        print("Brak trafień. Spróbuj jeszcze raz!")
        
    print("\n" + "X" * 40 + "\n") # wydruk linii odzielającej z XXXX

    return len(trafione)


if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))



