/*
Copyright (c) 2000-2003, Jelle Kok, University of Amsterdam
All rights reserved.

Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions are met:

1. Redistributions of source code must retain the above copyright notice, this
list of conditions and the following disclaimer.

2. Redistributions in binary form must reproduce the above copyright notice,
this list of conditions and the following disclaimer in the documentation
and/or other materials provided with the distribution.

3. Neither the name of the University of Amsterdam nor the names of its
contributors may be used to endorse or promote products derived from this
software without specific prior written permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE
FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
*/

/*! \file PlayerTeams.cpp
<pre>
<b>File:</b>          PlayerTest.cpp
<b>Project:</b>       Robocup Soccer Simulation Team: UvA Trilearn
<b>Authors:</b>       Jelle Kok
<b>Created:</b>       10/12/2000
<b>Last Revision:</b> $ID$
<b>Contents:</b>      This file contains the class definitions for the
                      Player that are used to test the teams' high level
                      strategy.
<hr size=2>
<h2><b>Changes</b></h2>
<b>Date</b>             <b>Author</b>          <b>Comment</b>
10/12/2000        Jelle Kok       Initial version created
</pre>
*/

/*Modificado por: Andre Luiz C. Ottoni
UaiSoccer2D - UFSJ
27 de Janeiro de 2011*/

#include "Player.h"
#include "Objects.h"
#include <iostream>
#include <sstream>
#include <string>
#include <cstdlib>
#include <stdlib.h>

using namespace std;

float q[32][6]; // matriz aprendizado
float r[2][8];  // matriz reforço

int resultado_acao = 3;
float x, y, yball, xball = 0;
int acao, s_plus;
int agente;
float maior[32] = {-9999999, -9999999, -9999999, -9999999, -9999999, -9999999, -9999999, -9999999, -9999999,
                   -9999999, -9999999, -9999999, -9999999, -9999999, -9999999, -9999999, -9999999, -9999999,
                   -9999999, -9999999, -9999999, -9999999, -9999999, -9999999, -9999999, -9999999, -9999999,
                   -9999999, -9999999, -9999999, -9999999, -9999999
                  };
int indice[32];
int coluna;
string nome_acao;

/*!This method is the first complete simple team and defines the actions taken
   by all the players on the field (excluding the goalie). It is based on the
   high-level actions taken by the simple team FC Portugal that it released in
   2000. The players do the following:
   - if ball is kickable
       kick ball to goal (random corner of goal)
   - else if i am fastest player to ball 
       intercept the ball
   - else
       move to strategic position based on your home position and pos ball */
