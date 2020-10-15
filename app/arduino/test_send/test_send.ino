/*
    Based on Neil Kolban example for IDF: 
https://github.com/nkolban/esp32-snippets/blob/master/cpp_utils/tests/BLE%20Tests/SampleWrite.cpp
    Ported to Arduino ESP32 by Evandro Copercini
*/
// Modificado por Juan Antonio Villalpando.
// http://kio4.com/arduino/160i_Wemos_ESP32_BLE.htm

#include <BLEDevice.h>
#include <BLEUtils.h>
#include <BLEServer.h>

#include <TFT_eSPI.h> // Graphics and font library for ST7735 driver chip
#include <SPI.h>

String valor;
bool mode = true; //mode = true veut dire en mode AUTO, false = mode controle

#define SERVICE_UUID        "4fafc201-1fb5-459e-8fcc-c5c9c331914b"
#define CHARACTERISTIC_UUIDreceive "beb5483e-36e1-4688-b7f5-ea07361b26a8"

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

        Serial.println("*********");
        Serial.print("valeur reçue = ");
        Serial.println(valor); // Presenta valor.
      }    
      //SEND VALEUR TO RASPBERRY
 

        
    }
};

void setup() {
  Serial.begin(115200);

  BLEDevice::init("MyESP32pop");
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

  
}

void loop() {
  // put your main code here, to run repeatedly:
   delay(2000);
   //Serial.println("valeur dans la loop = ");
   //Serial.println(valor); // Presenta valor.
}
