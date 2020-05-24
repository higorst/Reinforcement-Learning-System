# coding: utf-8
import sqlite3, json
from datetime import datetime
import os.path
import constants.constants as constants

# ---------------------------------------------- EXPERIMENTOS

def getExperimentos():
    conexao = sqlite3.connect(constants.addressBD)

    titulo = conexao.cursor()
    titulo.execute("select id, titulo from experimento")

    experimentos_titulo = []
    experimentos_titulo.clear()

    experimentos_id = []
    experimentos_id.clear()

    for x in titulo.fetchall():
        experimentos_id.append(x[0])
        experimentos_titulo.append(x[1])

    return tuple([experimentos_id, experimentos_titulo])

def cadastrarExperimento(title):
    conexao = sqlite3.connect(constants.addressBD)

    c = conexao.cursor()    
    c.execute(
        "INSERT INTO experimento (titulo) "
        "VALUES ('" + str(title) + "')")

    conexao.commit()
    conexao.close()

def deletarExperimento(idExperimento):
    conexao = sqlite3.connect(constants.addressBD)

    c = conexao.cursor()    
    c.execute("""DELETE FROM experimento WHERE id = ?""", (str(idExperimento),))
    c.execute("""DELETE FROM ensaio WHERE idExperimento = ?""", (str(idExperimento),))
    c.execute("""DELETE FROM ensaioRelacao WHERE idExperimento = ?""", (str(idExperimento),))
    c.execute("""DELETE FROM resultados WHERE idExperimento = ?""", (str(idExperimento),))
    c.execute("""DELETE FROM combinacao WHERE idExperimento = ?""", (str(idExperimento),))

    conexao.commit()
    conexao.close()

# ---------------------------------------------- ENSAIOS

def cadastrarEnsaio(idExperimento, alpha, gamma, epsilon, golsFeitos, golsSofridos, saldoGols, soma_gols_feitos, soma_gols_sofridos, soma_saldo, episodios):
       
    # ------------------ cadastrar combinação
    conexao = sqlite3.connect(constants.addressBD)
    c = conexao.cursor() 
    d = conexao.cursor() 
    e = conexao.cursor() 

    # verificar se combinação já foi cadastrada
    cadastrar = False
    id_combinacao = None
    count_ensaio = 1

    d.execute(
        "select id, count_ensaio "
        "from combinacao c "
        "where  alpha = '" + alpha + "' and gamma = '" + gamma + "' and epsilon = '" + epsilon + "';")
    # teste = ''
    for x in d.fetchall():
        # teste = x[0]
        id_combinacao = x[0]
        count_ensaio += int(x[1])

    if id_combinacao is None:
        cadastrar = True

    # se cadastrar
    if cadastrar:
        e.execute("select count(c.id) Combinações "
                    "from combinacao c, experimento exp "
                    "where c.idExperimento = exp.id and exp.id = '" + str(idExperimento) + "';")
        count_combinacao = 1
        for x in e.fetchall():
            count_combinacao += x[0]

        d.execute(
            "INSERT INTO combinacao (idExperimento, count_combinacao, count_ensaio, alpha, gamma, epsilon) "
            "VALUES ('" + 
                str(idExperimento) + "','" + 
                str(count_combinacao) + "','" + 
                str(1) + "','" + 
                str(alpha) + "','" + 
                str(gamma) + "','" + 
                str(epsilon) + "')")

        # recuprar id do ensaio cadastrado
        d.execute("SELECT last_insert_rowid();")
        id_combinacao = ''
        for x in d.fetchall():
            id_combinacao = x[0]
    else:
        d.execute(
            "UPDATE combinacao "
            "SET count_ensaio = '" + str(count_ensaio) + "' "
            "WHERE id = '" + str(id_combinacao) + "'; ")

    # ---------------------------------------

    # ---------------------- cadastrar ensaio    

    c.execute(
        "INSERT INTO ensaio (idCombinacao, idExperimento, count_ensaio, episodios, soma_gols_feitos, soma_gols_sofridos, soma_saldo_gol, alpha, gamma, epsilon) "
        "VALUES ('" + 
            str(id_combinacao) + "','" + 
            str(idExperimento) + "','" + 
            str(count_ensaio) + "','" + 
            str(episodios) + "','" + 
            str(soma_gols_feitos) + "','" + 
            str(soma_gols_sofridos) + "','" + 
            str(soma_saldo) + "','" + 
            str(alpha) + "','" + 
            str(gamma) + "','" + 
            str(epsilon) + "')")

    # recuprar id do ensaio cadastrado
    c.execute("SELECT last_insert_rowid();")
    id_ensaio = ''
    for x in c.fetchall():
        id_ensaio = x[0]

    # cadastrar a relação do ensaio com o experimento
    c.execute(
        "INSERT INTO ensaioRelacao (idExperimento, idEnsaio, idCombinacao) "
        "VALUES ('" + 
            str(idExperimento) + "','" + 
            str(id_ensaio) + "','" + 
            str(id_combinacao) + "')")

    # cadastrar resultados do ensaio
    i = 0
    for x in golsFeitos:
        c.execute(
            "INSERT INTO resultados (idEnsaio, idExperimento, golFeito, golSofrido, saldoGol, episodio) "
            "VALUES ('" + 
                str(id_ensaio) + "','" + 
                str(idExperimento) + "','" + 
                str(golsFeitos[i]) + "','" + 
                str(golsSofridos[i]) + "','" + 
                str(saldoGols[i]) + "','" + 
                str(i+1) + "')")
        i += 1

    conexao.commit()
    conexao.close()

