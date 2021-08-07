# -*- coding: utf-8 -*-
"""
Created on Thu Jan 21 15:19:50 2021

@author: axelt
"""

#subtract 103 from small letters
import sympy

def C_string(M,e,pq):
    #first: convert string to numbers
    C = []
    for letter in M:
        C.append(C_oneChar(letter,e,pq))
    return C

def C_oneChar (M_i,e,pq):
    encryptedText = M_i**e % (pq)
    return encryptedText    

def stringToNumbers(string):
    stringAsNumbers =[]
    for letter in string:
        stringAsNumbers.append(ord(letter.lower())-96)
    return stringAsNumbers
def numbersToString(numbers):
    numbersAsString=[]
    for number in numbers:
        numbersAsString.append(chr(number+97))
    return numbersAsString

def M_string (C, pq,d):
    M = []
    for letter in C:
        m_i = M_oneChar(letter,pq,d)
        M.append(m_i)
    return M

def M_oneChar (C_i,pq,d):
    return C_i**d%(pq)
def computeDecryptionKey (p,q,e):
    a = (p-1)*(q-1)
    #compute the modulo inverse
    #this should be 3, but how do we calculate it????
    d = sympy.mod_inverse(e, a)
    return d

messageToEncrypt = "HOWRU"
#convert the letters to numbers that can be used to encrypt
M = stringToNumbers(messageToEncrypt)
e = 7
p=5
q=11
pq = p*q
#d is the decryption key.


print ("Text: ", messageToEncrypt)
print ("M: ",M)
print ("e: ", e)
print ("pq: ", pq)

C = C_string(M,e,pq)
print ("C: ", C)

print ("----------------")
d = computeDecryptionKey(p,q,e)
print ("d: ", d)

CtoDecrypt=[28,49,11,11,9]
M_decrypted = M_string(C=CtoDecrypt,pq=pq,d=23)
print ("Decrypted Message :", M_decrypted)


print (numbersToString(M_decrypted))











