from database.database import conectar


def registrar(nome, senha):

    conexao = conectar()

    cursor = conexao.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS usuarios(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            senha TEXT NOT NULL
        )
    """)

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
        cursor.execute(
            """
            INSERT INTO usuarios(nome, senha)
            VALUES (?, ?)
            """,
            (nome, senha)
        )



    

    conexao.commit()
    conexao.close()