#! /usr/bin/env python3
#-*- coding: utf-8 -*-


def fib_iter1(n): # definicja funkcji
    '''
    Funkcja drukuje kolejne wyrazy ciągu Fibonacciego
    aż do wyrazu n-tego, który zwraca.
    Wersja iteracyjnaz pętlą while.
    '''
    pwyrazy = (0, 1) # dwa pierwsze wyrazy zapisane w tupli
    a, b = pwyrazy # przypisanie wielokrotne, rozpakowanie tupli
    print(a, end=" ")
    while n > 1:
        print (b, end=" ")
        a, b = b, a + b # przypisanie wielokrotne
        n -= 1

















def main(args):
    n = int(input('Podaj nr wyrazu: '))
    fib_iter1(n)
    print()
    print("=" * 40)








if __name__ == '_main__':
    import sys
    sys.exit(main(sys.argv))
    











