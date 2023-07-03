int buttonState = 0;
int count = 0;

void setup() {
  Serial.begin(9600);
  pinMode(2,INPUT);
  pinMode(3,OUTPUT);
  pinMode(4,OUTPUT);
  pinMode(5,OUTPUT);
  pinMode(6,OUTPUT);
  pinMode(7,OUTPUT); 
}

void loop() {
  digitalWrite(3, LOW);
  digitalWrite(4, LOW);
  digitalWrite(5, LOW);
  digitalWrite(6, LOW);
  digitalWrite(7, LOW);

buttonState = digitalRead(2);

if(buttonState == LOW) {

} 
else { 
  count++;
  delay(200);
  Serial.print(count);
  

if((count % 2) > 0) { 
  digitalWrite(3, HIGH); 
} else {
  digitalWrite(3, LOW); 
}

if((count % 4) > 1) { 
  digitalWrite(4, HIGH); 
} else { 
  digitalWrite(4, LOW);
}

if((count % 8) > 3) {
  digitalWrite(5, HIGH); 
} else { 
  digitalWrite(5, LOW); 
}

if((count % 16) > 7) {
  digitalWrite(6, HIGH); 
} else {
  digitalWrite(6, LOW);
}

if((count % 32) > 15) {
  digitalWrite(7, HIGH); 
} else { 
  digitalWrite(7, LOW); 
}
  delay(200);
} 
}



***********************************************************************************Scheme***********************************************************
  
