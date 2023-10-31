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
        for index,i in enumerate(bin):
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
    temp_c = 0
    string = ''
    for i in range(1,len(m)//pad+1):
        temp_intl = bin_to_int(m[temp_c:temp_c + pad])
        temp_c = temp_c + pad
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
    print(f"m_bin: {m_bin}")
    # one pad <=> 7 bits <=> max int 128
    # pad for whole key
    key = gen_rand(pow(128,len(message)-1),len(m_bin))
    print(f"key: {key}")
    encrypted = encrypt(m_bin,key)
    print(f"encrypted_bin: {encrypted}")
    ciphertext = bin_to_string(encrypted,pad)
    print(f"ciphertext: {ciphertext}, length: {len(ciphertext)}")
    print(f"key: {key}")
    decrypted = encrypt(encrypted,key)
    print(f"decrypted_bin: {decrypted}")
    decrypted_message = bin_to_string(decrypted,pad)
    print(f"descrypted message: {decrypted_message}")