int verificar_celula(float x, float y)
{

   // Bloco A
   if (x < -36.0)
   {
      coluna = 0;
      if (y <= -20.16)
      {
         return 1;
      }
      else if (y > -20.16 and y <= 0)
      {
         return 2;
      }
      else if (y > 0 and y <= 20.16)
      {
         return 3;
      }
      else
      {
         return 4;
      }      
   }

   // Bloco B
   else if (x >= -36.0 and x < -34.0)
   {
      coluna = 1;
      if (y <= -20.16)
      {
         return 5;
      }
      else if (y > -20.16 and y <= 0)
      {
         return 6;
      }
      else if (y > 0 and y <= 20.16)
      {
         return 7;
      }
      else
      {
         return 8;
      }      
   }

   // Bloco C
   else if (x >= -34.0 and x < -12.5)
   {
      coluna = 2;
      if (y <= -20.16)
      {
         return 9;
      }
      else if (y > -20.16 and y <= 0)
      {
         return 10;
      }
      else if (y > 0 and y <= 20.16)
      {
         return 11;
      }
      else
      {
         return 12;
      }      
   }

   // Bloco D
   else if (x >= -12.5 and x < 0)
   {
      coluna = 3;
      if (y <= -20.16)
      {
         return 13;
      }
      else if (y > -20.16 and y <= 0)
      {
         return 14;
      }
      else if (y > 0 and y <= 20.16)
      {
         return 15;
      }
      else
      {
         return 16;
      }      
   }

   // Bloco E
   else if (x >= 0 and x < 12.5)
   {
      coluna = 4;
      if (y <= -20.16)
      {
         return 17;
      }
      else if (y > -20.16 and y <= 0)
      {
         return 18;
      }
      else if (y > 0 and y <= 20.16)
      {
         return 19;
      }
      else
      {
         return 20;
      }      
   }

   // Bloco F
   else if (x >= 12.5 and x < 25)
   {
      coluna = 5;
      if (y <= -20.16)
      {
         return 21;
      }
      else if (y > -20.16 and y <= 0)
      {
         return 22;
      }
      else if (y > 0 and y <= 20.16)
      {
         return 23;
      }
      else
      {
         return 24;
      }      
   }

   // Bloco G
   else if (x >= 25 and x < 32)
   {
      coluna = 6;
      if (y <= -20.16)
      {
         return 25;
      }
      else if (y > -20.16 and y <= 0)
      {
         return 26;
      }
      else if (y > 0 and y <= 20.16)
      {
         return 27;
      }
      else
      {
         return 28;
      }      
   }

   // Bloco H
   else if (x >= 32)
   {
      coluna = 7;
      if (y <= -20.16)
      {
         return 29;
      }
      else if (y > -20.16 and y <= 0)
      {
         return 30;
      }
      else if (y > 0 and y <= 20.16)
      {
         return 31;
      }
      else
      {
         return 32;
      }      
   }
}
void ler_matriz_arquivo()
{ // Retorna uma matriz 18x6 lida do arquivo

   //int leitura[18][6];

   FILE *fp;
   fp = fopen("q.txt", "r"); // Abre o arquivo somente para leitura
   if (fp == NULL)
   {
      perror("Erro ao abrir o arquivo.\n");
   }
   else
   {
      //printf("Leitura do arquivo\n");
      for (int i = 0; i < 32; i++)
      {
         for (int j = 0; j < 6; j++)
         {
            fscanf(fp, "%f ", &q[i][j]);
         }
      }
   }
   fclose(fp);

   FILE *f;
   f = fopen("r.txt", "r"); // Abre o arquivo somente para leitura
   if (f == NULL)
   {
      perror("Erro ao abrir o arquivo.\n");
   }
   else
   {
      //printf("Leitura do arquivo\n");
      for (int i = 0; i < 2; i++)
      {
         for (int j = 0; j < 8; j++)
         {
            fscanf(f, "%f ", &r[i][j]);
         }
      }
   }
   fclose(f);
}
void escrever_arquivo()
{ // Escreve no arquivo uma matriz 18x8
   FILE *fp;
   fp = fopen("q.txt", "w");

   if (fp == NULL)
   {
      perror("Erro ao abrir o arquivo.\n");
      return;
   }
   else
   {
      printf("        CHUTAR   CLEAR_B      P_N       P_F       D_W       D_F\n");
      for (int i = 0; i < 32; i++)
      {
         if (i == 0)
         {
            printf(" A1  |");
         }
         else if (i == 1)
         {
            printf(" A2  |");
         }
         else if (i == 2)
         {
            printf(" A3  |");
         }
         else if (i == 3)
         {
            printf(" A4  |");
         }
         else if (i == 4)
         {
            printf(" B5  |");
         }
         else if (i == 5)
         {
            printf(" B6  |");
         }
         else if (i == 6)
         {
            printf(" B7  |");
         }
         else if (i == 7)
         {
            printf(" B8  |");
         }
         else if (i == 8)
         {
            printf(" C9  |");
         }
         else if (i == 9)
         {
            printf(" C10 |");
         }
         else if (i == 10)
         {
            printf(" C11 |");
         }
         else if (i == 11)
         {
            printf(" C12 |");
         }
         else if (i == 12)
         {
            printf(" D13 |");
         }
         else if (i == 13)
         {
            printf(" D14 |");
         }
         else if (i == 14)
         {
            printf(" D15 |");
         }
         else if (i == 15)
         {
            printf(" D16 |");
         }
         else if (i == 16)
         {
            printf(" E17 |");
         }
         else if (i == 17)
         {
            printf(" E18 |");
         }
         else if (i == 18)
         {
            printf(" E19 |");
         }
         else if (i == 19)
         {
            printf(" E20 |");
         }
         else if (i == 20)
         {
            printf(" F21 |");
         }
         else if (i == 21)
         {
            printf(" F22 |");
         }
         else if (i == 22)
         {
            printf(" F23 |");
         }
         else if (i == 23)
         {
            printf(" F24 |");
         }
         else if (i == 24)
         {
            printf(" G25 |");
         }
         else if (i == 25)
         {
            printf(" G26 |");
         }
         else if (i == 26)
         {
            printf(" G27 |");
         }
         else if (i == 27)
         {
            printf(" G28 |");
         }
         else if (i == 28)
         {
            printf(" H29 |");
         }
         else if (i == 29)
         {
            printf(" H30 |");
         }
         else if (i == 30)
         {
            printf(" H31 |");
         }
         else if (i == 31)
         {
            printf(" H32 |");
         }
         maior[i] = -9999999;
         for (int j = 0; j < 6; j++)
         {
            if (q[i][j] == -0.00)
            {
               q[i][j] = 0.00;
            }
            // escrita no arquivo
            fprintf(fp, "%.2f ", q[i][j]);

            // guardar a melhor ação para cada estado
            if (maior[i] < q[i][j])
            {
               maior[i] = q[i][j];
               indice[i] = j;
            }

            // um algarismo negativo
            if ((q[i][j] < 0) and (q[i][j] > -10))
            {
               printf("   %.2f |", q[i][j]);
            }
            // dois algarismos negativos
            else if ((q[i][j] < 0) and (q[i][j] <= -10) and (q[i][j] > -100))
            {
               printf("  %.2f |", q[i][j]);
            }
            // três algarismos negativos
            else if ((q[i][j] <= -100))
            {
               printf(" %.2f |", q[i][j]);
            }

            // um algarismo positivo
            else if ((q[i][j] >= 0) and (q[i][j] < 10))
            {
               printf("    %.2f |", q[i][j]);
            }
            // dois algarismos positivos
            else if ((q[i][j] >= 0) and (q[i][j] < 100))
            {
               printf("   %.2f |", q[i][j]);
            }
            // três algarismos positivos
            else if ((q[i][j] >= 0) and (q[i][j] >= 100) and (q[i][j] < 1000))
            {
               printf("  %.2f |", q[i][j]);
            }
            // quatro algarismos
            else if ((q[i][j] >= 0) and (q[i][j] >= 1000) and (q[i][j] < 10000))
            {
               printf(" %.2f |", q[i][j]);
            }
            // cinco algarismos
            else
            {
               printf("%.2f |", q[i][j]);
            }
         }
         fprintf(fp, "\n");
         printf("\n");
      }
   }

   printf("\n");
   int aux = 1;

   for (int i = 0; i < 32; ++i)
   {
      if (i == 0)
      {
         printf(" A1  > ");
      }
      else if (i == 1)
      {
         printf("A2  > ");
      }
      else if (i == 2)
      {
         printf("A3  > ");
      }
      else if (i == 3)
      {
         printf("A4  > ");
      }
      else if (i == 4)
      {
         printf(" B5  > ");
      }
      else if (i == 5)
      {
         printf("B6  > ");
      }
      else if (i == 6)
      {
         printf("B7  > ");
      }
      else if (i == 7)
      {
         printf("B8  > ");
      }
      else if (i == 8)
      {
         printf(" C9  > ");
      }
      else if (i == 9)
      {
         printf("C10 > ");
      }
      else if (i == 10)
      {
         printf("C11 > ");
      }
      else if (i == 11)
      {
         printf("C12 > ");
      }
      else if (i == 12)
      {
         printf(" D13 > ");
      }
      else if (i == 13)
      {
         printf("D14 > ");
      }
      else if (i == 14)
      {
         printf("D15 > ");
      }
      else if (i == 15)
      {
         printf("D16 > ");
      }
      else if (i == 16)
      {
         printf(" E17 > ");
      }
      else if (i == 17)
      {
         printf("E18 > ");
      }
      else if (i == 18)
      {
         printf("E19 > ");
      }
      else if (i == 19)
      {
         printf("E20 > ");
      }
      else if (i == 20)
      {
         printf(" F21 > ");
      }
      else if (i == 21)
      {
         printf("F22 > ");
      }
      else if (i == 22)
      {
         printf("F23 > ");
      }
      else if (i == 23)
      {
         printf("F24 > ");
      }
      else if (i == 24)
      {
         printf(" G25 > ");
      }
      else if (i == 25)
      {
         printf("G26 > ");
      }
      else if (i == 26)
      {
         printf("G27 > ");
      }
      else if (i == 27)
      {
         printf("G28 > ");
      }
      else if (i == 28)
      {
         printf(" H29 > ");
      }
      else if (i == 29)
      {
         printf("H30 > ");
      }
      else if (i == 30)
      {
         printf("H31 > ");
      }
      else if (i == 31)
      {
         printf("H32 > ");
      }

      // melhor ação
      if (indice[i] == 0)
      {
         printf("CHUTAR    ");
      }
      else if (indice[i] == 1)
      {
         printf("CLEAR_B   ");
      }
      else if (indice[i] == 2)
      {
         printf("PASS_N    ");
      }
      else if (indice[i] == 3)
      {
         printf("PASS_F    ");
      }
      else if (indice[i] == 4)
      {
         printf("DRIBLE_N  ");
      }
      else if (indice[i] == 5)
      {
         printf("DRIBLE_F  ");
      }

      if (aux == 4)
      {
         printf("\n");
         aux = 1;
      }
      else
      {
         aux++;
      }
   }
   fclose(fp);
}
int definir_acao(int celula_)
{
   int acao;
   float n;
   float e_greedy = 0.1;
   n = rand() % 100 + 1;
   n = n/100;
   if (n < e_greedy)
   {
      acao = rand() % 6 + 1;
   }
   else
   {
      float maior_ = q[celula_ - 1][0];
      acao = 1;
      bool zerado = true;
      for (int i = 0; i < 6; i++)
      {
         if (q[celula_ - 1][i] > maior_)
         {
            maior_ = q[celula_ - 1][i];
            acao = i + 1;
         }
         if (zerado and q[celula_ - 1][i] != 0)
         {
            zerado = false;
         }
      }
      if (zerado)
      {
         acao = rand() % 6 + 1;
      }
   }
   return acao;
}
float getMax(int col) // O maior valor para a ação
{
   s_plus = verificar_celula(xball, yball);
   s_plus -= 1;
   float _maior = q[s_plus][0];
   for (int i = 1; i < 6; i++)
   {
      if (q[s_plus][i] > _maior)
      {
         _maior = q[s_plus][i];
      }
   }
   s_plus += 1;
   return _maior;
}
/* legenda para 'resultado_acao'
   - 0 >> ação requisitada
   - 1 >> ação resultou em um resultado efetivo
   - 2 >> ação resultou em um resultado negativo
*/
void q_learning(float x, float y, int acao, int jogador, int resultado_acao)
{
   // ------------------------------------- Q- learning
   float q_t, q_t_plus, reforco, max;
   float alpha = 0.125;
   float gamma = 0.9;
   
   int celula = verificar_celula(x, y); // Verifica qual célula o agente está
   int linha = 0;

   float mQ = getMax(acao - 1) * gamma;
   //max = getMax(acao - 1);        // pega maior valor de Q da tabela

   if(acao == 1){
      if(celula == 30 or celula == 31){
         resultado_acao = 1; // sempre recompensa para essa célula para o chute
      }
      else{
         resultado_acao = 2; // sempre penalidade as demais células para o chute
      }
   }
   else
   {
      if(celula == 30 or celula == 31) // para qualquer ação dierente de chute - penalidade
      {
         resultado_acao = 2;
      }      
   }

   if (resultado_acao == 1)
   {
      linha = 0; // linha superior do arquivo de reforço - recompensa
   }
   else
   {
      linha = 1; // linha inferior do arquivo de reforço - penalidade
   }
   

   q_t = q[celula - 1][acao - 1]; // valor atual de aprendizagem
   reforco = r[linha][coluna];    // valor de reforço

   if(acao == 1){
      if(resultado_acao == 1){
         reforco += 500;
      }else{
         reforco -= 500;
      }
   }   

   // Equação do Q_learning - novo valor de aprendizado para um par (s, a)
   // float mQ = gamma * max;
   q_t_plus = q_t + alpha * (reforco + mQ - q_t);

   // atualização de valor de aprendizagem para a tabela
   q[celula - 1][acao - 1] = q_t_plus;

   escrever_arquivo();
   // ------------------------------------- Q- learning
}

