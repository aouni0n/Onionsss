#include <SPI.h>
#include <SoftwareSerial.h>
#include <Servo.h>
#include <Wire.h>[
#include <Adafruit_GFX.h>
#include <Adafruit_SSD1306.h>


Servo door;
int gasPin = A3;
int sensorThres = 400;
long duration;
int distanceCm, distanceInch;
int pirPin = 9;             
int pirStat = 0;
#define trigPin 5
#define echoPin 6
#define OLED_RESET 4
Adafruit_SSD1306 display(OLED_RESET);



byte val = "";
void setup() {
 door.attach(2);
 pinMode(gasPin, INPUT);
 pinMode(trigPin, OUTPUT);
 pinMode(echoPin, INPUT);     
 pinMode(pirPin, INPUT);   
 display.begin(SSD1306_SWITCHCAPVCC, 0x3C); 
 display.clearDisplay();
 Serial.begin(9600); 
}



void dist() {
float duration;
float distance_cm;
float distance_in;
 
digitalWrite(trigPin, LOW);
delayMicroseconds(2);
digitalWrite(trigPin, HIGH);
delayMicroseconds(10);
digitalWrite(trigPin, LOW);
 
duration = pulseIn(echoPin, HIGH);
 
distance_cm = (duration/2) / 29.1;
distance_in = (duration/2) / 73.914;
 
display.setCursor(0,0); 
display.setTextSize(1);
display.setTextColor(WHITE);
display.println("Recent Distance");
 
display.setCursor(60,10);
display.setTextSize(1);
display.setTextColor(WHITE);
display.println(distance_cm);
display.setCursor(90,10);
display.setTextSize(1);
display.println("cm");
 
display.setCursor(60,20); 
display.setTextSize(1);
display.setTextColor(WHITE);
display.println(distance_in);
display.setCursor(90,20);
display.setTextSize(1);
display.println("in");
display.display();
 
delay(500);
display.clearDisplay();
 
Serial.println(distance_cm);
Serial.println(distance_in);
}

void loop() {
   val = Serial.read();      
   int analogSensor = analogRead(gasPin); 
   pirStat = digitalRead(pirPin);
   if(val == 'l'){
      door.write(180);
      delay(1000);
    }
   if(val == 'u'){
      door.write(0);
      delay(1000);
    }
   if(pirStat == HIGH){       
      Serial.println("motion");
      delay(10000);
   }
   if(val == 'd'){
      dist();
      delay(1000);
   }
   if(analogSensor > sensorThres){
      Serial.println("gas");
      delay(10000);
   }


 }
