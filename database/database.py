import sqlite3


def conectar():

    conexao = sqlite3.connect("database/database.db")

    return conexao  