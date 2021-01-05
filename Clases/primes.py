#! /user/bin/env python3

def primo(n):
    i = 2
    a = True
    while i < n:
        if n%i == 0:
            a  = False
            i = n 
        else:
            i =  i + 1
    return a

def primos(n):
    """Esta funcion regresa los primo entre 2 y n"""
    primes = []

    for i in range(2, n):

        if primo(i):
            primes.append(i)

    return primes

def gemelos(n):
    
    primosGemelos = []
    l = primos(n)
    i = 1
    while i < len(l):
        if l[i] - l[i - 1] == 2:
            primosGemelos.append( (l[i-1], l[i]) )
        i = i +1

    return primosGemelos

