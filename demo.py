#!/usr/bin/python
# -*-coding:UTF-8 -*
from deck import Deck
import sys
"""leave at least 2 spaces after each number, the encoding isn't that good
yet"""

def print_cipher(result):
    cpt = 0
    for r in result:
        sys.stdout.write(r)
        cpt+=1
        if(cpt % 5 == 0):
            print ' ',
    print ""

mydeck = Deck('schneier pisa',(7,14))
message = 'Bonjour monsieur 12  comment vont messieurs 0  a 250?'
print "encrypting :"+message
output = mydeck.crypt(message)
print_cipher(output)
print ""

otherdeck = Deck('schneier pisa',(7,14))
baddeck = Deck('schneier pisa',(7,15))

print "decrypting with otherdeck:"
print otherdeck.decrypt(output)
print ""
print "result with wrong key:"
print baddeck.decrypt(output)

print ""
print "result with wrong passphrase:"
print Deck('pontifex',(7,14)).decrypt(output)
