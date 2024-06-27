import sqlite3
from typing import List, Optional
from NutriMentor.model.consumo import Consumo
from sql.consumo_sql import *
from util.database import obter_conexao

class ConsumoRepo():

    @classmethod
    def criar_tabela(cls):
        with obter_conexao() as conexao:
            cursor = conexao.cursor()
            cursor.execute(SQL_CRIAR_TABELA)

    @classmethod
    def inserir(cls,consumo: Consumo) -> Optional[Consumo]:
        try:
            with obter_conexao() as conexao:
                cursor = conexao.cursor()
                cursor.execute(SQL_INSERIR, (
                    Consumo.data_consumo,
                    Consumo.quantidade,
                    Consumo.tipo,
                ))
                if cursor.rowcount > 0:
                    suplemento.id = cursor.lastrowid
                    return suplemento
        except sqlite3.Error as ex:
            print(ex)
            return None
        
    @classmethod
    def obter_todos(cls) -> List[Suplemento]:
        try:
            with obter_conexao() as conexao:
                cursor = conexao.cursor()
                tuplas = cursor.execute(SQL_OBTER_TODOS).fetchall()
                suplemento = [Suplemento(*t) for t in tuplas]
                return suplemento
        except sqlite3.Error as ex:
            print(ex)
            return None   
        
    @classmethod
    def alterar(cls, suplemento: Suplemento) -> bool:
        try:
            with obter_conexao() as conexao:
                cursor = conexao.cursor()
                cursor.execute(SQL_ALTERAR, (
                    suplemento.nome,
                    suplemento.marca,
                    suplemento.tipo,
                    suplemento.id
                ))
                return(cursor.rowcount > 0)
        except sqlite3.Error as ex:
            print(ex)
            return False

    @classmethod
    def excluir(cls, id: int) -> bool:
        try:
            with obter_conexao() as conexao:
                cursor = conexao.cursor()
                cursor.execute(SQL_EXCLUIR, (id,))
                return (cursor.rowcount > 0)
        except sqlite3.Error as ex:
            print(ex)
            return False
        
    @classmethod
    def obter_um(cls, id: int) -> Optional[Suplemento]:
        try:
            with obter_conexao() as conexao:
                cursor = conexao.cursor()
                tupla = cursor.execute(SQL_OBTER_POR_ID, (id,)).fetchone()
                suplemento = Suplemento(*tupla)
                return suplemento
        except sqlite3.Error as ex:
            print(ex)
            return None
        
    
    @classmethod
    def obter_quantidade(cls) -> Optional[int]:
        try:
            with obter_conexao() as conexao:
                cursor = conexao.cursor()
                tupla = cursor.execute(SQL_OBTER_QUANTIDADE).fetchone()
                return int(tupla[0])
        except sqlite3.Error as ex:
            print(ex)
            return None   