import sqlite3
from typing import List, Optional
from models.Consumo import Consumo
from sql.ConsumoSql import *
from util.bancodedados import obter_conexao

class ConsumoRepo:

    @classmethod
    def criar_tabela(cls):
        with obter_conexao() as conexao:
            cursor = conexao.cursor()
            cursor.execute(SQL_CRIAR_TABELA_CONSUMO)

    @classmethod
    def inserir(cls, consumo: Consumo) -> Optional[Consumo]:
        try:
            with obter_conexao() as conexao:
                cursor = conexao.cursor()
                cursor.execute(SQL_INSERIR_CONSUMO, (
                    consumo.id_Usuario,
                    consumo.id_Suplemento,
                    consumo.nome_Suplemento,
                    consumo.nome_Usuario,
                    consumo.data_Consumo,
                    consumo.quantidade,
                ))
                if cursor.rowcount > 0:
                    consumo.id = cursor.lastrowid
                    return consumo
        except sqlite3.Error as ex:
            print(ex)
            return None

    @classmethod
    def obter_todos(cls) -> Optional[List[Consumo]]:
        try:
            with obter_conexao() as conexao:
                cursor = conexao.cursor()
                tuplas = cursor.execute(SQL_OBTER_TODOS_CONSUMO).fetchall()
                consumos = [Consumo(*t) for t in tuplas]
                return consumos
        except sqlite3.Error as ex:
            print(ex)
            return None

    @classmethod
    def alterar(cls, consumo: Consumo) -> bool:
        try:
            with obter_conexao() as conexao:
                cursor = conexao.cursor()
                cursor.execute(SQL_ALTERAR_CONSUMO, (
                    consumo.id_Usuario,
                    consumo.id_Suplemento,
                    consumo.nome_Suplemento,
                    consumo.nome_Usuario,
                    consumo.data_Consumo,
                    consumo.quantidade,
                    consumo.id
                ))
                return cursor.rowcount > 0
        except sqlite3.Error as ex:
            print(ex)
            return False

    @classmethod
    def excluir(cls, id: int) -> bool:
        try:
            with obter_conexao() as conexao:
                cursor = conexao.cursor()
                cursor.execute(SQL_EXCLUIR_CONSUMO, (id,))
                return cursor.rowcount > 0
        except sqlite3.Error as ex:
            print(ex)
            return False

    @classmethod
    def obter_um(cls, id: int) -> Optional[Consumo]:
        try:
            with obter_conexao() as conexao:
                cursor = conexao.cursor()
                tupla = cursor.execute(SQL_OBTER_CONSUMO_POR_ID, (id,)).fetchone()
                if tupla:
                    consumo = Consumo(*tupla)
                    return consumo
                return None
        except sqlite3.Error as ex:
            print(ex)
            return None

    @classmethod
    def obter_quantidade(cls) -> Optional[int]:
        try:
            with obter_conexao() as conexao:
                cursor = conexao.cursor()
                tupla = cursor.execute(SQL_OBTER_QUANTIDADE_CONSUMO).fetchone()
                if tupla:
                    return int(tupla[0])
                return None
        except sqlite3.Error as ex:
            print(ex)
            return None
