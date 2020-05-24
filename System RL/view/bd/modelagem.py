# coding: utf-8
import sqlite3, json
import os
import subprocess
import os.path
import constants.constants as constants

def run():
    input_ = "sqlite3 " + constants.addressBD + " '.tables'"
    var = subprocess.getoutput(input_)
    if var == "":
        # conectando...
        conexao = sqlite3.connect(constants.addressBD)
        # BASE_DIR = os.path.dirname(os.path.abspath(__file__))
        # db_path = os.path.join(BASE_DIR, ".aprendizado.db")
        # conexao = sqlite3.connect(db_path)

        # definindo um cursor
        cursor = conexao.cursor()

        # criando as tabelas (schema)
        cursor.execute("""
        CREATE TABLE experimento (
                id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                titulo TEXT NOT NULL
        );
        """)
        # criando as tabelas (schema)
        cursor.execute("""
        CREATE TABLE ensaio (
                id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                idExperimento INTEGER NOT NULL,
                idCombinacao INTEGER NOT NULL,
                count_ensaio INTEGER NOT NULL,
                episodios INTEGER NOT NULL,
                soma_gols_feitos INTEGER NOT NULL,
                soma_gols_sofridos INTEGER NOT NULL,
                soma_saldo_gol INTEGER NOT NULL,
                alpha TEXT NOT NULL,
                gamma TEXT NOT NULL,
                epsilon TEXT NOT NULL
        );
        """)
        # criando as tabelas (schema)
        cursor.execute("""
        CREATE TABLE ensaioRelacao (
                id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                idExperimento INTEGER NOT NULL,
                idEnsaio INTEGER NOT NULL,
                idCombinacao INTEGER NOT NULL
        );
        """)
        # criando as tabelas (schema)
        cursor.execute("""
        CREATE TABLE resultados (
                idEnsaio INTEGER NOT NULL,
                idExperimento INTEGER NOT NULL,
                golFeito INTEGER NOT NULL,
                golSofrido INTEGER NOT NULL,
                saldoGol INTEGER NOT NULL,
                episodio INTEGER NOT NULL
        );
        """)
        # criando as tabelas (schema)
        cursor.execute("""
        CREATE TABLE combinacao (
                id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                idExperimento INTEGER NOT NULL,
                count_combinacao INTEGER NOT NULL,
                count_ensaio INTEGER NOT NULL,
                alpha TEXT NOT NULL,
                gamma TEXT NOT NULL,
                epsilon TEXT NOT NULL
        );
        """)

        print('Schema criado com sucesso')
        # desconectando...
        conexao.close()

    return True