#include <Arduino.h>
#include "SDHT.h"

SDHT dht;

void layout();
// valori:
int serial = 9600;
int pin = 8;

void setup() {

  Serial.begin(serial);

}

void loop() {

  if (dht.read(DHT11, pin)) layout();
  delay(2000);

}

void layout() {
  Serial.println(String(double(dht.celsius) / 10, 0));
}