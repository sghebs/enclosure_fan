#include <Arduino.h>
#include "SDHT.h"

SDHT dht;
void layout();

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
}

void loop() {
  // put your main code here, to run repeatedly:
  if (dht.read(DHT11, 8)) layout();
  delay(2000);
}

void layout() {
  Serial.println(String(double(dht.celsius) / 10, 1));
}