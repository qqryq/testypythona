#! /usr/bin/env python3
#-*- coding: utf-8 -*-

# deklarujemy i inicjalizujemy zmienne
# aktRok = 2018
pythonRok = 1989


# pobieramy dane
aktRok = int(input('Podaj aktualny rok: '))
imie = input("Jak się nazywasz? ")
wiek = int(input("Ile masz lat? "))

# oblicz wiek pythona
wiekPythona = aktRok - pythonRok

# wyświetlamy komunikaty
print("Witaj", imie)
print("Mów mi Python, mam ", wiekPythona, " lat.")

# instrukcja warunkowa
if wiek > wiekPythona:
    print('Jesteś starszy ode mnie.')
else:
    print('Jesteś młodszy ode mnie.')

