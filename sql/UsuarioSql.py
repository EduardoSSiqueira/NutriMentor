SQL_CRIAR_TABELA = """
    CREATE TABLE IF NOT EXISTS usuario (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
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

SQL_ALTERAR = """
    UPDATE usuario
    SET nome=?, cpf=?, data_nascimento=?, endereco=?, telefone=?, email=?
    WHERE id=?
"""

SQL_ALTERAR_TOKEN = """
    UPDATE usuario
    SET token=?
    WHERE id=?
"""

SQL_EXCLUIR = """
    DELETE FROM usuario    
    WHERE id=?
"""
SQL_OBTER_POR_TOKEN = """"
    SELECT id, nome, email
    FROM usuario
    WHERE token =?
"""
SQL_OBTER_POR_EMAIL = """
    SELECT id, nome, email, admin
    FROM usuario
    WHERE email =?
"""
SQL_OBTER_SENHA_POR_EMAIL = """
    SELECT senha
    FROM usuario
    WHERE email =?
"""

SQL_EXISTE_EMAIL = """
    SELECT EXISTS (
        SELECT 1 FROM usuario
        WHERE email =?
    )
"""
SQL_OBTER_POR_ID = """
    SELECT id, nome, cpf, data_nascimento, endereco, telefone, email
    FROM usuario
    WHERE id=?
"""
# senha 1aA@
SQL_INSERIR_ADMINISTRADOR_PADRAO = """
    INSERT OR IGNORE INTO usuario (
        nome, email, senha)
    VALUES ('Administrador do Sistema', 'admin@email.com',
    '$2b$12$oAmErugexoRbXaSy3QEYB.GUueyURF3hqe0XYs5aEicyVs3B10/zK')
"""

# senha 1aA@
SQL_INSERIR_USUARIO_PADRAO = """
    INSERT OR IGNORE INTO usuario (
        nome, email, senha, admin)
    VALUES ('Usuário Padrão do Sistema', 'usuario@email.com',
    '$2b$12$oAmErugexoRbXaSy3QEYB.GUueyURF3hqe0XYs5aEicyVs3B10/zK')
"""

