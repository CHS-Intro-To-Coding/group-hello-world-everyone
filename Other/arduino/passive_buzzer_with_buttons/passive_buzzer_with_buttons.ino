//www.elegoo.com
//2016.12.08

#include "pitches.h"

// notes in the melody:
int melody[] = {
  NOTE_C5, NOTE_D5, NOTE_E5, NOTE_F5, NOTE_G5, NOTE_A5, NOTE_B5, NOTE_C6
};
int duration = 500;  // 500 miliseconds
int buttonApin = 9;
int buttonBpin = 10;

void setup() {
  pinMode(buttonApin, INPUT_PULLUP);
  pinMode(buttonBpin, INPUT_PULLUP);
}

void loop() {
  if (digitalRead(buttonApin) == LOW)
    {for (int thisNote = 0; thisNote < 8; thisNote++) {
    // pin8 output the voice, every scale is 0.5 second
    tone(8, melody[thisNote], duration);

    // Output the voice after several minutes
    delay(1000);
  }}

  // restart after two seconds
  //delay(2000);
}
