

#include <BLEDevice.h>
#include <BLEUtils.h>
#include <BLEServer.h>
#include <TFT_eSPI.h> // Graphics and font library for ST7735 driver chip
#include <SPI.h>


TFT_eSPI tft = TFT_eSPI();  // Invoke library, pins defined in User_Setup.h

#define LED_PIN 13
#define SERVICE_UUID        "4fafc201-1fb5-459e-8fcc-c5c9c331914b"
#define CHARACTERISTIC_UUIDreceive "beb5483e-36e1-4688-b7f5-ea07361b26a8"

// Global variables
const int CapteurPin = 2; // broche du capteur infrarouge
int capteur_state; // etat de la sortie du capteur

String valor;
//bool mode = true; //mode = true veut dire en mode AUTO, false = mode controle
bool depassementFlag = false; //flag mis a true quand on a eu un dépassement dans le vide


class ReceiveBLECallback: public BLECharacteristicCallbacks {
    void onWrite(BLECharacteristic *pCharacteristic) {
      //Serial.println("On write");
      std::string value = pCharacteristic->getValue();
     
      if (value.length() > 0) {
        valor = "";
        for (int i = 0; i < value.length(); i++){
          // Serial.print(value[i]); // Presenta value.
          valor = valor + value[i];
        }

        //Serial.println("*********");
        Serial.print("BLE : valeur reçue = ");
        Serial.println(valor); // Presenta valor.

        //SEND VALEUR TO RASPBERRY
        Serial.write(valor);
      }    
      
 

        
    }
};

void setup() {

  //BLE
  Serial.begin(115200);

  BLEDevice::init("BOB_LE_NETTOYEUR");
  BLEServer *pServer = BLEDevice::createServer();
  BLEService *pService = pServer->createService(SERVICE_UUID);
  
  BLECharacteristic *pCharacteristic = pService->createCharacteristic(
                                         CHARACTERISTIC_UUIDreceive,
                                         BLECharacteristic::PROPERTY_READ |
                                         BLECharacteristic::PROPERTY_WRITE
                                       );

  pCharacteristic->setCallbacks(new ReceiveBLECallback());
  pCharacteristic->setValue("Hello World");
  pService->start();

  BLEAdvertising *pAdvertising = pServer->getAdvertising();
  pAdvertising->start();

  //CAPTEUR
  pinMode(CapteurPin, INPUT); //la broche du capteur est mise en entree

  Serial.begin(115200);
  Serial.println("CAPTEUR : INITIALISATION ...");
  
  tft.init();
  tft.setRotation(1);
  tft.setTextSize(3);
  tft.fillScreen(TFT_BLACK);
  tft.setTextColor(TFT_BLUE, TFT_BLACK);

  tft.drawString("Bonjour, je suis\r\nBob Le Nettoyeur !", 0, 0, 2);

  delay(3000);
  tft.fillScreen(TFT_BLACK);
  
}

void loop() {
  // put your main code here, to run repeatedly:
   delay(1000);
   //Serial.println("valeur dans la loop = ");
   //Serial.println(valor); // Presenta valor.

   //CAPTEUR
   capteur_state = digitalRead(CapteurPin);//lecture du capteur

    tft.fillScreen(TFT_BLACK);
    
    if (capteur_state == LOW) //si quelquechose est detecte
    {
       Serial.println("CAPTEUR : Table");
       //tft.setTextColor(TFT_GREEN, TFT_BLACK);
       //tft.drawString("Table", 0, 0, 2);

       //Ne pas envoyer à raspi sauf si flag = 1. Si flag = 1, on envoie table a raspi et on remet flag à 0
       if(depassementFlag == true){
        Serial.write("CAPTEUR/table");
        depassementFlag = false;
       }
    }
    else //rien n'est detecté dans les 5 cm
    {
      Serial.println("CAPTEUR : Vide");
      //tft.setTextColor(TFT_RED, TFT_BLACK);
      //tft.drawString("VIDE !", 0, 0, 2);
      
      //SEND TO RASPY WHILE "vide". Mettre un flag à true.
      Serial.write("CAPTEUR/vide");
      depassementFlag = true;
      
    }
}
