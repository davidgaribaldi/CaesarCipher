"""

Challenge #2

DavidGaribaldi

Create a Caesar Cipher with two inputs (Message, shift)

"""
import string

word = 'dc'
word = word.lower()
n = 1
p = 0
myDict = dict(zip(string.ascii_lowercase, range(1,27)))
letters = list(string.ascii_lowercase)

for l in word[p:]:
    for i in myDict:
        if i == l :
            new_l = myDict[i]+3
            for char in letters:
                if n == new_l and new_l < 27:
                    print(char)
                    p += 1
                    break
                n += 1
            n = 0
            

                