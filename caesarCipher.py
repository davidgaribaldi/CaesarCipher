"""

Challenge #2

DavidGaribaldi

Create a Caesar Cipher with two inputs (Message, shift)

"""

import string
            
def shiftLetters(word, shift):
    new_word = ""
    p = 0
    lower_case_letters = dict(zip(string.ascii_lowercase, range(1,27)))
    upper_case_letters = dict(zip(string.ascii_uppercase, range(1,27)))
    for l in word[p:]:
        if l in lower_case_letters:
            for i in lower_case_letters:
                if i == l: 
                    new_letter = lower_case_letters[i] + shift  # Actually a number that corresponds to a letter
                    new_letter = newLowerCaseLetter(new_letter)  # This will turn the number into a letter 
                    new_word = new_word + new_letter
        elif l in upper_case_letters:
            for i in upper_case_letters:
                if i == l: 
                    new_letter = upper_case_letters[i] + shift  # Actually a number that corresponds to a letter
                    new_letter = newUpperCaseLetter(new_letter)  # This will turn the number into a letter 
                    new_word = new_word + new_letter
        else:
            new_word = new_word + l      
    return new_word
                
def newLowerCaseLetter(number):
    n = 1
    letters = list(string.ascii_lowercase)
    if number > 26:
        number = number - 26
    for char in letters:
        if n == number and number < 27:
            return char            
        n += 1
        
def newUpperCaseLetter(number):
    n = 1
    letters = list(string.ascii_uppercase)
    if number > 26:
        number = number - 26
    for char in letters:
        if n == number and number < 27:
            return char            
        n += 1
        
def caesarianShift():
    phrase = 'Rovvy Nkfsn! Sd sc Gonxocnki robo, grkd klyed grobo iye kbo?'  
    shift = int(input('How many spaces should we shift?'))          
    print(shiftLetters(phrase, shift))
    
caesarianShift()
