SQL_CRIAR_TABELA = """
    CREATE TABLE IF NOT EXISTS suplemento (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        marca TEXT NOT NULL,
        tipo TEXT NOT NULL)
"""

SQL_INSERIR = """
    INSERT INTO suplemento(nome, marca, tipo)
    VALUES (?, ?, ?)
"""

SQL_OBTER_TODOS = """
    SELECT id, nome, marca, tipo
    FROM suplemento
    ORDER BY nome
"""

SQL_ALTERAR = """
    UPDATE suplemento
    SET nome=?, marca=?, tipo=?
    WHERE id=?
"""

SQL_EXCLUIR = """
    DELETE FROM suplemento    
    WHERE id=?
"""

SQL_OBTER_POR_ID = """
    SELECT id, nome, marca, tipo
    FROM suplemento
    WHERE id=?
"""

SQL_OBTER_QUANTIDADE = """
    SELECT COUNT(*) FROM suplemento
"""
