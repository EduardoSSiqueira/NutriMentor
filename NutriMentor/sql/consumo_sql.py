SQL_CRIAR_TABELA = """
    CREATE TABLE IF NOT EXISTS consumo (
        consumo_id INTEGER PRIMARY KEY,
        usuario_id INTEGER NOT NULL,
        suplemento_id INTEGER NOT NULL,
        data_consumo DATETIME NOT NULL,
        quantidade INTEGER NOT NULL,
        FOREIGN KEY (usuario_id) REFERENCES usuario(id),
        FOREIGN KEY (suplemento_id) REFERENCES suplemento(id)
)
"""

SQL_INSERIR = """
    INSERT INTO consumo (usuario_id, suplemento_id, data_consumo, quantidade)
    VALUES (?, ?, ?, ?);
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









