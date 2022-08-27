//Read values from GUI and vary brightness accordingly

const int ledPin = 3;  
int incomingByte;

void setup() {
  Serial.begin(9600);
  pinMode(ledPin, OUTPUT);   
}

void loop() {

  if (Serial.available() > 0){
    incomingByte = Serial.read();
    analogWrite(ledPin, incomingByte); 
    //delay(10);
    //if (incomingByte == 'H'){
      //digitalWrite(ledPin, incomingByte);
    //}
    if (incomingByte == 'L'){
      digitalWrite(ledPin, LOW);
    }
  } 
}
