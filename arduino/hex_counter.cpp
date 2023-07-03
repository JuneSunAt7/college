int buttonState = 0;
int count = 0;

void setup() {
  Serial.begin(9600);
  pinMode(2,INPUT);
  
}

void loop() {

buttonState = digitalRead(2);

if(buttonState == LOW) {

} 
else { 
  count++;
  delay(200);
  stringOne =  String(45, HEX);
  Serial.print(stringOne);
  
}



***********************************************************************************Scheme***********************************************************
  
