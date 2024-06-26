SQL_CRIAR_TABELA = """
    CREATE TABLE IF NOT EXISTS consumo (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        data_consumo DATETIME NOT NULL,
        quantidade INTEGER NOT NULL,
        cliente_id INTEGER NOT NULL,
        FOREIGN KEY (id_cliente) REFERENCES cliente(id))
"""

SQL_INSERIR = """
    INSERT INTO consumo(data_consumo, quantidade, id_cliente)
    VALUES (?, ?, ?)
"""

SQL_ALTERAR_DATA_HORA = """
    UPDATE consumo
    SET data_consumo=?
    WHERE id=?
"""

SQL_EXCLUIR = """
    DELETE FROM consumo
    WHERE id=?
"""

SQL_OBTER_POR_ID = """
    SELECT id, data_consumo, quantidade, id_cliente
    FROM consumo
    WHERE id=?
"""

SQL_OBTER_QUANTIDADE_POR_PERIODO = """
    SELECT COUNT(*) 
    FROM consumo
    WHERE (id_cliente = ?) AND (data_consumo BETWEEN ? AND ?)
"""









