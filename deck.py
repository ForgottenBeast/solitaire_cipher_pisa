#!/usr/bin/python
# -*-coding:UTF-8 -*
import sys
import re

class Deck():

    def __init__(self,password,private_key):
        """the password is used to key the deck, the private key is a couple of
        numbers between 1 and 52 included that help get rid of the otherwise
        inherent bias. Cards are in a bridge ordering so 1 = ace of Clubs, 52 =
        King of Spades, 53  = first joker and 54 = last joker"""
        if(53 in private_key or 54 in private_key):
            raise Exception("cant use jokers for private key!")

        self.deck = []
        for i in range(1,55):
            self.deck.append(i)

        self.private_key = private_key

        password_letters = list(password)
        password_letters.pop(-1)#get rid of the newline at end of password

        for l in password_letters:
            self.generate(l)

    def crypt(self,message):
        num_pattern = re.compile('[0-9]')
        letters = list(message)
        #letters.pop(-1)

        while(len(letters) % 5 != 0):#let's pad it
            letters.append('x')

        result = []
        numbers = False
        xval = Deck.encode('x')
        for l in letters:
            plain = []

            if(re.search(num_pattern,l)):
                if(not numbers):
                    numbers = True
                    plain.extend([xval,xval,int(l)])
                plain.append(int(l))
                print "added number:",plain
            else:
                if(numbers):
                    plain.extend([xval,xval])
                    numbers = False

                plain.append(Deck.encode(l))

            for p in plain:
                value = self.generate()
                crypted = (p + value)%27
                result.append(Deck.decode(crypted))

        while(len(result) % 5 != 0):
            pad = (self.generate() + xval) % 27
            result.append(pad)


        output = ''.join(result)
        cpt = 0
        for r in result:
            sys.stdout.write(r)
            cpt+=1
            if(cpt % 5 == 0):
                print ' ',

    def generate(self,*args):
        """if called with a letter in argument it will do a setup routine, else
        it will just output the next number in the keystream"""

        
        self.move(53,54)#move both jokers

        self.triple_cut(53,54)#triple cut at the jokers

        self.count_cut(self.deck[-1])

        if(len(args) > 0):
            self.count_cut(Deck.encode(args[0]))#we are keying the deck, done for this turn
            return

        self.move(self.private_key[0],self.private_key[1])#move the secret cards

        self.triple_cut(self.private_key[0],self.private_key[1])

        self.count_cut(self.deck[-1])

        resultidx = self.deck[0]#read the top card giving the index of the
                                #returned value

        return self.deck[resultidx]



    def move(self,c1,c2):

        """newidx is calculated that way because the deck behaves like a loop"""
        j1_idx = self.deck.index(c1)
        self.deck.pop(j1_idx)
        newidx = (j1_idx + 1) if j1_idx < 53 else 1
        self.deck.insert(newidx,c1)

        j2_idx = self.deck.index(c2)
        newidx = (j2_idx + 2) if j2_idx < 51 else 53 - j2_idx
        self.deck.pop(j2_idx)
        self.deck.insert(newidx,c2)


    def triple_cut(self,c1,c2):
        [ind1,ind2] = [self.deck.index(c1),self.deck.index(c2)]
        if(ind1 > ind2):
            tmp = ind1
            ind1 = ind2
            ind2 = tmp
        above = self.deck[:ind1]
        below = self.deck[ind2+1:]#do not include ind2 card


        del self.deck[:ind1]
        del self.deck[ind2 - ind1 + 1:]#we have removed everything before ind1


        self.deck.extend(above)

        self.deck = below + self.deck

    def count_cut(self,value):
        if(value == 54):#it's a joker so don't move
            return

        tocut = self.deck[:value]
        del self.deck[:value]
        tocut.append(self.deck.pop(-1))
        self.deck.extend(tocut)

    @staticmethod
    def encode(letter):
        alphabet = list('abcdefghijklmnopqrstuvwxyz')
        if(letter not in alphabet):
            return (alphabet.index('x') + 1)
        else:
            return (alphabet.index(letter.lower())+1)

    @staticmethod
    def decode(number):
        alphabet = list('abcdefghijklmnopqrstuvwxyz')
        return alphabet[number]
