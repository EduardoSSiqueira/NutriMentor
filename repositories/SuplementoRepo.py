import json
import sqlite3
from typing import List, Optional
from models.Suplemento import Suplemento
from sql.SuplementoSql import *
from util.bancodedados import obter_conexao

class SuplementoRepo:

    @classmethod
    def criar_tabela(cls):
        with obter_conexao() as conexao:
            cursor = conexao.cursor()
            cursor.execute(SQL_CRIAR_TABELA)

    @classmethod
    def inserir(cls, suplemento: Suplemento) -> Optional[Suplemento]:
        try:
            with obter_conexao() as conexao:
                cursor = conexao.cursor()
                cursor.execute(SQL_INSERIR, (
                    suplemento.nome,
                    suplemento.marca,
                    suplemento.tipo,
                ))
                if cursor.rowcount > 0:
                    suplemento.id = cursor.lastrowid
                    return suplemento
        except sqlite3.Error as ex:
            print(ex)
            return None

    @classmethod
    def obter_todos(cls) -> Optional[List[Suplemento]]:
        try:
            with obter_conexao() as conexao:
                cursor = conexao.cursor()
                tuplas = cursor.execute(SQL_OBTER_TODOS).fetchall()
                suplementos = [Suplemento(*t) for t in tuplas]
                return suplementos
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
    def obter_um(cls, id: int) -> Optional[Suplemento]:
        try:
            with obter_conexao() as conexao:
                cursor = conexao.cursor()
                tupla = cursor.execute(SQL_OBTER_POR_ID, (id,)).fetchone()
                if tupla:
                    suplemento = Suplemento(*tupla)
                    return suplemento
                return None
        except sqlite3.Error as ex:
            print(ex)
            return None

    @classmethod
    def obter_quantidade(cls) -> Optional[int]:
        try:
            with obter_conexao() as conexao:
                cursor = conexao.cursor()
                tupla = cursor.execute(SQL_OBTER_QUANTIDADE).fetchone()
                if tupla:
                    return int(tupla[0])
                return None
        except sqlite3.Error as ex:
            print(ex)
            return None

    @classmethod
    def inserir_suplemento_json(cls, arquivo_json: str):
        if SuplementoRepo.obter_quantidade() == 0:
            with open(arquivo_json, "r", encoding="utf-8") as arquivo:
                suplementos = json.load(arquivo)
                for suplemento in suplementos:
                    SuplementoRepo.inserir(Suplemento(**suplemento))
