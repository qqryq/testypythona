#! /usr/bin/env python3
#-*- coding: utf-8 -*-
lista = []
op = "t"
while op == "t":
    while not len(lista) == 3:
        lista = input('Podaj trzy liczby oddzielone spacjami: ').split(",")
        #lista = [a, b, c]
        if len(lista) < 3:
            print('Wprowadzono za mało liczb.')
        elif len(lista) > 3:    
            print('Wprowadzono za dużo liczb.')
    

    a = lista[0]
    b = lista[1]
    c = lista[2]    

    print('Wprowadzono liczby: ', a, b, c,)
    print ('\nNajmniejsza: ')
    
    if a < b:
        if a < c:
            najmniejsza = a
        else:
            najmniejsza = c
    elif b < c:
        najmniejsza = b
    else:
        najmniejsza = c

    print(najmniejsza)    
    op = input('Jeszcze raz t/n? ')
    lista = []
print('Koniec.')















