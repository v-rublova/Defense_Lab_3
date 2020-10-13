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
    print("*"*10,"p="+str(p),"q="+str(q),"*"*10,sep="\n")
    n = p * q
    phi = (p - 1) * (q - 1)
    e = prevprime(phi)

    pub.append(e)
    pub.append(n)
    
    #private key
    d = libnum.invmod(e,phi)

    priv.append(d)
    priv.append(n)

def block_it_up(mess,public_key,numeric_mess):
    mess_copy = mess
    ev = true
    c = 0 #counter for blocks
    str_buf = ""
    if (len(mess_copy) % 2 != 0): ev = false
    for i in range(0,len(mess_copy)):
        c+=1
        if (c <= 2):
            str_buf+=str.zfill(str(ord(mess_copy[i])),3)
        if (c == 2 or (not ev and i == len(mess_copy) - 1)):
            if not numeric_mess:#if list is empty
                numeric_mess.append(str_buf) 
            else:
                numeric_mess.append((int(str_buf) + int(numeric_mess[len(numeric_mess) - 1])) % public_key[1])
            str_buf = ""
            c = 0
def cipher(data,public_key,raw_message):
    for i in data:
        raw_message.append(pow(int(i),public_key[0],public_key[1]))

def decipher(raw_message,private_key,info):
    data = []
    for block in raw_message:
        data.append(str.zfill(str(pow(block,private_key[0] ,private_key[1])),6))
    if (len(data) > 1):
        for i in range(len(data) - 1,0,-1):
            data[i] = str.zfill(str((int(data[i]) - int(data[i - 1])) % private_key[1]),6)
    for i in data:
        info.extend([str(i)[:3],str(i)[3:]])

#if message is not null
t = true
#message
while t:
    mess = input("Your message:")
    if mess: t = false
print("Open message:",mess,sep="\n")
#empty keys
public_key = []
private_key = []
#data in numeric format
numeric_mess = []
#ciphered data
raw_message = []
#deciphered data
message = []



keys(public_key,private_key,10000,100000)
block_it_up(mess,public_key,numeric_mess)
print("Open message (numbers):")
for i in numeric_mess:
    print(str(i),end="-")

cipher(numeric_mess,public_key,raw_message)

print("\nCiphered message: ")
for i in raw_message:
    print(str(i),end="-")

decipher(raw_message,private_key,message)
print("\nDeciphered message:")
for i in message:
    if int(i): 
        print(str(chr(int(i))),end="")
print()