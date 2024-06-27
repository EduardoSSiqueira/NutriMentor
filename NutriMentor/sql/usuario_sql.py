SQL_CRIAR_TABELA = """
    CREATE TABLE IF NOT EXISTS usuario (
        id_usuario INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        cpf TEXT NOT NULL UNIQUE,
        data_nascimento DATE NOT NULL,
        endereco TEXT NOT NULL,
        telefone TEXT NOT NULL UNIQUE,
        email TEXT NOT NULL UNIQUE,
        senha TEXT NOT NULL,
        token TEXT)
"""

SQL_INSERIR = """
    INSERT INTO usuario(nome, cpf, data_nascimento, endereco, telefone, email, senha)
    VALUES (?, ?, ?, ?, ?, ?, ?)
"""

SQL_OBTER_TODOS = """
    SELECT id_usuario, nome, cpf, data_nascimento, endereco, telefone, email
    FROM usuario
    ORDER BY nome
"""

SQL_ALTERAR = """
    UPDATE usuario
    SET nome=?, cpf=?, data_nascimento=?, endereco=?, telefone=?, email=?
    WHERE id_usuario=?
"""

SQL_ALTERAR_SENHA = """
    UPDATE usuario
    SET senha=?
    WHERE id_usuario=?
"""

SQL_EXCLUIR = """
    DELETE FROM usuario    
    WHERE id_usuario=?
"""

SQL_OBTER_POR_ID = """
    SELECT id_usuario, nome, cpf, data_nascimento, endereco, telefone, email
    FROM usuario
    WHERE id_usuario=?
"""

