#define c4    261.63
#define d4    293.66
#define e4    329.63
#define f4    349.23
#define g4    392.00
#define a4    440.00
#define b4    493.88
#define c5    523.25
#define d5    587.33
#define e5    659.25
#define f5    698.46
#define g5    783.99
#define a5    880.00
#define b5    987.77
#define c6    1046.50
#define ciss4   277.18
#define diss4   311.13
#define fiss4   369.99
#define giss4   415.30
#define aiss4   466.16
#define ciss5   554.37
#define diss5   622.25
#define fiss5   739.99
#define giss5   830.61
#define aiss5   932.33
float notes[] = {c4, d4, e4, f4, g4, a4, b4, c5, d5, e5, f5, g5, a5, b5, c6};
float sharpNotes[] = {ciss4, diss4, fiss4, giss4, aiss4, ciss5, diss5, fiss5, giss5, aiss5};
const int soundPin = 13;
const int buttonPin = 12;
int buttonState = 0;
const int touchPin = 11;
int touchValue = 0;

void setup() {
 pinMode(soundPin, OUTPUT);
 pinMode(buttonPin, INPUT);
 pinMode(touchPin, INPUT);
 Serial.begin(9600);
 buttonState = HIGH;
 touchValue = LOW;
}

void loop() {
  Serial.print(touchValue);
  touchValue = digitalRead(touchPin);
  buttonState = digitalRead(buttonPin);
  if (buttonState == LOW) {
    int sensorValue = analogRead(A0);
    if (touchValue == HIGH) {
      tone(soundPin, sharpNotes[(sensorValue-1) * 9/1023], 20);
    } else {
      tone(soundPin, notes[(sensorValue-1) * 13/1023], 20);
    }
  }
  delay(20);

}

