/*
 RaceInABox
 
 */
#define MOTOR1DIR 2
#define MOTOR2DIR 4
#define MOTOR1PWM 3
#define MOTOR2PWM 5
#define MOTOR1CLOCKWISE   digitalWrite(MOTOR1DIR, HIGH);   
#define MOTOR1COUNTERCLOCKWISE   digitalWrite(MOTOR1DIR, LOW);   
#define MOTOR2CLOCKWISE   digitalWrite(MOTOR2DIR, HIGH);   
#define MOTOR2COUNTERCLOCKWISE   digitalWrite(MOTOR2DIR, LOW);   
#define INBUFFERLENGTH 32
char inbuffer[INBUFFERLENGTH];

void setup()  { 
  Serial.begin(115200);
  pinMode(MOTOR1DIR, OUTPUT);
  pinMode(MOTOR2DIR, OUTPUT);
  pinMode(MOTOR1PWM, OUTPUT);
  pinMode(MOTOR2PWM, OUTPUT);
  analogWrite(MOTOR1PWM, 0);         
  analogWrite(MOTOR2PWM, 0);         

  MOTOR1CLOCKWISE;
  MOTOR2CLOCKWISE;
} 
bool isClockwise = true;
uint8_t bufferIndex=0;
uint8_t bike1speed;

void loop()  { 
   while (Serial.available()) {
    // get the new byte:
    char inChar = (char)Serial.read(); 
    // add it to the inputString:
    if (bufferIndex<INBUFFERLENGTH)
      inbuffer[bufferIndex++]=inChar;
    // if the incoming character is a newline, set a flag
    // so the main loop can do something about it:
    if (inChar == '\n') {
      inbuffer[bufferIndex]=0;
      if ((inbuffer[0]=='b') && bufferIndex>3) {
          bike1speed=(uint8_t) atoi(inbuffer+3);
          if (inbuffer[1]=='1') {
            analogWrite(MOTOR1PWM,bike1speed);
          } else {
            analogWrite(MOTOR2PWM,bike1speed);
          } 
      } else if (inbuffer[0]=='v') {
        Serial.println("RaceInABox 0.1");
        Serial.flush();
      }
      
      bufferIndex=0; //reset input

  }
}
}


