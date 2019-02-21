
int led = 13;

void setup() {                
  pinMode(led, OUTPUT);   
  Serial.begin(115200);  
}

void loop() {
  if(Serial.available()>0) 
  {
    char ser = Serial.read();
  if(ser=='a') digitalWrite(led, HIGH);               
  else if(ser=='b') digitalWrite(led, LOW);
  }
}           
