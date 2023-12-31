"""
a = key
b = message -> message-> characters. Each character -> int by ord(char)
a xor b xor a = b
key xor m
"""

# Note: this is not timing side channel secure

import random
def gen_rand(range,pad):
    key = random.randint(1,range)
    return int_to_bin(key,pad)

def int_to_bin(n:int,pad=7):
    result = []
    while n>0:
        result = [n%2] + result
        n//=2
    while len(result) < pad:
        result = [0] + result
    return result

def bin_to_int(bin:list):
        sum = 0
        for index,i in enumerate(bin[::-1]):
            sum += i*pow(2,index)
        return sum

def string_to_bin(m:str,pad):
    result = []
    for char in m:
        int_char = ord(char)
        bin_char = int_to_bin(int_char,pad)
        result += bin_char
    return result

def bin_to_string(m:list,pad=7):
    string = ''
    for i in range(0,len(m),pad):
        temp_intl = bin_to_int(m[i:i + pad])
        char = chr(temp_intl)
        string += char

    return string

# encrypt
def encrypt(m:list,key:list):
    xor_lt = []
    for i in range(len(m)):
        xor_lt += [m[i]^key[i]]
    return xor_lt
# decrypt
def decrypt(c:list,key:list):
    xor_lt = []
    for i in range(len(c)):
        xor_lt += [c[i]^key[i]]
    return xor_lt
if __name__ == "__main__":
    message = input("message: ")
    pad = 7
    # pad for each character
    m_bin = string_to_bin(message,pad)
    # one pad <=> 7 bits <=> max int 128
    # pad for whole key
    key = gen_rand(pow(128,len(message)-1),len(m_bin))
    print(f"key: {key}")
    encrypted = encrypt(m_bin,key)
    ciphertext = bin_to_string(encrypted,pad)
    print(f"ciphertext: {ciphertext}")
    decrypted = decrypt(encrypted,key)
    decrypted_message = bin_to_string(decrypted,pad)
    print(f"decrypted message: {decrypted_message}")