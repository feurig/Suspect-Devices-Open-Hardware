/*------------------------------------------------------------------------------------
 * rough in of new clock. 
 * bikewedge proxy provides the number of steps wanted from goldsprints data.
 * this should do some pid ling around so that it will be less jerkey. 
 *
 * Copyright 2013 (c) Donald Delmar Davis, Suspect Devices, 
 *   All rights reserved.
 *
 *   Redistribution and use in source and binary forms, with or without
 *   modification, are permitted provided that the following conditions are met:
 *   * Redistributions of source code must retain the above copyright
 *       notice, this list of conditions and the following disclaimer.
 *   * Redistributions in binary form must reproduce the above copyright
 *       notice, this list of conditions and the following disclaimer in the
 *       documentation and/or other materials provided with the distribution.
 *   * Neither the name of the <organization> nor the
 *       names of its contributors may be used to endorse or promote products
 *       derived from this software without specific prior written permission.
 *
 *   THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND
 *   ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
 *   WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
 *   DISCLAIMED. IN NO EVENT SHALL <COPYRIGHT HOLDER> BE LIABLE FOR ANY
 *   DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
 *   (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
 *    LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND
 *   ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
 *   (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
 *   SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
 */

#include <Stepper.h>
#define MIN_MILLIS_PER_STEP 20
#define STEPPER_STEPS 200
//#define STEPS_PER_REVOLUTION 2132                                    
#define STEPS_PER_REVOLUTION 1067                                    
#define INBUFFERLENGTH 100

#define BLUE_BCK_BUTTON  17
#define BLUE_FWD_BUTTON  15
#define YELLOW_BCK_BUTTON  16
#define YELLOW_FWD_BUTTON  14


char inbuffer[INBUFFERLENGTH];
int bufferIndex;
int yellowGoal=0;
int blueGoal=0;
int yellowPosition=0;
int bluePosition=0;
int stepCount = 0;         
unsigned long int lastStepMillis;

Stepper blue(STEPPER_STEPS, 8,9,10,11);
Stepper yellow(STEPPER_STEPS, 2,3,4,5);            

void setup() {
  // initialize the serial port:
  Serial.begin(115200);
  pinMode(BLUE_BCK_BUTTON,INPUT_PULLUP);
  pinMode(BLUE_FWD_BUTTON,INPUT_PULLUP);
  pinMode(YELLOW_BCK_BUTTON,INPUT_PULLUP);
  pinMode(YELLOW_FWD_BUTTON,INPUT_PULLUP);
}

void loop() {
  int target;
  while (Serial.available()) {
    // get the new byte:
    char inChar = (char)Serial.read(); 
    // add it to the inputString:
    if (bufferIndex<INBUFFERLENGTH)
      inbuffer[bufferIndex++]=inChar;
    if (inChar == '\n') {
      inbuffer[bufferIndex]=0;
      if ((inbuffer[0]=='d') && bufferIndex>3) {
        target=atoi(inbuffer+3);
        if (target>STEPS_PER_REVOLUTION) target=STEPS_PER_REVOLUTION;
        if (inbuffer[1]=='1') {
          blueGoal=target;
          Serial.println(inbuffer+3);
        } else {
          yellowGoal=target;
        } 
      } else if (inbuffer[0]=='v') {
        Serial.println("RaceClock 0.1");
        Serial.flush();
      } else if (inbuffer[0]=='s') {
        if (blueGoal||yellowGoal) {
          blueGoal=yellowGoal=STEPS_PER_REVOLUTION;
        }
      }

      bufferIndex=0; //reset input

    }
  }
  
  if ((millis()-lastStepMillis)>MIN_MILLIS_PER_STEP){ 
    
    if (!digitalRead(BLUE_BCK_BUTTON)) bluePosition++;
    if (!digitalRead(BLUE_FWD_BUTTON)) bluePosition--;
    if (!digitalRead(YELLOW_BCK_BUTTON)) yellowPosition++;
    if (!digitalRead(YELLOW_FWD_BUTTON)) yellowPosition--;
    
    if ((blueGoal==STEPS_PER_REVOLUTION)&&((bluePosition==0)||(blueGoal==bluePosition))){
         blueGoal=bluePosition=0;
    }
    if ((yellowGoal==STEPS_PER_REVOLUTION)&&((yellowPosition==0)||(yellowGoal==yellowPosition))){
         yellowGoal=yellowPosition=0;
    }   
      
    if ((blueGoal>bluePosition) && (bluePosition<STEPS_PER_REVOLUTION)){
        blue.step(1);
        bluePosition++;  
    }
    if ((yellowGoal>yellowPosition) && (yellowPosition<STEPS_PER_REVOLUTION)) {
        yellow.step(1);
        yellowPosition++;
      
    }
    lastStepMillis=millis();
  }

   
}