SoccerCommand Player::deMeer5()
{
   ler_matriz_arquivo();
   SoccerCommand soc(CMD_ILLEGAL);
   VecPosition posAgent = WM->getAgentGlobalPosition();
   VecPosition posBall = WM->getBallPos();
   int iTmp;
   xball = posBall.getX();
   yball = posBall.getY();

   if (WM->isBeforeKickOff())
   {
      if (WM->isKickOffUs() && WM->getPlayerNumber() == 9) // 9 takes kick
      {
         if (WM->isBallKickable())
         {
            // if(pode_marcar == 0 and WM->getCurrentCycle() > 10 and WM->getCurrentCycle() !=3000 and WM->getCurrentCycle()<6000){
            //    gs += 1;
            //    pode_marcar = 1;
            //    gol_sofrido();
            // }
            //Toca a bola para o 8 no inicio do jogo
            VecPosition posAgent_passe8 = WM->getGlobalPosition(OBJECT_TEAMMATE_8);
            soc = directPass(posAgent_passe8, PASS_NORMAL);
            Log.log(100, "take kick off");
         }
         else
         {
            soc = intercept(false);
            Log.log(100, "move to ball to take kick-off");
         }
         ACT->putCommandInQueue(soc);
         ACT->putCommandInQueue(turnNeckToObject(OBJECT_BALL, soc));
         return soc;
      }
      if (formations->getFormation() != FT_INITIAL || // not in kickoff formation
          posAgent.getDistanceTo(WM->getStrategicPosition()) > 2.0)
      {
         formations->setFormation(FT_INITIAL); // go to kick_off formation
         ACT->putCommandInQueue(soc = teleportToPos(WM->getStrategicPosition()));
      }
      else // else turn to center
      {
         ACT->putCommandInQueue(soc = turnBodyToPoint(VecPosition(0, 0), 0));
         ACT->putCommandInQueue(alignNeckWithBody());
      }
   }
   else
   {
      formations->setFormation(FT_433_OFFENSIVE);
      soc.commandType = CMD_ILLEGAL;
      if (WM->getConfidence(OBJECT_BALL) < PS->getBallConfThr())
      {
         ACT->putCommandInQueue(soc = searchBall());  // if ball pos unknown
         ACT->putCommandInQueue(alignNeckWithBody()); // search for it
      }
      else if (WM->isBallKickable()) // if kickable
      {
         xball = posBall.getX();
         yball = posBall.getY();
         ////////////////////////////////////
         if (resultado_acao == 0 and WM->getCurrentCycle() < 6000)
         {
            resultado_acao = 1; // indica resultado positivo de ação
            xball = posBall.getX();
            q_learning(x, y, acao, agente, resultado_acao);
         }
         ////////////////////////////////////

         //Declaracao de objetos de posiocionamento de jogadores
         VecPosition posGoal(PITCH_LENGTH / 2.0, (-1 + 2 * (WM->getCurrentCycle() % 2)) * 0.4 * SS->getGoalWidth());
         VecPosition posAgent_passe6 = WM->getGlobalPosition(OBJECT_TEAMMATE_6);
         VecPosition posAgent_passe7 = WM->getGlobalPosition(OBJECT_TEAMMATE_7);
         VecPosition posAgent_passe8 = WM->getGlobalPosition(OBJECT_TEAMMATE_8);
         VecPosition posAgent_passe9 = WM->getGlobalPosition(OBJECT_TEAMMATE_9);
         VecPosition posAgent_passe10 = WM->getGlobalPosition(OBJECT_TEAMMATE_10);
         VecPosition posAgent_passe11 = WM->getGlobalPosition(OBJECT_TEAMMATE_11);

         //Verifica o oponente mais rapido para a bola
         int tempoAdv;
         ObjectT Ladrao = WM->getFastestInSetTo(OBJECT_SET_OPPONENTS, OBJECT_BALL, &tempoAdv);
         VecPosition posLadrao = WM->getGlobalPosition(Ladrao);
         //Calcula a distancia desse oponente, margem segura para posse bola
         //Caso essa margem for pequena o jogador passa a bola ou chuta
         int dxl = posAgent.getX() - posLadrao.getX();
         int dyl = posAgent.getY() - posLadrao.getY();
         int distl = (int)sqrt(dxl * dxl + dyl * dyl);

         x = posAgent.getX();
         y = posAgent.getY();

         //Escolhe qual o agente
         switch (WM->getPlayerNumber())
         {
         case 2:
            // ------------------------------------- Q- learning
            acao = definir_acao(verificar_celula(x, y));
            if (acao == 1)
            { // chutar ao gol
               soc = kickTo(posGoal, SS->getBallSpeedMax());
               nome_acao = "       CHUTAR     ";
            }
            else if (acao == 2)
            {
               soc = clearBall(CLEAR_BALL_OFFENSIVE, SIDE_ILLEGAL, NULL);
               nome_acao = "     CLEAR_BALL   ";
            }
            else if (acao == 3)
            {
               soc = directPass(posAgent_passe6, PASS_NORMAL);
               nome_acao = "    PASS_NORMAL   ";
            }
            else if (acao == 4)
            {
               soc = directPass(posAgent_passe7, PASS_FAST);
               nome_acao = "     PASS_FAST    ";
            }
            else if (acao == 5)
            {
               soc = dribble(0, DRIBBLE_WITHBALL);
               nome_acao = " DRIBBLE_WITHBALL ";
            }
            else
            {
               soc = dribble(0, DRIBBLE_FAST);
               nome_acao = "   DRIBBLE_FAST   ";
            }
            resultado_acao = 0;
            agente = 2;
            // ------------------------------------- Q- learning
            break;
         case 3:
            // ------------------------------------- Q- learning
            acao = definir_acao(verificar_celula(x, y));
            if (acao == 1)
            { // chutar ao gol
               soc = kickTo(posGoal, SS->getBallSpeedMax());
               nome_acao = "       CHUTAR     ";
            }
            else if (acao == 2)
            {
               soc = clearBall(CLEAR_BALL_OFFENSIVE, SIDE_ILLEGAL, NULL);
               nome_acao = "     CLEAR_BALL   ";
            }
            else if (acao == 3)
            {
               soc = directPass(posAgent_passe6, PASS_NORMAL);
               nome_acao = "    PASS_NORMAL   ";
            }
            else if (acao == 4)
            {
               soc = directPass(posAgent_passe7, PASS_FAST);
               nome_acao = "     PASS_FAST    ";
            }
            else if (acao == 5)
            {
               soc = dribble(0, DRIBBLE_WITHBALL);
               nome_acao = " DRIBBLE_WITHBALL ";
            }
            else
            {
               soc = dribble(0, DRIBBLE_FAST);
               nome_acao = "   DRIBBLE_FAST   ";
            }
            resultado_acao = 0;
            agente = 3;
            // ------------------------------------- Q- learning
            break;
         case 4:
            // ------------------------------------- Q- learning
            acao = definir_acao(verificar_celula(x, y));
            if (acao == 1)
            { // chutar ao gol
               soc = kickTo(posGoal, SS->getBallSpeedMax());
               nome_acao = "       CHUTAR     ";
            }
            else if (acao == 2)
            {
               soc = clearBall(CLEAR_BALL_OFFENSIVE, SIDE_ILLEGAL, NULL);
               nome_acao = "     CLEAR_BALL   ";
            }
            else if (acao == 3)
            {
               soc = directPass(posAgent_passe6, PASS_NORMAL);
               nome_acao = "    PASS_NORMAL   ";
            }
            else if (acao == 4)
            {
               soc = directPass(posAgent_passe8, PASS_FAST);
               nome_acao = "     PASS_FAST    ";
            }
            else if (acao == 5)
            {
               soc = dribble(0, DRIBBLE_WITHBALL);
               nome_acao = " DRIBBLE_WITHBALL ";
            }
            else
            {
               soc = dribble(0, DRIBBLE_FAST);
               nome_acao = "   DRIBBLE_FAST   ";
            }
            resultado_acao = 0;
            agente = 4;
            // ------------------------------------- Q- learning
            break;
         case 5:
            // ------------------------------------- Q- learning
            acao = definir_acao(verificar_celula(x, y));
            if (acao == 1)
            { // chutar ao gol
               soc = kickTo(posGoal, SS->getBallSpeedMax());
               nome_acao = "       CHUTAR     ";
            }
            else if (acao == 2)
            {
               soc = clearBall(CLEAR_BALL_OFFENSIVE, SIDE_ILLEGAL, NULL);
               nome_acao = "     CLEAR_BALL   ";
            }
            else if (acao == 3)
            {
               soc = directPass(posAgent_passe6, PASS_NORMAL);
               nome_acao = "    PASS_NORMAL   ";
            }
            else if (acao == 4)
            {
               soc = directPass(posAgent_passe8, PASS_FAST);
               nome_acao = "     PASS_FAST    ";
            }
            else if (acao == 5)
            {
               soc = dribble(0, DRIBBLE_WITHBALL);
               nome_acao = " DRIBBLE_WITHBALL ";
            }
            else
            {
               soc = dribble(0, DRIBBLE_FAST);
               nome_acao = "   DRIBBLE_FAST   ";
            }
            resultado_acao = 0;
            agente = 5;
            // ------------------------------------- Q- learning
            break;
         case 6:
            // ------------------------------------- Q- learning
            acao = definir_acao(verificar_celula(x, y));
            if (acao == 1)
            { // chutar ao gol
               soc = kickTo(posGoal, SS->getBallSpeedMax());
               nome_acao = "       CHUTAR     ";
            }
            else if (acao == 2)
            {
               soc = clearBall(CLEAR_BALL_OFFENSIVE, SIDE_ILLEGAL, NULL);
               nome_acao = "     CLEAR_BALL   ";
            }
            else if (acao == 3)
            {
               soc = directPass(posAgent_passe8, PASS_NORMAL);
               nome_acao = "    PASS_NORMAL   ";
            }
            else if (acao == 4)
            {
               soc = directPass(posAgent_passe7, PASS_FAST);
               nome_acao = "     PASS_FAST    ";
            }
            else if (acao == 5)
            {
               soc = dribble(0, DRIBBLE_WITHBALL);
               nome_acao = " DRIBBLE_WITHBALL ";
            }
            else
            {
               soc = dribble(0, DRIBBLE_FAST);
               nome_acao = "   DRIBBLE_FAST   ";
            }
            resultado_acao = 0;
            agente = 6;
            // ------------------------------------- Q- learning
            break;
         case 7:
            // ------------------------------------- Q- learning
            acao = definir_acao(verificar_celula(x, y));
            if (acao == 1)
            { // chutar ao gol
               soc = kickTo(posGoal, SS->getBallSpeedMax());
               nome_acao = "       CHUTAR     ";
            }
            else if (acao == 2)
            {
               soc = clearBall(CLEAR_BALL_OFFENSIVE, SIDE_ILLEGAL, NULL);
               nome_acao = "     CLEAR_BALL   ";
            }
            else if (acao == 3)
            {
               soc = directPass(posAgent_passe9, PASS_NORMAL);
               nome_acao = "    PASS_NORMAL   ";
            }
            else if (acao == 4)
            {
               soc = directPass(posAgent_passe10, PASS_FAST);
               nome_acao = "     PASS_FAST    ";
            }
            else if (acao == 5)
            {
               soc = dribble(0, DRIBBLE_WITHBALL);
               nome_acao = " DRIBBLE_WITHBALL ";
            }
            else
            {
               soc = dribble(0, DRIBBLE_FAST);
               nome_acao = "   DRIBBLE_FAST   ";
            }
            resultado_acao = 0;
            agente = 7;
            // ------------------------------------- Q- learning
            break;
         case 8:
            // ------------------------------------- Q- learning
            acao = definir_acao(verificar_celula(x, y));
            if (acao == 1)
            { // chutar ao gol
               soc = kickTo(posGoal, SS->getBallSpeedMax());
               nome_acao = "       CHUTAR     ";
            }
            else if (acao == 2)
            {
               soc = clearBall(CLEAR_BALL_OFFENSIVE, SIDE_ILLEGAL, NULL);
               nome_acao = "     CLEAR_BALL   ";
            }
            else if (acao == 3)
            {
               soc = directPass(posAgent_passe11, PASS_NORMAL);
               nome_acao = "    PASS_NORMAL   ";
            }
            else if (acao == 4)
            {
               soc = directPass(posAgent_passe10, PASS_FAST);
               nome_acao = "     PASS_FAST    ";
            }
            else if (acao == 5)
            {
               soc = dribble(0, DRIBBLE_WITHBALL);
               nome_acao = " DRIBBLE_WITHBALL ";
            }
            else
            {
               soc = dribble(0, DRIBBLE_FAST);
               nome_acao = "   DRIBBLE_FAST   ";
            }
            resultado_acao = 0;
            agente = 8;
            // ------------------------------------- Q- learning
            break;
         case 9:
            // ------------------------------------- Q- learning
            acao = definir_acao(verificar_celula(x, y));
            if (acao == 1)
            { // chutar ao gol
               soc = kickTo(posGoal, SS->getBallSpeedMax());
               nome_acao = "       CHUTAR     ";
            }
            else if (acao == 2)
            {
               soc = clearBall(CLEAR_BALL_OFFENSIVE, SIDE_ILLEGAL, NULL);
               nome_acao = "     CLEAR_BALL   ";
            }
            else if (acao == 3)
            {
               soc = directPass(posAgent_passe7, PASS_NORMAL);
               nome_acao = "    PASS_NORMAL   ";
            }
            else if (acao == 4)
            {
               soc = directPass(posAgent_passe10, PASS_FAST);
               nome_acao = "     PASS_FAST    ";
            }
            else if (acao == 5)
            {
               soc = dribble(0, DRIBBLE_WITHBALL);
               nome_acao = " DRIBBLE_WITHBALL ";
            }
            else
            {
               soc = dribble(0, DRIBBLE_FAST);
               nome_acao = "   DRIBBLE_FAST   ";
            }
            resultado_acao = 0;
            agente = 9;
            // ------------------------------------- Q- learning
            break;
         case 10:
            // ------------------------------------- Q- learning
            acao = definir_acao(verificar_celula(x, y));
            if (acao == 1)
            { // chutar ao gol
               soc = kickTo(posGoal, SS->getBallSpeedMax());
               nome_acao = "       CHUTAR     ";
            }
            else if (acao == 2)
            {
               soc = clearBall(CLEAR_BALL_OFFENSIVE, SIDE_ILLEGAL, NULL);
               nome_acao = "     CLEAR_BALL   ";
            }
            else if (acao == 3)
            {
               soc = directPass(posAgent_passe11, PASS_NORMAL);
               nome_acao = "    PASS_NORMAL   ";
            }
            else if (acao == 4)
            {
               soc = directPass(posAgent_passe9, PASS_FAST);
               nome_acao = "     PASS_FAST    ";
            }
            else if (acao == 5)
            {
               soc = dribble(0, DRIBBLE_WITHBALL);
               nome_acao = " DRIBBLE_WITHBALL ";
            }
            else
            {
               soc = dribble(0, DRIBBLE_FAST);
               nome_acao = "   DRIBBLE_FAST   ";
            }
            resultado_acao = 0;
            agente = 10;
            // ------------------------------------- Q- learning
            break;
         case 11:
            // ------------------------------------- Q- learning
            acao = definir_acao(verificar_celula(x, y));
            if (acao == 1)
            { // chutar ao gol
               soc = kickTo(posGoal, SS->getBallSpeedMax());
               nome_acao = "       CHUTAR     ";
            }
            else if (acao == 2)
            {
               soc = clearBall(CLEAR_BALL_OFFENSIVE, SIDE_ILLEGAL, NULL);
               nome_acao = "     CLEAR_BALL   ";
            }
            else if (acao == 3)
            {
               soc = directPass(posAgent_passe10, PASS_NORMAL);
               nome_acao = "    PASS_NORMAL   ";
            }
            else if (acao == 4)
            {
               soc = directPass(posAgent_passe10, PASS_FAST);
               nome_acao = "     PASS_FAST    ";
            }
            else if (acao == 5)
            {
               soc = dribble(0, DRIBBLE_WITHBALL);
               nome_acao = " DRIBBLE_WITHBALL ";
            }
            else
            {
               soc = dribble(0, DRIBBLE_FAST);
               nome_acao = "   DRIBBLE_FAST   ";
            }
            resultado_acao = 0;
            agente = 11;
            // ------------------------------------- Q- learning
            break;
         }

         ACT->putCommandInQueue(soc);
         ACT->putCommandInQueue(turnNeckToObject(OBJECT_BALL, soc)); //retorna o conmando de girar o pescoco com angulo que fara para chutar para o gol
         Log.log(100, "kick ball");
      }
      else if (WM->getFastestInSetTo(OBJECT_SET_TEAMMATES, OBJECT_BALL, &iTmp) == WM->getAgentObjectType() && !WM->isDeadBallThem())
      {
         // if fastest to ball
         Log.log(100, "I am fastest to ball; can get there in %d cycles", iTmp);
         soc = intercept(false); // intercept the ball

         if (soc.commandType == CMD_DASH && // if stamina low
             WM->getAgentStamina().getStamina() <
                 SS->getRecoverDecThr() * SS->getStaminaMax() + 200)
         {
            soc.dPower = 30.0 * WM->getAgentStamina().getRecovery(); // dash slow
            ACT->putCommandInQueue(soc);
            ACT->putCommandInQueue(turnNeckToObject(OBJECT_BALL, soc));
         }
         else // if stamina high
         {
            ACT->putCommandInQueue(soc); // dash as intended
            ACT->putCommandInQueue(turnNeckToObject(OBJECT_BALL, soc));
         }
      }
      else if (posAgent.getDistanceTo(WM->getStrategicPosition()) >
               1.5 + fabs(posAgent.getX() - posBall.getX()) / 10.0)
      // if not near strategic pos
      {

         if (WM->getAgentStamina().getStamina() > // if stamina high
             SS->getRecoverDecThr() * SS->getStaminaMax() + 800)
         {
            VecPosition posAgent_1 = WM->getGlobalPosition(OBJECT_TEAMMATE_1);
            VecPosition posAgent_Op9 = WM->getGlobalPosition(OBJECT_OPPONENT_9);
            VecPosition posAgent_Op10 = WM->getGlobalPosition(OBJECT_OPPONENT_10);
            VecPosition posAgent_Op11 = WM->getGlobalPosition(OBJECT_OPPONENT_11);
            int dx = posAgent.getX() - posAgent_1.getX();
            int dy = posAgent.getY() - posAgent_1.getY();
            int dist = (int)sqrt(dx * dx + dy * dy);

            ///////////////////////////////////////////////////////////////////////////////////
            // time adversário com a bola
            xball = posBall.getX();
            yball = posBall.getY();
            if (resultado_acao == 0 and WM->getCurrentCycle() < 6000)
            {
               resultado_acao = 2; // indica resultado negativo de ação
               q_learning(x, y, acao, agente, resultado_acao);
            }
            ///////////////////////////////////////////////////////////////////////////////////

            switch (WM->getPlayerNumber())
            {

            case 4:
               //soc = mark(OBJECT_OPPONENT_11, 2, MARK_GOAL);
               if ((posBall.getX() < 0) && (posBall.getX() > -37) && (posBall.getY() > -5) && (posBall.getY() < 5))
               {
                  soc = intercept(NULL);
               }
               else
               {
                  soc = moveToPos(WM->getStrategicPosition(), PS->getPlayerWhenToTurnAngle());
               }
               break;
            case 5:
               if ((posAgent_Op10.getX() < -15) && (posAgent.getY() < -5) && (dist > 3))
               {
                  soc = mark(OBJECT_OPPONENT_10, 1, MARK_GOAL);
               }
               else
               {
                  soc = moveToPos(WM->getStrategicPosition(), PS->getPlayerWhenToTurnAngle());
               }
               break;
            case 3:
               if ((posAgent_Op9.getX() < -15) && (posAgent.getY() > -10) && (posBall.getY() < 10) && (dist > 3))
               {
                  soc = mark(OBJECT_OPPONENT_9, 1, MARK_GOAL);
               }
               else
               {
                  soc = moveToPos(WM->getStrategicPosition(), PS->getPlayerWhenToTurnAngle());
               }
               break;
            case 2:
               if ((posAgent_Op11.getX() < -15) && (posAgent.getY() > 5) && (dist > 3))
               {
                  soc = mark(OBJECT_OPPONENT_11, 1, MARK_GOAL);
               }
               else
               {
                  soc = moveToPos(WM->getStrategicPosition(), PS->getPlayerWhenToTurnAngle());
               }
               break;
            default:
               soc = moveToPos(WM->getStrategicPosition(), PS->getPlayerWhenToTurnAngle());
               break;
            }
            ACT->putCommandInQueue(soc); // move to strategic pos
            ACT->putCommandInQueue(turnNeckToObject(OBJECT_BALL, soc));
         }
         else // else watch ball
         {
            ACT->putCommandInQueue(soc = turnBodyToObject(OBJECT_BALL));
            ACT->putCommandInQueue(turnNeckToObject(OBJECT_BALL, soc));
         }
      }
      else if (fabs(WM->getRelativeAngle(OBJECT_BALL)) > 1.0) // watch ball
      {
         ACT->putCommandInQueue(soc = turnBodyToObject(OBJECT_BALL));
         ACT->putCommandInQueue(turnNeckToObject(OBJECT_BALL, soc));
      }
      else // nothing to do
         ACT->putCommandInQueue(SoccerCommand(CMD_TURNNECK, 0.0));
   }
   return soc;
}

