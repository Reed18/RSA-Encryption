#Programming Activity #2 - CS Elec2 Computer Security and Cryptography
#Submitted by Reden Mar L. Bellen BSCS-3B
#Program applying RSA Cryptosystem in Python
import math
import random

#pre-define two 15-digits prime numbers
p = 100000000105583
q = 111111151111111
n = p * q
#totient of n
tn = (p - 1)*(q - 1)
#generating the value of e
while True:
  #Randomly selects value of e
  e = random.randint(1, tn)
  #checks if e chosen randomly is valid
  if math.gcd(e, tn) == 1 and pow(e, -1, tn) != e:
    break
#computing for the value of d
d = pow(e, -1, tn)
#Printing the values of Public Keys
print("\nPublic Keys:\n","e = ", e,"\n n = ", n,"\n")
#asking for the message to be encrypted from the user
message = input("Input message to be encrypt:\n ")

#The message encryption starts here
ciphered = " "
#Iterating through the characters of the string and encrypting them with the public key e
for char in message:
  ciphered += "X" + str(pow(ord(char), e, n))
#Printing of the encrypted message
print("\nCiphered Message:\n",ciphered.replace("X","01234567899876543210"))

#The message decryption starts here
deciphered = " "
#Iterating through the list separated by X and decrypting them with the private key d
temp = list(ciphered.split("X"))
temp.remove(" ")
for char in temp:
	deciphered += chr(pow(int(char), d, n))
#Printing of the decrypted message
print("\nDeciphered Message:\n", deciphered,"\n")