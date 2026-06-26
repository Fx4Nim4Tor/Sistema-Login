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
        INSERT INTO usuarios(nome, senha)
        VALUES (?, ?)
        """,
        (nome, senha)
    )

    conexao.commit()
    conexao.close()