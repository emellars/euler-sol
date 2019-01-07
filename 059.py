#Runtime ~1.5s.

import itertools as iter

#Partition a list into groups of size sublist_size.
def reshape(list, sublist_size):
    return [list[n:n+sublist_size] for n in range(0, len(list), sublist_size)]

with open("059.txt", "r") as cipher:
    cipher_text = cipher.read()

cipher_text = reshape(list(map(int, cipher_text.split(","))), 3)    #Partition cipher into groups of three as the password is three characters long and cyclically repeats.
passwords = list(iter.permutations(range(97,123), 3))   #Password is given as three lowercase characters, which correspond to the range given here.

for password in passwords:
    plain_text = [list(map(lambda x,y: x^y, cipher, password)) for cipher in cipher_text]    #XOR the cipher text with the password.
    plain_text = [elem for sublist in plain_text for elem in sublist] #Flatten the decrypted text.
    plain_text_ASCII = map(chr, plain_text)   #Convert plaintext from a number to its ASCII letter.
    plain_text_ASCII = "".join(elem for elem in plain_text_ASCII) #Convert list to string.

    if "The" in plain_text_ASCII and "the" in plain_text_ASCII and "be" in plain_text_ASCII and "to" in plain_text_ASCII and "of" in plain_text_ASCII: break    #Scan for the most common english words and stop on the first plaintext that contains them all.

print("Sum of ASCII values of plaintext is:", sum(plain_text))
print("Password is:", "".join(elem for elem in map(chr, password)))
print("The plaintext is:", plain_text_ASCII)
