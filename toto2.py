#!/usr/bin/env python3
#-*- coding: utf-8 -*-
import random

try:
    ileliczb = int(input("Ile liczb typujesz: "))
    maksliczba = int(input("Maksymalna losowana liczba: "))
    if ileliczb > maksliczba:
        print("Błędne dane!")
        exit()
except ValueError:
    print("Błedne dane!")
    exit()

liczby = []
i = 0
while i < ileliczb:
    liczba = random.randint(1, maksliczba)
    if liczby.count(liczba) == 0:
        liczby.append(liczba)
        i= i + 1


for j in range (3):
    typy = set()
    print("Losowanie nr %s" % (j + 1))
    print("Wytypuj %s z %s liczb: " % (ileliczb, maksliczba))
    i = 0
    while i < ileliczb:
        try:
            typ = int(input("Podaj liczbę %s: " % (i + 1)))
        except ValueError:
            print("Błęne dane!")
            continue

        if 0 < typ <= maksliczba and typ not in typy:
            typy.add(typ)    
            i = i + 1

    trafione = set(liczby) & typy
    if trafione:
        print("\nIlość tafień: %s" %len(trafione))
        print("Trafione liczby: ", trafione)
    else:
        print("Brak trafień. Spróbój jeszcze raz!")

    print("Podane liczby: ", typy)
    print("\n" + "X" * 40 + "\n") # drukowanie pusty wiersz XXXX pusty wiersz

print("Wylosowane liczby: ", liczby)


#    propozycja = int(input("Propozycja nr %s podaj liczbę: " % ( i + 1)))
#    if propozycja < maksliczba:
#        liczby.append(propozycja)
#        print("Twoja popozycja nr %s to: %s" % (i +1, propozycja))
#    else:
#        print("Twoja propozycja jest błędna.")
# print("Poprawienie wytypowałeś liczby: ", liczby)
