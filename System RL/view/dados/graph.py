# coding: utf-8
# import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt
from view.bd import query

def run(dict_config):
	numEnsaios = query.getMAXofEnsaios(dict_config["experimento_id"])
	numCombinacoes = query.getCombinacoes(dict_config["experimento_id"])
	resultados = query.getDados(dict_config["experimento_id"])

	combinacoes = []
	for x in resultados:
	    comb = str("TA:"+x[1]+" FD:"+x[2]+" EG:"+x[3])
	    combinacoes.append(comb)

	medias = []
	for x in resultados:
	    medias.append(x[5])

	y_pos = np.arange(len(combinacoes))

	plt.bar(y_pos, medias, align='center', alpha=0.5)
	plt.xticks(y_pos, combinacoes)
	plt.ylabel('Combinações')
	plt.title('Programming language usage')

	plt.show()

	# -----------------------------------------------------------
	# numEnsaios = query.getMAXofEnsaios(dict_config["experimento_id"])
	# numCombinacoes = query.getCombinacoes(dict_config["experimento_id"])
	# resultados = query.getDados(dict_config["experimento_id"])

	# combinacoes = []
	# for x in resultados:
	#     comb = str("TA:"+x[1]+" FD:"+x[2]+" EG:"+x[3])
	#     combinacoes.append(comb)

	# combinacoes.append("Média")

	# medias = []
	# for x in range(numEnsaios):


	# notas_pedro = [8, 9, 7, 8]
	# notas_maria = [5, 10, 6, 9]
	# notas_jose = [7, 7, 5, 8]

	# # Definindo a largura das barras
	# barWidth = 0.25

	# # Aumentando o gráfico
	# plt.figure(figsize=(10, 5))

	# # Definindo a posição das barras
	# r1 = np.arange(len(notas_pedro))
	# r2 = [x + barWidth for x in r1]
	# r3 = [x + barWidth for x in r2]

	# # criando as barras
	# plt.bar(r1, notas_pedro, color='#6A5ACD', width=barWidth, label='Pedro')
	# plt.bar(r2, notas_maria, color='#6495ED', width=barWidth, label='Maria')
	# plt.bar(r3, notas_jose, color='#00BFFF', width=barWidth, label='José')

	# # Adicionando legendas as barras
	# plt.xlabel('Provas')
	# plt.xticks([r + barWidth for r in range(len(notas_pedro))], combinacoes)
	# plt.ylabel('Notas')
	# plt.title( 'Representação das notas de 3 alunos e 4 provas do semestre')

	# # criando a legenda e exibindo o gráfico
	# plt.legend(
	#     loc='upper center', 
	#     bbox_to_anchor=(0.5, -0.02), 
	#     fancybox=True, 
	#     shadow=True, 
	#     ncol=numEnsaios)
	# plt.show()

	#  ================================================================
	# notas_pedro = [8, 9, 7, 8]
	# notas_maria = [5, 10, 6, 9]
	# notas_jose = [7, 7, 5, 8]

	# # Definindo a largura das barras
	# barWidth = 0.25

	# # Aumentando o gráfico
	# plt.figure(figsize=(10, 5))

	# # Definindo a posição das barras
	# r1 = np.arange(len(notas_pedro))
	# r2 = [x + barWidth for x in r1]
	# r3 = [x + barWidth for x in r2]

	# # criando as barras
	# plt.bar(r1, notas_pedro, color='#6A5ACD', width=barWidth, label='Pedro')
	# plt.bar(r2, notas_maria, color='#6495ED', width=barWidth, label='Maria')
	# plt.bar(r3, notas_jose, color='#00BFFF', width=barWidth, label='José')

	# # Adicionando legendas as barras
	# plt.xlabel('Provas')
	# plt.xticks([r + barWidth for r in range(len(notas_pedro))], ['Prova 1', 'Prova 2', 'Prova 3', 'Prova 4'])
	# plt.ylabel('Notas')
	# plt.title( 'Representação das notas de 3 alunos e 4 provas do semestre')

	# # criando a legenda e exibindo o gráfico
	# plt.legend(
	#     loc='upper center', 
	#     bbox_to_anchor=(0.5, -0.02), 
	#     fancybox=True, 
	#     shadow=True, 
	#     ncol=3)
	# plt.show()
	# -----------------------------------------------------------
