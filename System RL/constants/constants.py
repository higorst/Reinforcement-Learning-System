import os
import subprocess

input_ = "who"
var = subprocess.getoutput(input_)
var = var.split()
user_name = var[0]

# --------------------------------------------------------------
# For All System of Reinforcement Learning
# --------------------------------------------------------------

# --------------------------------------------------------------
# Colors
# --------------------------------------------------------------
backgroundColor 		= "#fff"
backgroundColorInfo		= "#42a5f5"
butonColor 				= "#fff"
butonColorInfo 			= "#42a5f5"
borderColorButtonInfo	= "#64b5f6"
buttonStartActive		= "#2286c3"
buttonStopColor			= "#d32f2f"
buttonStopColorActive	= "#9a0007"
buttonColorConfig		= "#4caf50"
buttonColorConfigActive	= "#087f23"
letterColor 			= "#000"
activeButtonColor		= "#fb8c00"
buttonHighLight			= "#fb8c00"
activeButtonColorInfo	= "#0077c2"

listboxBG				= "#757575"
listboxFG				= "#fff"

# --------------------------------------------------------------
# Title
# --------------------------------------------------------------
titleHome 				= "Sistema de Aprendizado por Reforço para Futebol de Robôs"
titleButtonInfoMessage	= "OK"
titleTelaInicial 		= titleHome
titleTelaInfo	 		= "Como iniciar uma simulação"
titleTela01				= titleHome
titleTela02				= titleHome
titleTela03				= titleHome
titleTela04				= titleHome
titleTela05				= titleHome
titleCopyright			= "Copyright 2020 : UFRBots"
titleAskDirectory		= "Acesse diretório do time"

# --------------------------------------------------------------
# Title"s Button
# --------------------------------------------------------------
btTelaInicial 			= "Voltar"
btMenu		 			= "Menu"
btInfo					= "Info"
btStart					= "Iniciar Partida"
btAguarde				= "Aguarde"
btStop					= "Finalizar"
btInfoBack				= "Entendi"
btExit 					= "Sair"
btTelaInicial01 		= "Nova Partida"
btTelaInicial02 		= "Aprendizado"
btTelaInicial03 		= "Assistir Partidas"
btTelaInicial04 		= "Tutorial"
btTelaInicial05 		= "Sobre"
btGetTeam01				= "Time 1"
btGetTeam02				= "Time 2"
btModoMatchFast			= "Modo Rápido"
btModoMatchNormal		= "Modo Normal"
btModoViewActive		= "Monitor Ativado"
btModoViewInactive		= "Monitor Desativado"

# --------------------------------------------------------------
# String
# --------------------------------------------------------------
stringInfo00 			= "Você deve selecionar dois \ntimes para poder prosseguir!"
stringInfo01			= "[1] Navegue até o diretório \ndos times!"
stringInfo02 			= "[2] Escolha um dos times \ndisponíveis!"
stringInfo03 			= "[3] Entre na pasta do time!"
stringInfo04			= "[4] Pressione"
stringForNameTeam		= "set team  = "
msgWinner				= " VENCEU!"
msgEmpate				= "EMPATE"
msgCloseMonitor			= "FECHE O MONITOR!"
stringPlacar			= "Placar"
stringXPlacar			= "X"

msgSucess				= "Sucesso"
msgSetParms				= "Verificando parâmetros ...\n"
msgCriarMatriz			= "Criando Matriz"
msgConfigTeam			= "Configurando Time de Aprendizado!\nAguarde .."
msgReiniciarPartida		= "Ocorreu um erro e a partida precisa ser reiniciada!"

ERROR					= "9999"

labelEpisodes			= "Episódios"
labelAlpha				= "Taxa de Aprendizado"
labelGamma				= "Fator de Desconto"
labelEpsilon			= "Política e-greedy"
labelAlgorithm			= "Algoritmo"
labelMatriz				= "Matriz"
labelResultTeam			= "AR    x    Res"
labelResult 			= "Resultados:"
labelLearning			= "Aprendendo .."

btAfterAR				= "Iniciar"
btAfterAguarde			= "Aguarde"
btBeforeAR				= "Resultados"

labelGRAPH_AR			= "Gols AR"
labelGRAPH_Res			= "Gols Reserva"
labelGRAPH_Saldo		= "Saldo de Gols"

infoLogplayer			= "Selecione uma opção e clique em \"Assistir\"\nFeche o monitor logplayer para acessar o sistema novamente!"
msgToSelectLogplayer	= "Selecione primeiro uma opção!"
titleLogplayer			= "Monitor de Partidas AR"

# --------------------------------------------------------------
# Popup
# --------------------------------------------------------------
titlePopup				= "INFO"
infoEpisodes			= "Número total de partidas\n** Deve ser nº inteiro"
infoAlpha				= "Taxa de aprendizado\n** Deve ser nº entre 0 - 1"
infoGamma				= "Fator de desconto\n** Deve ser nº entre 0 - 1"
infoEpsilon				= "Aleatoriedade na escola das ações. Ex: 0.1 -> 10%\n** Deve ser nº entre 0 - 1"
infoAlgorithm			= "Algoritmo de aprendizado por reforço\n** Apenas o Q_Learning está disponível"
infoMatriz				= "Matriz Q de aprendizado"
sizePopup				= "400x50+500+300"

