def diffie_hellman(p,alpha,A_key_private,B_key_private):
    A_pubic =  pow(alpha,A_key_private) % p
    B_pubic =  pow(alpha,B_key_private) % p

    shared_secret_a = pow(pow(alpha,A_key_private),B_key_private) % p
    shared_secret_b = pow(pow(alpha,B_key_private),A_key_private) % p

    return shared_secret_a, shared_secret_b

if __name__ == "__main__":
    p = 173
    alpha = 3
                
    A_key_private = 6                                 
    B_key_private = 11

    shared_secret_a , shared_secret_b = diffie_hellman(p,alpha,A_key_private,B_key_private)

    print(f"Shared secret A: {shared_secret_a}")
    print(f"Shared secret B: {shared_secret_b}")
    
    assert shared_secret_a == shared_secret_b, "Shared secrets do not match!"
    print("Shared secrets match. Key exchange successful!")