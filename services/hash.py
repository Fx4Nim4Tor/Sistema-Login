from hashlib import sha256

def criptografa_Senha(senha):
    return sha256(senha.encode()).hexdigest()

def verifica_senha(senha,usuario):
    verifica = sha256(senha.encode()).hexdigest()
    
    if verifica == usuario[2]:
        return True
    else:
        return False