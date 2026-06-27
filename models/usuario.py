def criar_tabela_usuario(cursor):
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS usuarios(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            senha TEXT NOT NULL
        )
    """)


def inserir_usuario(cursor,nome, senha):
    cursor.execute(
        """
        SELECT * FROM usuarios
        WHERE nome = ?
        """,
        (nome,)
    )

    usuario = cursor.fetchone()
    
    if usuario:
        print("Já existe um usuário com esse nome.")
    else:
        print("Nome disponível.")
        from services.hash import criptografa_Senha
        hash_senha = criptografa_Senha(senha)
        print(hash_senha)
        cursor.execute(
            """
            INSERT INTO usuarios(nome, senha)
            VALUES (?, ?)
            """,
            (nome, hash_senha)
        )

def buscar_usuario(cursor, nome, senha):
    cursor.execute(
        """
        SELECT * FROM usuarios
        WHERE nome = ?
        """,
        (nome,)
    )

    usuario = cursor.fetchone()
    if usuario:
        # o usuario exite
        from services.hash import verifica_senha
        verifica_senha(senha)
        print(senha,"entrou")


    print("testeeeeeeeeeee",usuario)