def getEnsaios(idExperimento):
    conexao = sqlite3.connect(constants.addressBD)

    c = conexao.cursor()
    c.execute(
        "select c.count_combinacao Combinação, e.count_ensaio Ensaios, e.soma_gols_feitos, e.soma_gols_sofridos, e.soma_saldo_gol SaldoGols, e.id idEnsaio, c.id idCombinação, e.alpha, e.gamma, e.epsilon, e.episodios " 
        "from combinacao c, ensaio e, ensaioRelacao er, experimento exp "
        "where exp.id = '" + str(idExperimento) + "' and "
              "exp.id = er.idExperimento and "
              "c.id = er.idCombinacao and "
              "e.id = er.idEnsaio "
        "order by c.count_combinacao asc;"
        )

    ensaios = []
    ensaios.clear()

    for x in c.fetchall():
        ensaios.append(x)

    return ensaios

def getFullEnsaio(idEnsaio):
    conexao = sqlite3.connect(constants.addressBD)

    c = conexao.cursor()
    c.execute(
        "select golFeito, golSofrido, saldoGol, episodio "
        "from resultados "
        "where idEnsaio = '" + str(idEnsaio) + "';"
        )

    golsFeitos = []
    golsSofridos = []
    saldoGols = []
    episodios = []

    for x in c.fetchall():
        golsFeitos.append(x[0])
        golsSofridos.append(x[1])
        saldoGols.append(x[2])
        episodios.append(x[3])

    return tuple([golsFeitos, golsSofridos, saldoGols, episodios])

def getMAXofEnsaios(idExperimento):
    conexao = sqlite3.connect(constants.addressBD)

    c = conexao.cursor()
    c.execute(
        "select max(m.ensaios) as ensaios "
        "from ( "
            "select count (e.id) as ensaios "
            "from combinacao c, ensaio e, ensaioRelacao er, experimento exp "
            "where exp.id = '" + str(idExperimento) + "' and "
                  "exp.id = er.idExperimento and "
                  "c.id = er.idCombinacao and "
                  "e.id = er.idEnsaio "
            "group by c.id "
        ") as m;"
        )

    max_ = []
    max_.clear()

    for x in c.fetchall():
        max_.append(x)

    return max_

def deletarEnsaio(idExperimento, idEnsaio, alpha, gamma, epsilon):
    conexao = sqlite3.connect(constants.addressBD)

    c = conexao.cursor()    
    c.execute("""DELETE FROM ensaio WHERE id = ?""", (str(idEnsaio),))
    c.execute("""DELETE FROM ensaioRelacao WHERE idEnsaio = ?""", (str(idEnsaio),))
    c.execute("""DELETE FROM resultados WHERE idEnsaio = ?""", (str(idEnsaio),))

    # diminuir valor de count_ensaio da tabela combinação
    count_ensaio = 1
    id_combinacao = 1

    c.execute(
        "select id, count_ensaio "
        "from combinacao c "
        "where  alpha = '" + alpha + "' and gamma = '" + gamma + "' and epsilon = '" + epsilon + "';")
    for x in c.fetchall():
        id_combinacao = x[0]
        count_ensaio = int(x[1]) - 1

    c.execute(
            "UPDATE combinacao "
            "SET count_ensaio = '" + str(count_ensaio) + "' "
            "WHERE id = '" + str(id_combinacao) + "'; ")

    conexao.commit()
    conexao.close()

# ---------------------------------------------- COMBINAÇÕES

def getDados(idExperimento):
    conexao = sqlite3.connect(constants.addressBD)

    c = conexao.cursor()
    c.execute(
        "select c.count_combinacao Combinação, sum(e.soma_gols_feitos)/count(e.id) MediaGolsFeitos, sum(e.soma_gols_sofridos)/count(e.id) MediaGolsSofridos, sum(e.soma_saldo_gol)/count(e.id) MediaSaldoGols, c.alpha, c.gamma, c.epsilon, c.id idCombinação, c.count_combinacao Ensaios "
        "from combinacao c, ensaio e, ensaioRelacao er, experimento exp "
        "where exp.id = '" + str(idExperimento) + "' and "
              "exp.id = er.idExperimento and "
              "c.id = er.idCombinacao and "
              "e.id = er.idEnsaio "
        "group by c.id;"
        )

    resultados = []
    resultados.clear()

    for x in c.fetchall():
        resultados.append(x)

    return resultados

def getCombinacoes(idExperimento):
    conexao = sqlite3.connect(constants.addressBD)

    c = conexao.cursor()
    c.execute(
        "select count(c.id) Combinações "
        "from combinacao c, experimento exp "
        "where c.idExperimento = exp.id and exp.id = '" + str(idExperimento) + "';"
        )

    combinacoes = []
    combinacoes.clear()

    for x in c.fetchall():
        combinacoes.append(x)

    return combinacoes