SQL_CRIAR_TABELA_CONSUMO = """
    CREATE TABLE IF NOT EXISTS consumo (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        id_Usuario INTEGER,
        id_Suplemento INTEGER,
        nome_Suplemento TEXT,
        nome_Usuario TEXT,
        data_Consumo DATE,
        quantidade INTEGER,
        FOREIGN KEY (id_Usuario) REFERENCES usuario(id),
        FOREIGN KEY (id_Suplemento, nome_Suplemento) REFERENCES suplemento(id, nome)
    )
"""

SQL_INSERIR_CONSUMO = """
    INSERT INTO consumo (id_Usuario, id_Suplemento, nome_Suplemento, nome_Usuario, data_Consumo, quantidade)
    VALUES (?, ?, ?, ?, ?, ?)
"""

SQL_OBTER_TODOS_CONSUMO = """
    SELECT id, id_Usuario, id_Suplemento, nome_Suplemento, nome_Usuario, data_Consumo, quantidade
    FROM consumo
    ORDER BY data_Consumo
"""

SQL_ALTERAR_CONSUMO = """
    UPDATE consumo
    SET id_Usuario = ?, id_Suplemento = ?, nome_Suplemento = ?, nome_Usuario = ?, data_Consumo = ?, quantidade = ?
    WHERE id = ?
"""

SQL_EXCLUIR_CONSUMO = """
    DELETE FROM consumo
    WHERE id = ?
"""

SQL_OBTER_CONSUMO_POR_ID = """
    SELECT id, id_Usuario, id_Suplemento, nome_Suplemento, nome_Usuario, data_Consumo, quantidade
    FROM consumo
    WHERE id = ?
"""

SQL_OBTER_QUANTIDADE_CONSUMO = """
    SELECT COUNT(*) FROM consumo
"""
