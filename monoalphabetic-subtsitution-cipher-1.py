# imperfection of the monoalphabetic substituion cipher using Shannon's Theorem

def fact(n):
    if n == 1:
        return 1
    else:
        return n*fact(n-1)

n = 1
keys = fact(26)
# messages = 26^n

while 26**n<=keys:
    n+=1

print(n)