#include <Wire.h>
#include <Adafruit_PWMServoDriver.h>

Adafruit_PWMServoDriver pwm = Adafruit_PWMServoDriver();

void setup() {
  Serial.begin(115200);
  Serial.setTimeout(1);
  pwm.begin();
  pwm.setPWMFreq(50);  // Set the PWM frequency (usually 60 Hz)
}

void loop() {

  /*if(Serial.available()){
    int x = Serial.readString().toInt();
    int y = Serial.readString().toInt();
    //      Servo,   PWM
    pwm.setPWM(0, 0, x);
    pwm.setPWM(1, 0, y);
  }*/

  for(int i = 0; i < 10; i++) {
    pwm.setPWM(1, 0, 400+i*15);
    for(int j = 0; j < 50; j++) {
      pwm.setPWM(0, 0, 200+j*3);
      delay(100);
    }

  }
}

