# coding: utf-8

secret = 7

guess = int(raw_input("adivina el número secreto entre 1 y 20: "))

if guess == secret:
    print "¡Enhorabuena! lo has advinado, es el número 7"

else:
    print "Ese no es el número secreto, intentalo de nuevo"