/*!This method is a simple goalie based on the goalie of the simple Team of
   FC Portugal. It defines a rectangle in its penalty area and moves to the
   position on this rectangle where the ball intersects if you make a line
   between the ball position and the center of the goal. If the ball can
   be intercepted in the own penalty area the ball is intercepted and catched.
*/
SoccerCommand Player::deMeer5_goalie()
{
   int i;

   SoccerCommand soc;
   VecPosition posAgent = WM->getAgentGlobalPosition();
   AngDeg angBody = WM->getAgentGlobalBodyAngle();

   // define the top and bottom position of a rectangle in which keeper moves
   static const VecPosition posLeftTop(-PITCH_LENGTH / 2.0 +
                                           0.7 * PENALTY_AREA_LENGTH,
                                       -PENALTY_AREA_WIDTH / 4.0);
   static const VecPosition posRightTop(-PITCH_LENGTH / 2.0 +
                                            0.7 * PENALTY_AREA_LENGTH,
                                        +PENALTY_AREA_WIDTH / 4.0);

   // define the borders of this rectangle using the two points.
   static Line lineFront = Line::makeLineFromTwoPoints(posLeftTop, posRightTop);
   static Line lineLeft = Line::makeLineFromTwoPoints(
       VecPosition(-50.0, posLeftTop.getY()), posLeftTop);
   static Line lineRight = Line::makeLineFromTwoPoints(
       VecPosition(-50.0, posRightTop.getY()), posRightTop);

   if (WM->isBeforeKickOff())
   {
      if (formations->getFormation() != FT_INITIAL || // not in kickoff formation
          posAgent.getDistanceTo(WM->getStrategicPosition()) > 2.0)
      {
         formations->setFormation(FT_INITIAL); // go to kick_off formation
         ACT->putCommandInQueue(soc = teleportToPos(WM->getStrategicPosition()));
      }
      else // else turn to center
      {
         ACT->putCommandInQueue(soc = turnBodyToPoint(VecPosition(0, 0), 0));
         ACT->putCommandInQueue(alignNeckWithBody());
      }
      return soc;
   }

   if (WM->getConfidence(OBJECT_BALL) < PS->getBallConfThr())
   {                                        // confidence ball too  low
      ACT->putCommandInQueue(searchBall()); // search ball
      ACT->putCommandInQueue(alignNeckWithBody());
   }
   else if (WM->getPlayMode() == PM_PLAY_ON || WM->isFreeKickThem() ||
            WM->isCornerKickThem())
   {
      if (WM->isBallCatchable())
      {
         ACT->putCommandInQueue(soc = catchBall());
         ACT->putCommandInQueue(turnNeckToObject(OBJECT_BALL, soc));
      }
      else if (WM->isBallKickable())
      {
         //soc = kickTo( VecPosition(0,posAgent.getY()*2.0), 2.0 );
         soc = clearBall(CLEAR_BALL_DEFENSIVE, SIDE_ILLEGAL, NULL);
         ACT->putCommandInQueue(soc);
         ACT->putCommandInQueue(turnNeckToObject(OBJECT_BALL, soc));
      }
      else if (WM->isInOwnPenaltyArea(getInterceptionPointBall(&i, true)) &&
               WM->getFastestInSetTo(OBJECT_SET_PLAYERS, OBJECT_BALL, &i) ==
                   WM->getAgentObjectType())
      {
         ACT->putCommandInQueue(soc = intercept(true));
         ACT->putCommandInQueue(turnNeckToObject(OBJECT_BALL, soc));
      }
      else
      {
         // make line between own goal and the ball
         VecPosition posMyGoal = (WM->getSide() == SIDE_LEFT)
                                     ? SoccerTypes::getGlobalPositionFlag(OBJECT_GOAL_L, SIDE_LEFT)
                                     : SoccerTypes::getGlobalPositionFlag(OBJECT_GOAL_R, SIDE_RIGHT);
         Line lineBall = Line::makeLineFromTwoPoints(WM->getBallPos(), posMyGoal);

         // determine where your front line intersects with the line from ball
         VecPosition posIntersect = lineFront.getIntersection(lineBall);

         // outside rectangle, use line at side to get intersection
         if (posIntersect.isRightOf(posRightTop))
            posIntersect = lineRight.getIntersection(lineBall);
         else if (posIntersect.isLeftOf(posLeftTop))
            posIntersect = lineLeft.getIntersection(lineBall);

         if (posIntersect.getX() < -49.0)
            posIntersect.setX(-49.0);

         // and move to this position
         if (posIntersect.getDistanceTo(WM->getAgentGlobalPosition()) > 0.5)
         {
            soc = moveToPos(posIntersect, PS->getPlayerWhenToTurnAngle());
            ACT->putCommandInQueue(soc);
            ACT->putCommandInQueue(turnNeckToObject(OBJECT_BALL, soc));
         }
         else
         {
            ACT->putCommandInQueue(soc = turnBodyToObject(OBJECT_BALL));
            ACT->putCommandInQueue(turnNeckToObject(OBJECT_BALL, soc));
         }
      }
   }
   else if (WM->isFreeKickUs() == true || WM->isGoalKickUs() == true)
   {
      if (WM->isBallKickable())
      {
         if (WM->getTimeSinceLastCatch() == 25 && WM->isFreeKickUs())
         {
            // move to position with lesser opponents.
            if (WM->getNrInSetInCircle(OBJECT_SET_OPPONENTS,
                                       Circle(posRightTop, 15.0)) <
                WM->getNrInSetInCircle(OBJECT_SET_OPPONENTS,
                                       Circle(posLeftTop, 15.0)))
               soc.makeCommand(CMD_MOVE, posRightTop.getX(), posRightTop.getY(), 0.0);
            else
               soc.makeCommand(CMD_MOVE, posLeftTop.getX(), posLeftTop.getY(), 0.0);
            ACT->putCommandInQueue(soc);
         }
         else if (WM->getTimeSinceLastCatch() > 28)
         {
            //soc = kickTo( VecPosition(0,posAgent.getY()*2.0), 2.0 );
            soc = clearBall(CLEAR_BALL_DEFENSIVE, SIDE_ILLEGAL, NULL);
            ACT->putCommandInQueue(soc);
         }
         else if (WM->getTimeSinceLastCatch() < 25)
         {
            VecPosition posSide(0.0, posAgent.getY());
            if (fabs((posSide - posAgent).getDirection() - angBody) > 10)
            {
               soc = turnBodyToPoint(posSide);
               ACT->putCommandInQueue(soc);
            }
            ACT->putCommandInQueue(turnNeckToObject(OBJECT_BALL, soc));
         }
      }
      else if (WM->isGoalKickUs())
      {
         ACT->putCommandInQueue(soc = intercept(true));
         ACT->putCommandInQueue(turnNeckToObject(OBJECT_BALL, soc));
      }
      else
         ACT->putCommandInQueue(turnNeckToObject(OBJECT_BALL, soc));
   }
   else
   {
      ACT->putCommandInQueue(soc = turnBodyToObject(OBJECT_BALL));
      ACT->putCommandInQueue(turnNeckToObject(OBJECT_BALL, soc));
   }
   return soc;
}
