from sympy import *
import libnum
import random

def keys(pub,priv,floor,ceil):
    """
       pub - list for public key;
       priv - list for private key;
       floor - lower boundary for random prime number generator;
       ceil - upper boundary for random prime number generator;
    """
    p = 0 #prime number №uno
    q = 0 #prime number №dos

    q = randprime(floor,ceil)
    p = randprime(floor,ceil)
    n = p * q
    phi = (p - 1) * (q - 1)
    e = prevprime(phi)

    pub.append(e)
    pub.append(n)
    
    #private key
    d = libnum.invmod(e,phi)

    priv.append(d)
    priv.append(n)

def cipher(data,public_key,raw_message):
    for i in range(len(mess)):
        raw_message.append(pow(ord(data[i]),public_key[0],public_key[1]))

def decipher(raw_message,private_key,data):
    for block in raw_message:
        data.append(pow(block,private_key[0] ,private_key[1]))
#message
mess = "Viktoria"

#empty keys
public_key = []
private_key = []

#ciphered data
raw_message = []
#deciphered data
message = []

print("Message:")
for i in range(len(mess)):
    print(mess[i] + ' ' + str(ord(mess[i])))

keys(public_key,private_key,10,100)
cipher(mess,public_key,raw_message)
decipher(raw_message,private_key,message)

print("Deciphered:")
for i in message:
    print(str(chr(i)))