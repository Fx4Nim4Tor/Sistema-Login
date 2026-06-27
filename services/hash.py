from hashlib import sha256

def criptografa_Senha(senha):
    return sha256(senha.encode()).hexdigest()

def verifica_senha(senha):
    verifica = sha256(senha.encode()).hexdigest()
    
    if verifica == senha:
        return True
    else:
        return False