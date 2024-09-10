import random
import math
# from sympy import isprime

# import sympy

# def gen1024():
#     while True:
#         p = random.getrandbits(1024)
#         if isprime(p):
#             break
    
#     while True:
#         q = random.getrandbits(1024)
#         if isprime(q):
#             break
#     return p, q

def genPublicPrivate():
    # x, y = gen1024()
    p = 51
    q = 73
    n = p * q
    phi = (p - 1) * (q - 1)


    while True:
        e = random.randint(2, phi - 1)
        if math.gcd(e, phi) == 1:
            break

  
    while True:
        d = random.randint(2, phi - 1)
        if (d * e) % phi == 1:
            break

    print("e:", e)
    print("d:", d)
    print("n:", n)


    # msg = 109
    print("message: ")
    msg = int(input())
    print("message data:" , msg)

    #encryption
    c = pow(msg , e)
    # c = math.fmod(c,n)
    c = c%n
    print("Encrypted data = ", c)

    #decryption 
    m = pow(c,d)
    m = m%n
    print("Original Message Sent = ", m)


genPublicPrivate()




