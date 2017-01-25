#!/usr/bin/python
# -*-coding:UTF-8 -*
from deck import Deck

mydeck = Deck('schneier pisa',(7,14))
print "encrypting 'Bonjour'"
mydeck.crypt('Bonjour')

otherdeck = Deck('schneier pisa',(7,14))
baddeck = Deck('schneier pisa',(7,15))
