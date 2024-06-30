import json
import sqlite3
from typing import List, Optional
from models.Usuario import Usuario
from sql.UsuarioSql import *
from util.bancodedados import obter_conexao


class UsuarioRepo:

    @classmethod
    def criar_tabela(cls):
        with obter_conexao() as conexao:
            cursor = conexao.cursor()
            cursor.execute(SQL_CRIAR_TABELA)

    @classmethod
    def inserir(cls, usuario: Usuario) -> Optional[Usuario]:
        try:
            with obter_conexao() as conexao:
                cursor = conexao.cursor()
                cursor.execute(
                    SQL_INSERIR,
                    (
                        usuario.nome,
                        usuario.cpf,
                        usuario.data_nascimento,
                        usuario.endereco,
                        usuario.telefone,
                        usuario.email,
                        usuario.senha,
                    ),
                )
                if cursor.rowcount > 0:
                    usuario.id = cursor.lastrowid
                    return usuario
        except sqlite3.Error as ex:
            print(ex)
            return None

    @classmethod
    def alterar(cls, usuario: Usuario) -> bool:
        try:
            with obter_conexao() as conexao:
                cursor = conexao.cursor()
                cursor.execute(
                    SQL_ALTERAR,
                    (
                        usuario.nome,
                        usuario.cpf,
                        usuario.data_nascimento,
                        usuario.endereco,
                        usuario.telefone,
                        usuario.email,
                        usuario.id,
                    ),
                )
                return cursor.rowcount > 0
        except sqlite3.Error as ex:
            print(ex)
            return False

    @classmethod
    def excluir(cls, id: int) -> bool:
        try:
            with obter_conexao() as conexao:
                cursor = conexao.cursor()
                cursor.execute(SQL_EXCLUIR, (id,))
                return cursor.rowcount > 0
        except sqlite3.Error as ex:
            print(ex)
            return False

    @classmethod
    def obter_por_id(cls, id: int) -> Optional[Usuario]:
        try:
            with obter_conexao() as conexao:
                cursor = conexao.cursor()
                tupla = cursor.execute(SQL_OBTER_POR_ID, (id,)).fetchone()
                usuario = Usuario(*tupla)
                return usuario
        except sqlite3.Error as ex:
            print(ex)
            return None



    @classmethod
    def inserir_usuarios_json(cls, arquivo_json: str):
        if UsuarioRepo.obter_quantidade() == 0:
            with open(arquivo_json, "r", encoding="utf-8") as arquivo:
                usuarios = json.load(arquivo)
                for usuario in usuarios:
                    UsuarioRepo.inserir(Usuario(**usuario))

   
   

    @classmethod
    def alterar_token(cls, id: int, token: str) -> bool:
        try:
            with obter_conexao() as conexao:
                cursor = conexao.cursor()
                cursor.execute(SQL_ALTERAR_TOKEN, (token, id))
                return cursor.rowcount > 0
        except sqlite3.Error as ex:
            print(ex)
            return False


    @classmethod
    def obter_por_email (cls, email: str) -> Optional[Usuario] :
        with obter_conexao() as conexao:
            cursor = conexao. cursor ()
            tupla = cursor. execute(SQL_OBTER_POR_EMAIL, (email,)).fetchone()
            if tupla:
                objeto = Usuario(
                    id=tupla[0], nome=tupla[1], email=tupla[2],
                    admin=tupla[3]
                )
                return objeto
    @classmethod
    def obter_senha_por_email(cls, email: str) -> Optional[str]:
        with obter_conexao() as conexao:
            cursor = conexao.cursor()
            resultado = cursor. execute(SQL_OBTER_SENHA_POR_EMAIL, (email,)).fetchone ()
            if resultado:
                return str(resultado [0])
            

    @classmethod
    def existe_email(cls, email: str) -> Optional[str]:
        with obter_conexao() as conexao:
            cursor = conexao.cursor()
            resultado = cursor. execute(SQL_EXISTE_EMAIL, (email, )) .fetchone()
            if resultado:
                return bool(resultado[0])

    @classmethod
    def criar_administrador_padrao(cls) -> Optional[str]:
        try:
            with obter_conexao() as conexao:
                cursor = conexao. cursor ()
                cursor . execute(SQL_INSERIR_ADMINISTRADOR_PADRAO)
                return cursor. rowcount > 0
        except sqlite3.Error:
            return False
    
    @classmethod
    def criar_usuario_padrao(cls) -> Optional[str]:
        try:
            with obter_conexao() as conexao:
                cursor = conexao. cursor ()
                cursor. execute(SQL_INSERIR_USUARIO_PADRAO)
                return cursor.rowcount > 0
        except sqlite3. Error:
            return False
        
    @classmethod
    def obter_por_token(cls, token: str) -> Optional[Usuario]:
        with obter_conexao() as conexao:
            cursor = conexao.cursor()
            tupla = cursor.execute(SQL_OBTER_POR_TOKEN, (token,)).fetchone()
        if tupla:
            objeto = Usuario(
                id=tupla[0], nome=tupla[1], email=tupla[2]
            )
            return objeto