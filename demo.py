#!/usr/bin/python
# -*-coding:UTF-8 -*
from deck import Deck
import sys


def print_cipher(result):
    cpt = 0
    for r in result:
        sys.stdout.write(r)
        cpt+=1
        if(cpt % 5 == 0):
            print ' ',
    print ""

mydeck = Deck('schneier pisa',(7,14))
print "encrypting 'Bonjour monsieur 12'"
output = mydeck.crypt('Bonjour monsieur 12')
print_cipher(output)

otherdeck = Deck('schneier pisa',(7,14))
baddeck = Deck('schneier pisa',(7,15))

print "decrypting with otherdeck:"
print otherdeck.decrypt(output)

print "result with wrong key:"
print baddeck.decrypt(output)
