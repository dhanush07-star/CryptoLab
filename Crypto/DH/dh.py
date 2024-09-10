def mod_exp(base, exp, mod):
    """Perform modular exponentiation."""
    return pow(base, exp, mod)

def diffie_hellman(p, g, private_key_a, private_key_b):
    """
    Perform Diffie-Hellman key exchange.
    
    :param p: Prime number (modulus)
    :param g: Base (generator)
    :param private_key_a: Private key for party A
    :param private_key_b: Private key for party B
    :return: Shared secret computed by both parties
    """
    # Compute public keys
    public_key_a = mod_exp(g, private_key_a, p)
    public_key_b = mod_exp(g, private_key_b, p)
    
    # Compute shared secrets
    shared_secret_a = mod_exp(public_key_b, private_key_a, p)
    shared_secret_b = mod_exp(public_key_a, private_key_b, p)
    
    return shared_secret_a, shared_secret_b

# Example usage
if __name__ == "__main__":
    # Prime number and base (generator)
    p = 23
    g = 5
    
    # Private keys for Party A and Party B
    private_key_a = 6
    private_key_b = 15
    
    # Compute the shared secret
    shared_secret_a, shared_secret_b = diffie_hellman(p, g, private_key_a, private_key_b)
    
    print(f"Shared secret computed by Party A: {shared_secret_a}")
    print(f"Shared secret computed by Party B: {shared_secret_b}")
    
    # Verify that both shared secrets are the same
    assert shared_secret_a == shared_secret_b, "Shared secrets do not match!"
    print("Shared secrets match. Key exchange successful!")
