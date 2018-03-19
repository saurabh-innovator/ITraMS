#include <TinyGPS++.h>
#include <SoftwareSerial.h>
int RXPin = 2;
int TXPin = 3;
float a;
int GPSBaud = 9600;
TinyGPSPlus gps;
SoftwareSerial gpsSerial(RXPin, TXPin);
int x=A0;
int y=A1;
int z=A2;
int xdata,ydata,zdata;
void setup() {
  Serial.begin(9600);
   gpsSerial.begin(GPSBaud);
}

void loop() {
  while (gpsSerial.available() > 0)
    if (gps.encode(gpsSerial.read()))
      displayInfo();
  if (millis() > 5000 && gps.charsProcessed() < 10)
  {
    Serial.println("No GPS detected");
   
  }
}
void displayInfo()
{
  Serial.print("");
  if (gps.location.isValid())
  {
   // Serial.print("Lattitude: ");
    Serial.print(gps.location.lat(), 6);
    Serial.print(",");
    Serial.println(gps.location.lng(), 6);
    Serial.println(gps.speed.kmph(),6);
    Serial.println("");
    a= gps.speed.kmph();
  }
  else
  {
    Serial.println("INVALID");
    
  }
}
  
