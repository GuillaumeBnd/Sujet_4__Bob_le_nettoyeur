
#include <TFT_eSPI.h> // Graphics and font library for ST7735 driver chip
#include <SPI.h>

TFT_eSPI tft = TFT_eSPI();  // Invoke library, pins defined in User_Setup.h

#define LED_PIN 13

// Global variables

const int CapteurPin = 2; // broche du capteur infrarouge
int capteur_state; // etat de la sortie du capteur

void setup()
{
  pinMode(CapteurPin, INPUT); //la broche du capteur est mise en entree

  Serial.begin(9600);
  Serial.println("Bonjour");
  
  tft.init();
  tft.setRotation(1);
  tft.setTextSize(3);
  tft.fillScreen(TFT_BLACK);
  tft.setTextColor(TFT_BLUE, TFT_BLACK);

  tft.drawString("Bonjour, je suis\r\nBob Le Nettoyeur !", 0, 0, 2);

  delay(3000);
  tft.fillScreen(TFT_BLACK);
}

void loop()
{
    
    // Serial.println("C'est la carte Arduino qui parle");

    capteur_state = digitalRead(CapteurPin);//lecture du capteur

    tft.fillScreen(TFT_BLACK);

    if (capteur_state == LOW) //si quelquechose est detecte
    {
       Serial.println("Table");
       tft.setTextColor(TFT_GREEN, TFT_BLACK);
       tft.drawString("Table", 0, 0, 2);
    }
    else
    {
      Serial.println("Vide");
      tft.setTextColor(TFT_RED, TFT_BLACK);
      tft.drawString("VIDE !", 0, 0, 2);
    }

    /*
    while(Serial.available()) {

        if (capteur_state == LOW) //si quelquechose est detecte
        {
           Serial.println("La table est détéctée.");
        }
        else //sinon
        {
          Serial.println("Attention vide.");
        }
        
    }*/

//    delay(100);
}
