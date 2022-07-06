from passlib.hash import sha256_crypt

def encrypt_passwd(password):
    password = sha256_crypt.encrypt(password)
    return password