# --------------------------------------------------------------
# Address
# --------------------------------------------------------------
addressFileConstants	= "/home/" + user_name + "/.System RL/constants/constants.py"
addressFilePlayerTeams	= "/home/" + user_name + "/Documents/AR_System/src/PlayerTeams.cpp"
addressFileMatriz		= "/home/" + user_name + "/Documents/AR_System/q.txt"

addressFileDesktop		= "/home/" + user_name + "/.System\ RL/System RL.desktop"
moveFileDesktop			= "cd && cp -r /home/" + user_name + "/.System RL/System\ RL.desktop /usr/share/applications/"
moveFileDesktop2		= "cd && cp -r /usr/share/applications/System RL.desktop /home/" + user_name + "/Desktop/"
commandExec				= "python3 /home/" + user_name + "/.System\ RL/TelaInicial.py"
commandIcon				= "/home/" + user_name + "/.System\ RL/img/logo.png"

addressTeamArSystem		= "/home/" + user_name + "/Documents/AR_System"
addressTeamArName		= "AR"
addressTeamResSystem	= "/home/" + user_name + "/Documents/Reserva_AR_System/"
addressTeamResName		= "Reserva"

addressLogo 			= "/home/" + user_name + "/.System RL/img/logo.png"
initialDirectory		= "/home/" + user_name + "/Documents/"
archiveToReadTeam		= "/start.sh"
openInfoOsSytem			= "python3 /home/" + user_name + "/.System\ RL/info.py"
addressInfo01			= "/home/" + user_name + "/.System RL/img/info01.jpeg"
addressInfo02			= "/home/" + user_name + "/.System RL/img/info02.jpeg"
addressInfo03			= "/home/" + user_name + "/.System RL/img/info03.jpeg"
addressVS				= "/home/" + user_name + "/.System RL/img/vs.png"
addressFootbalField		= "/home/" + user_name + "/.System RL/img/footbal.png"
addressRefresh			= "/home/" + user_name + "/.System RL/img/refresh.png"
addressInfo				= "/home/" + user_name + "/.System RL/img/info.png"
addressHome				= "/home/" + user_name + "/.System RL/img/home.png"
addressAR				= "/home/" + user_name + "/.System RL/img/rocket.png"
addressExit				= ""
fileFreedom				= "/home/" + user_name + "/.log/freedom.txt"
createLogDir			= "cd && rm -r /home/" + user_name + "/.log && mkdir /home/" + user_name + "/.log"

addressDirAR			= "/home/" + user_name + "/Documents/AR_System"
addressPercent_1		= "/home/" + user_name + "/.System RL/img/percent_1.png"
addressPercent_2		= "/home/" + user_name + "/.System RL/img/percent_2.png"
addressPercent_3		= "/home/" + user_name + "/.System RL/img/percent_3.png"

addressDate				= "/home/" + user_name + "/.System RL/img/date.png"
addressHour				= "/home/" + user_name + "/.System RL/img/hour.png"
addressScoreboard		= "/home/" + user_name + "/.System RL/img/scoreboard.png"

addressPlay				= "/home/" + user_name + "/.System RL/img/play.png"
addressMovie01			= "/home/" + user_name + "/.System\ RL/movie/video01.mp4"
addressMovie02			= "/home/" + user_name + "/.System\ RL/movie/video02.mp4"
addressMovie03			= "/home/" + user_name + "/.System\ RL/movie/video03.mp4"
addressMovie01Time		= 38
addressMovie02Time		= 43
addressMovie03Time		= 21


# --------------------------------------------------------------
# Config
# --------------------------------------------------------------
viewSize				= "800x600+300+50"
fontPersonalizada 		= "Ubuntu"
fontPersonalizadaTeam	= "Purisa"
fontPersonalizadaPlacar = "DS-Digital"
fontSizeTitleTelaIn		= 20
fontSizeTitleTelaInfo	= 11 
fontSizePlacar			= 28
fontSizeTeamName		= 15
fontSizeCopyright		= 9
timeOfMatch				= 170
sizeIconInfo			= 12

fontPersonalizadaList	= "consolas"

fontPersonalizadaDesc	= "Ubuntu"
fontSizeDesc			= 12


commandCriarPastaLog	= "cd && rm -r /home/" + user_name + "/.log && mkdir /home/" + user_name + "/.log"

# --------------------------------------------------------------
# Dimensions
# --------------------------------------------------------------
widthLabelTeam 			= 18
widthLabelFinal 		= 50
proportionInfoImage		= 1.6
proportionVSImage		= 12
xLenghtLabelTeam		= 250
yLenghtLabelMessage		= 100