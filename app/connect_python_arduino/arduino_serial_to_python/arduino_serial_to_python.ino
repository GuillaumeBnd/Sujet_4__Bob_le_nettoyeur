#define LED_PIN 13
void setup()
{
  pinMode(LED_PIN, OUTPUT);
  Serial.begin(9600);
  Serial.println("Bonjour");
}

void loop()
{
    
    Serial.println("C'est la carte Arduino qui parle");

    while(Serial.available()) {
//        int lu = Serial.read();
//        flash(lu);

        String msg = Serial.readString();
        Serial.println("From arduino :" + msg);
        
    }
    delay(1000);
}

void flash(int n)
{
  for (int i = 0; i < n; i++)
  {
    digitalWrite(LED_PIN, HIGH);
    delay(1000);
    digitalWrite(LED_PIN, LOW);
    delay(1000);
  }
}
