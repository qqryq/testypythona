#! /usr/bin/env python3
#-*- coding: utf-8 -*-

from random import randint

ile = int(input('Ile liczb wylosować?'))
lista= [] # pusta lista
for i in range(0, ile):
    lista.append(randint(0, 100))

'''
print(lista)

print('Dodwanie elementów na końculisty')
for i in range(0, 3):
    liczba = int(input('Podaj liczbę: '))
    lista.append(liczba)
print(lista)

print('Zawartość listy ([indeks] wartość):')
for i, v in enumerate(lista):
    print('[', i, '] ', v)
print()

print('Elementy w odwróconym porządku')
for e in reversed(lista):
    print(e,end = " ")
print()

print('Elementy posortowane rosnąco:')
for e in sorted(lista):
    print(e, end = " ")
print()

e = int(input("którą liczbę usunąć?"))
lista.remove(e)
#print(lista)

print('Wstawianie elementów do listy')
a, i = eval(input('Podaj element i indeks oddzielone przecinkiem: '))
lista.insert(i, a)
#print(lista)
'''


print('Wyszukiwanie i zliczanie elementów w liście')
e = int(input('Podaj szukaną liczbę: '))
print('Liczba wystąpięń: ')
print(lista.count(e))
print('Liczba wystąpięń liczby "10": ', lista.count(10))
print('Liczba wystąpięń liczby "6": ', lista.count(6))
print('Liczba wystąpięń liczby "16": ', lista.count(16))
print('Liczba wystąpięń liczby "2": ', lista.count(2))
print('Liczba wystąpięń liczby "28": ', lista.count(28))
print('Liczba wystąpięń liczby "4": ', lista.count(4))
print('Liczba wystąpięń liczby "1": ', lista.count(1))
print('Liczba wystąpięń liczby "9": ', lista.count(9))
print('Liczba wystąpięń liczby "30": ', lista.count(30))
print('Liczba wystąpięń liczby "8": ', lista.count(8))


#print('Indeks pierszego wystąpienia: ')
#if lista.count(e):
#    print(lista.index(e))
#else:
#    print('Brak elementu w liście.')


'''
print('Pobieramy i usuwam ostatni element z listy: ')
print(lista.pop())
#print(lista)
'''

print ('Część listy (notacja wycinkowa):')
i, j = eval(input('Podaj index początkowy i końcowy oddzielone przecinkiem: '))
print(lista[i:j])


'''
print()
print('Tupla to lista niemodyfikowalna.')
print('Prób zmiany tupli eneruje błąd:')
tupla = tuple(lista)
#tupla[0] = 100
'''














