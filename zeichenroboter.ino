#include <Wire.h>
#include <Adafruit_PWMServoDriver.h>

// Create the servo driver instance
Adafruit_PWMServoDriver pwm = Adafruit_PWMServoDriver();

// Define the number of servos and their default speeds
const int numServos = 3;
int servoSpeeds[numServos] = {0}; // Initialize speeds for each servo

void setup() {
  Serial.begin(9600);

  pwm.begin();
  pwm.setPWMFreq(60);  // Set the PWM frequency (usually 60 Hz)

  // Set initial speeds and directions for each servo
  for (int i = 0; i < numServos; i++) {
    setServoSpeed(i, 0); // Stop all servos initially
  }

  delay(10);
}

void loop() {
  // Rotate each servo in a different direction and at different speeds
  setServoSpeed(0, 300); // Rotate servo 1 clockwise
  setServoSpeed(1, 400); // Rotate servo 2 clockwise faster
  setServoSpeed(2, 200); // Rotate servo 3 counterclockwise

  delay(2000); // Wait for 2 seconds

  // Stop all servos
  for (int i = 0; i < numServos; i++) {
    setServoSpeed(i, 0);
  }

  delay(2000); // Wait for 2 seconds
}

// Function to set speed for a specific servo
void setServoSpeed(int servoNum, int speed) {
  // Ensure the speed is within the valid PWM range
  speed = constrain(speed, 0, 4095);

  // Set the PWM value based on the speed
  pwm.setPWM(servoNum, 0, speed);

  // Store the speed for future reference
  servoSpeeds[servoNum] = speed;
}
