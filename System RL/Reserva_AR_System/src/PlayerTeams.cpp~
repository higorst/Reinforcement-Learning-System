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
SoccerCommand Player::deMeer5(  )
{

  SoccerCommand soc(CMD_ILLEGAL);
  VecPosition   posAgent = WM->getAgentGlobalPosition();
  VecPosition   posBall  = WM->getBallPos();
  int           iTmp;
  
  if( WM->isBeforeKickOff( ) )
  {
    if( WM->isKickOffUs( ) && WM->getPlayerNumber() == 9 ) // 9 takes kick
    {
      if( WM->isBallKickable() )
      { 
        //Toca a bola para o 8 no inicio do jogo
        VecPosition posAgent_passe8 = WM->getGlobalPosition(OBJECT_TEAMMATE_8);
        soc = directPass(posAgent_passe8, PASS_NORMAL);
        Log.log( 100, "take kick off" );        
      }
      else
      {
        soc = intercept( false );
        Log.log( 100, "move to ball to take kick-off" );
      }  
      ACT->putCommandInQueue( soc );
      ACT->putCommandInQueue( turnNeckToObject( OBJECT_BALL, soc ) );
      return soc;
    }  
    if( formations->getFormation() != FT_INITIAL || // not in kickoff formation
        posAgent.getDistanceTo( WM->getStrategicPosition() ) > 2.0 )  
    {
      formations->setFormation( FT_343_ATTACKING);       // go to kick_off formation
      ACT->putCommandInQueue( soc=teleportToPos( WM->getStrategicPosition() ));
    }
    else                                            // else turn to center
    {
      ACT->putCommandInQueue( soc=turnBodyToPoint( VecPosition( 0, 0 ), 0 ) );
      ACT->putCommandInQueue( alignNeckWithBody( ) );
    }
  }
  else
  {
    formations->setFormation( FT_334_OFFENSIVE);
    soc.commandType = CMD_ILLEGAL;
    if( WM->getConfidence( OBJECT_BALL ) < PS->getBallConfThr() )
    {
      ACT->putCommandInQueue( soc = searchBall() );   // if ball pos unknown
      ACT->putCommandInQueue( alignNeckWithBody( ) ); // search for it
    }
    else if( WM->isBallKickable())                    // if kickable
    {
      //Declaracao de objetos de posiocionamento de jogadores 
      VecPosition posGoal( PITCH_LENGTH/2.0,(-1 + 2*(WM->getCurrentCycle()%2)) * 0.4 * SS->getGoalWidth() );
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
      int distl = (int) sqrt(dxl*dxl + dyl*dyl); 
      
      //Escolhe qual o agente  
      switch(WM->getPlayerNumber()){
         case 2: 
            //CHUTA A BOLA PARA O CAMPO OFENSIVO    
            soc = clearBall(CLEAR_BALL_OFFENSIVE_SIDE, SIDE_ILLEGAL, NULL);        
            break;
         case 3: 
            //CHUTA A BOLA PARA O CAMPO OFENSIVO
            soc = clearBall(CLEAR_BALL_OFFENSIVE_SIDE, SIDE_ILLEGAL, NULL); 
            break;
         case 4:
            //CHUTA A BOLA PARA O CAMPO OFENSIVO 
            if((distl>2)&&(posAgent.getY()<32)){//verifica a margem segura
               if(posAgent.getX()<10){//posicao em x menor q 10
                   soc = dribble(1, DRIBBLE_SLOW);//liga o drible
               }else{ if(posAgent.getX()<20){
                         soc = directPass(posAgent_passe8, PASS_FAST);//passe p 10
                      }  
}
}
            break;
         case 5: 
	    //CHUTA A BOLA PARA O CAMPO OFENSIVO
            soc = clearBall(CLEAR_BALL_OFFENSIVE_SIDE, SIDE_ILLEGAL, NULL);  
            break;
         case 6: 
                     //CHUTA A BOLA PARA O CAMPO OFENSIVO 
             if(posAgent.getX()<20){
                         soc = directPass(posAgent_passe11, PASS_FAST);//passe p 10
                      }  
            
            break;
         case 7: 
                       //CHUTA A BOLA PARA O CAMPO OFENSIVO 
             if(posAgent.getX()<20){
                         soc = directPass(posAgent_passe10, PASS_FAST);//passe p 10
                      }   
            break;
         case 8:
                     //CHUTA A BOLA PARA O CAMPO OFENSIVO 
            if((distl>2)&&(posAgent.getY()<32)){//verifica a margem segura
               if(posAgent.getX()<10){//posicao em x menor q 10
                   soc = dribble(1, DRIBBLE_SLOW);//liga o drible
               }else{ if(posAgent.getX()<20){
                         soc = directPass(posAgent_passe10, PASS_FAST);//passe p 10
                      }  
}
}
            break;
         case 9: 
            if(posAgent.getX()>35){
                         
                                     soc = kickTo( posGoal, SS->getBallSpeedMax() );
           }
            break;
         case 10:
           if((distl>2)&&(posAgent.getX()<20)&&(posAgent.getY()<32)){//verifica margem 	
              if((posAgent.getX()<15)&&(posAgent.getX()<(posAgent_passe6.getX()-3))){
                 soc = directPass(posAgent_passe9, PASS_FAST);//toca para o 6
              }else{ if(posAgent.getX()<27){
                       soc = dribble(0, DRIBBLE_FAST);//liga o drible
                   }else{  	
		       soc = directPass(posAgent_passe11, PASS_FAST); //chuta
                   }
              }
           }
           break;
         case 11:
            if(posAgent.getX()>34){
                         
                                     soc = kickTo( posGoal, SS->getBallSpeedMax() );
           }
            break;
      }
	
      ACT->putCommandInQueue( soc );
      ACT->putCommandInQueue( turnNeckToObject( OBJECT_BALL, soc ) );//retorna o conmando de girar o pescoco com angulo que fara para chutar para o gol
      Log.log( 100, "kick ball" );
    }
    else if( WM->getFastestInSetTo( OBJECT_SET_TEAMMATES, OBJECT_BALL, &iTmp )
              == WM->getAgentObjectType()  && !WM->isDeadBallThem() )
    {                                                // if fastest to ball
      Log.log( 100, "I am fastest to ball; can get there in %d cycles", iTmp );
      soc = intercept( false );                      // intercept the ball

      if( soc.commandType == CMD_DASH &&             // if stamina low
          WM->getAgentStamina().getStamina() <
             SS->getRecoverDecThr()*SS->getStaminaMax()+200 )
      {
        soc.dPower = 30.0 * WM->getAgentStamina().getRecovery(); // dash slow
        ACT->putCommandInQueue( soc );
        ACT->putCommandInQueue( turnNeckToObject( OBJECT_BALL, soc ) );
      }
      else                                           // if stamina high
      {
        ACT->putCommandInQueue( soc );               // dash as intended
        ACT->putCommandInQueue( turnNeckToObject( OBJECT_BALL, soc ) );
      }
     }
     else if( posAgent.getDistanceTo(WM->getStrategicPosition()) >
                  1.5 + fabs(posAgent.getX()-posBall.getX())/10.0)
                                                  // if not near strategic pos
     {
       if( WM->getAgentStamina().getStamina() >     // if stamina high
                            SS->getRecoverDecThr()*SS->getStaminaMax()+800 )
       {
   VecPosition posAgent_1 = WM->getGlobalPosition(OBJECT_TEAMMATE_1); 
   VecPosition posAgent_Op9 = WM->getGlobalPosition(OBJECT_OPPONENT_9);
   VecPosition posAgent_Op10 = WM->getGlobalPosition(OBJECT_OPPONENT_10);
   VecPosition posAgent_Op11 = WM->getGlobalPosition(OBJECT_OPPONENT_11);
      int dx = posAgent.getX() - posAgent_1.getX();
      int dy = posAgent.getY() - posAgent_1.getY();
      int dist = (int) sqrt(dx*dx + dy*dy);                  
      switch(WM->getPlayerNumber()){

         case 4: 
	    //    
            //soc = mark(OBJECT_OPPONENT_11, 2, MARK_GOAL);
   if((posBall.getX()<0)&&(posBall.getX()>-37)&&(posBall.getY()>-5)&&(posBall.getY()<5)){    
               soc = intercept(NULL);
            }else{
               soc = moveToPos(WM->getStrategicPosition(),PS->getPlayerWhenToTurnAngle());
            }
            break;
         case 5:   
            if((posAgent_Op10.getX()<-15)&&(posAgent.getY()<-5)&&(dist>3)){
              soc = mark(OBJECT_OPPONENT_10, 1, MARK_GOAL);
            }else{
               soc = moveToPos(WM->getStrategicPosition(),PS->getPlayerWhenToTurnAngle());
            }
            break;
         case 3: 
            if((posAgent_Op9.getX()<-15)&&(posAgent.getY()>-10)&&(posBall.getY()<10)&&(dist>3)){
               soc = mark(OBJECT_OPPONENT_9, 1, MARK_GOAL);
            }else{
               soc = moveToPos(WM->getStrategicPosition(),PS->getPlayerWhenToTurnAngle());
            }
            break;
         case 2: 
            if((posAgent_Op11.getX()<-15)&&(posAgent.getY()>5)&&(dist>3)){
               soc = mark(OBJECT_OPPONENT_11, 1, MARK_GOAL);
            }else{
               soc = moveToPos(WM->getStrategicPosition(),PS->getPlayerWhenToTurnAngle());
            }
            break;
         default:
            soc = moveToPos(WM->getStrategicPosition(),PS->getPlayerWhenToTurnAngle());
            break;
       } 
       ACT->putCommandInQueue( soc );            // move to strategic pos
       ACT->putCommandInQueue( turnNeckToObject( OBJECT_BALL, soc ) );
       }
       else                                        // else watch ball
       {
         ACT->putCommandInQueue( soc = turnBodyToObject( OBJECT_BALL ) );
         ACT->putCommandInQueue( turnNeckToObject( OBJECT_BALL, soc ) );
       }
     }
     else if( fabs( WM->getRelativeAngle( OBJECT_BALL ) ) > 1.0 ) // watch ball
     {
       ACT->putCommandInQueue( soc = turnBodyToObject( OBJECT_BALL ) );
       ACT->putCommandInQueue( turnNeckToObject( OBJECT_BALL, soc ) );
     }
     else                                         // nothing to do
       ACT->putCommandInQueue( SoccerCommand(CMD_TURNNECK,0.0) );
   }
  return soc;
}

