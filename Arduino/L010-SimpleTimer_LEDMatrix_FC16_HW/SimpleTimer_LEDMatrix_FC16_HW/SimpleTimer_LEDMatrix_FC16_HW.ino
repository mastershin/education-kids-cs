/*
Title: Simple Timer using 4 x 8x8 LED Matrix.  (Default=45 Minute Timer.) PIN 2 (to GND) will display hh:mm, otherwise pure number will be displayed

Install: Sketch --> Include Libraries --> Manage Libraries --> MD_Parola
(C)2024. MatershinAI.com MIT License
*/
#include <MD_MAX72xx.h>
#include <MD_Parola.h>
#include <SPI.h>

// Font_Data.h contains COURIER-like font, but, built-in font from MD_Parola looks OK as well.
// #include "Font_Data.h"

// counter as seconds (decrements by 1 each sec)
// 900 = 15 minutes, 1800 = 30 minutes, 2700 = 45 minutes
int counter = 2700;

// - DS1307 (clock) library (MD_DS1307) found at https://github.com/MajicDesigns/DS1307
// - DHT11 (temp/humidity sensor) library (DHT11_lib) found at http://arduino.cc/playground/Main/DHT11Lib
// - MD_MAX72XX library can be found at https://github.com/MajicDesigns/MD_MAX72XX

#define HARDWARE_TYPE MD_MAX72XX::FC16_HW
#define MAX_DEVICES 4

#define DISP_MODE_PIN 2 // if connected to GND, use hh:mm format, otherwise, simple counter number is displayed

#define CS_PIN 10 // or SS
#define DATA_PIN 11 // or MOSI, COPI (Controller Out, Peripheral In)

#define CLK_PIN 13 // or SCK

#define LED_INTENSITY 0     // (0 is min, 15 is max)

// Software SPI on arbitrary pins; initializes the matrix with 4 8x8 grids and one "zone" (zone 0);
// zones are logical units of work that are used by the parola library for animations
// software SPI
MD_Parola P = MD_Parola(HARDWARE_TYPE, DATA_PIN, CLK_PIN, CS_PIN, MAX_DEVICES);

// hardware SPI
//MD_Parola P = MD_Parola(HARDWARE_TYPE, CS_PIN, MAX_DEVICES);


void setup(void){
  P.begin();
  P.setIntensity(LED_INTENSITY); // Set intensity level (0 is min, 15 is max)
  P.displayClear();

  pinMode(DISP_MODE_PIN, INPUT_PULLUP);
  pinMode(13, OUTPUT);  // built-in LED

  // If we're using Font_Data.h
  // P.setFont(0, numeric7Seg);
}
char formattedStr[10];

const int ledPin = 2;
void display_minute_sec(int totalSeconds) {

  // Calculate hours and minutes
  int hours = totalSeconds / 3600;
  int minutes = (totalSeconds % 3600) / 60;
  int seconds = totalSeconds % 60;

  // Format the time with leading zeros
  // sprintf(formattedStr, " %02d: %02d", minutes, seconds);  // numeric7Seg (Font_Data.h)
  sprintf(formattedStr, " %02d:%02d", minutes, seconds);  // built-in font from MD_Parola.h

  P.setTextAlignment(PA_LEFT);
  P.print(formattedStr);

  // turn on LED on Prototype 
  for(int i = 0; i <= 9; i++) {
  pinMode(ledPin, OUTPUT);
  digitalWrite(ledPin, HIGH);
  pinMode(i, OUTPUT);
  digitalWrite(i, HIGH);  
  }
}

const long interval = 1000;

unsigned long previousMillis = 0;

// Displays actual number
void display_counter(int counter) {
  snprintf(formattedStr, sizeof(formattedStr), "%6d", counter);
  P.print(formattedStr);
}

void loop(void){
  unsigned long currentMillis = millis();
  //P.displayText("1234", PA_CENTER, 0, 0, PA_PRINT, PA_NO_EFFECT);

  if (digitalRead(DISP_MODE_PIN) == HIGH) { // disconnected from GND, display numeric counter
    digitalWrite(13, LOW);
  // display as 4 digit number
   display_counter(counter);
  }
  else {
    digitalWrite(13, HIGH);
    // assuming counter is total seconds, display minutes : seconds
    display_minute_sec(counter);
  }
 
	// delay(1000);
  if (currentMillis - previousMillis >= interval) {
    previousMillis = currentMillis;
    if (counter > 0)
      counter --;
  }



}