/*!This method is a simple goalie based on the goalie of the simple Team of
   FC Portugal. It defines a rectangle in its penalty area and moves to the
   position on this rectangle where the ball intersects if you make a line
   between the ball position and the center of the goal. If the ball can
   be intercepted in the own penalty area the ball is intercepted and catched.
*/
SoccerCommand Player::deMeer5_goalie(  )
{
  int i;

  SoccerCommand soc;
  VecPosition   posAgent = WM->getAgentGlobalPosition();
  AngDeg        angBody  = WM->getAgentGlobalBodyAngle();

  // define the top and bottom position of a rectangle in which keeper moves
  static const VecPosition posLeftTop( -PITCH_LENGTH/2.0 +
               0.7*PENALTY_AREA_LENGTH, -PENALTY_AREA_WIDTH/4.0 );
  static const VecPosition posRightTop( -PITCH_LENGTH/2.0 +
               0.7*PENALTY_AREA_LENGTH, +PENALTY_AREA_WIDTH/4.0 );

  // define the borders of this rectangle using the two points.
  static Line  lineFront = Line::makeLineFromTwoPoints(posLeftTop,posRightTop);
  static Line  lineLeft  = Line::makeLineFromTwoPoints(
                         VecPosition( -50.0, posLeftTop.getY()), posLeftTop );
  static Line  lineRight = Line::makeLineFromTwoPoints(
                         VecPosition( -50.0, posRightTop.getY()),posRightTop );


  if( WM->isBeforeKickOff( ) )
  {
    if( formations->getFormation() != FT_INITIAL || // not in kickoff formation
        posAgent.getDistanceTo( WM->getStrategicPosition() ) > 2.0 )  
    {
      formations->setFormation( FT_INITIAL );       // go to kick_off formation
      ACT->putCommandInQueue( soc=teleportToPos(WM->getStrategicPosition()) );
    }
    else                                            // else turn to center
    {
      ACT->putCommandInQueue( soc = turnBodyToPoint( VecPosition( 0, 0 ), 0 ));
      ACT->putCommandInQueue( alignNeckWithBody( ) );
    }
    return soc;
  }

  if( WM->getConfidence( OBJECT_BALL ) < PS->getBallConfThr() )
  {                                                // confidence ball too  low
    ACT->putCommandInQueue( searchBall() );        // search ball
    ACT->putCommandInQueue( alignNeckWithBody( ) );
  }
  else if( WM->getPlayMode() == PM_PLAY_ON || WM->isFreeKickThem() ||
           WM->isCornerKickThem() )               
  {
    if( WM->isBallCatchable() )
    {
      ACT->putCommandInQueue( soc = catchBall() );
      ACT->putCommandInQueue( turnNeckToObject( OBJECT_BALL, soc ) );
    }
     else if( WM->isBallKickable() )
    {
       //soc = kickTo( VecPosition(0,posAgent.getY()*2.0), 2.0 );
       soc = clearBall(CLEAR_BALL_DEFENSIVE, SIDE_ILLEGAL, NULL);     
       ACT->putCommandInQueue( soc );
       ACT->putCommandInQueue( turnNeckToObject( OBJECT_BALL, soc ) );
    }
    else if( WM->isInOwnPenaltyArea( getInterceptionPointBall( &i, true ) ) &&
             WM->getFastestInSetTo( OBJECT_SET_PLAYERS, OBJECT_BALL, &i ) == 
                                               WM->getAgentObjectType() )
    {
      ACT->putCommandInQueue( soc = intercept( true ) );
      ACT->putCommandInQueue( turnNeckToObject( OBJECT_BALL, soc ) );
    }
    else
    {
      // make line between own goal and the ball
      VecPosition posMyGoal = ( WM->getSide() == SIDE_LEFT )
             ? SoccerTypes::getGlobalPositionFlag(OBJECT_GOAL_L, SIDE_LEFT )
             : SoccerTypes::getGlobalPositionFlag(OBJECT_GOAL_R, SIDE_RIGHT);
      Line lineBall = Line::makeLineFromTwoPoints( WM->getBallPos(),posMyGoal);

      // determine where your front line intersects with the line from ball
      VecPosition posIntersect = lineFront.getIntersection( lineBall );

      // outside rectangle, use line at side to get intersection
      if (posIntersect.isRightOf( posRightTop ) )
        posIntersect = lineRight.getIntersection( lineBall );
      else if (posIntersect.isLeftOf( posLeftTop )  )
        posIntersect = lineLeft.getIntersection( lineBall );

      if( posIntersect.getX() < -49.0 )
        posIntersect.setX( -49.0 );
        
      // and move to this position
      if( posIntersect.getDistanceTo( WM->getAgentGlobalPosition() ) > 0.5 )
      {
        soc = moveToPos( posIntersect, PS->getPlayerWhenToTurnAngle() );
        ACT->putCommandInQueue( soc );
        ACT->putCommandInQueue( turnNeckToObject( OBJECT_BALL, soc ) );
      }
      else
      {
        ACT->putCommandInQueue( soc = turnBodyToObject( OBJECT_BALL ) );
        ACT->putCommandInQueue( turnNeckToObject( OBJECT_BALL, soc ) );
      }
    }
  }
  else if( WM->isFreeKickUs() == true || WM->isGoalKickUs() == true )
  {
    if( WM->isBallKickable() )
    {
      if( WM->getTimeSinceLastCatch() == 25 && WM->isFreeKickUs() )
      {
        // move to position with lesser opponents.
        if( WM->getNrInSetInCircle( OBJECT_SET_OPPONENTS, 
                                          Circle(posRightTop, 15.0 )) <
            WM->getNrInSetInCircle( OBJECT_SET_OPPONENTS, 
                                           Circle(posLeftTop,  15.0 )) )
          soc.makeCommand( CMD_MOVE,posRightTop.getX(),posRightTop.getY(),0.0);
        else
          soc.makeCommand( CMD_MOVE,posLeftTop.getX(), posLeftTop.getY(), 0.0);
        ACT->putCommandInQueue( soc );
      }
      else if( WM->getTimeSinceLastCatch() > 28 )
      {
        //soc = kickTo( VecPosition(0,posAgent.getY()*2.0), 2.0 );
        soc = clearBall(CLEAR_BALL_DEFENSIVE, SIDE_ILLEGAL, NULL);     
        ACT->putCommandInQueue( soc );
      }
      else if( WM->getTimeSinceLastCatch() < 25 )
      {
        VecPosition posSide( 0.0, posAgent.getY() ); 
        if( fabs( (posSide - posAgent).getDirection() - angBody) > 10 )
        {
          soc = turnBodyToPoint( posSide );
          ACT->putCommandInQueue( soc );
        }
        ACT->putCommandInQueue( turnNeckToObject( OBJECT_BALL, soc ) );
      }
    }
    else if( WM->isGoalKickUs()  )
    {
      ACT->putCommandInQueue( soc = intercept( true ) );
      ACT->putCommandInQueue( turnNeckToObject( OBJECT_BALL, soc ) );
    }
    else
      ACT->putCommandInQueue( turnNeckToObject( OBJECT_BALL, soc ) );
  }
  else
  {
     ACT->putCommandInQueue( soc = turnBodyToObject( OBJECT_BALL ) );
     ACT->putCommandInQueue( turnNeckToObject( OBJECT_BALL, soc ) );
  }
  return soc;
}
