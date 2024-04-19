#include <Servo.h>

int leftMotor1 = 16; // Left motor 1
int leftMotor2 = 17; // Left motor 2
int rightMotor1 = 18; // Right motor 3
int rightMotor2 = 19; // Right motor 4

float distance1, distance2, distance3, distance4;

int E1 = 11; // Speed control pin 1
int E2 = 12; // Speed control pin 2

const int outputPin1 = 5;   // Define center ultrasonic signal receive interface (Trig)
const int inputPin1 = 6;  // Define center ultrasonic signal transmit interface (Echo)
const int outputPin2 = 9;   // Define left ultrasonic signal receive interface (Trig)
const int inputPin2 = 2;  // Define left ultrasonic signal transmit interface (Echo)
const int outputPin3 = 3;   // Define right ultrasonic signal receive interface (Trig)
const int inputPin3 = 4;  // Define right ultrasonic signal transmit interface (Echo)
const int outputPin4 = 45;  // Define bottom ultrasonic signal receive interface (Trig)
const int inputPin4 = 46;  // Define bottom ultrasonic signal receive interface (Echo)

float distance11 = 0;
float distance22 = 0;
float distance33 = 0;
float distance44 = 0;

int i;

// Parameters for detecting treasures

void setup() {
  // Setup code runs once
  Serial.begin(9600); // Serial initialization
  pinMode(leftMotor1, OUTPUT); // Speed measurement pin initialization
  pinMode(leftMotor2, OUTPUT);
  pinMode(rightMotor1, OUTPUT);
  pinMode(rightMotor2, OUTPUT);
  pinMode(E1, OUTPUT);
  pinMode(E2, OUTPUT);

  // Ultrasonic control pin initialization
  pinMode(inputPin1, INPUT);
  pinMode(outputPin1, OUTPUT);
  pinMode(inputPin2, INPUT);
  pinMode(outputPin2, OUTPUT);
  pinMode(inputPin3, INPUT);
  pinMode(outputPin3, OUTPUT);
  pinMode(inputPin4, INPUT);
  pinMode(outputPin4, OUTPUT);

  forward(); // Start by moving forward
}

void loop() {
  // Main code runs repeatedly
  float distance1 = getDistance1();
  float distance2 = getDistance2();
  float distance3 = getDistance3();
  float distance4 = getDistance4();

  if (distance1 <= 14) { // If there's an obstacle in front
    if ((distance4 - distance1) >= 7) {
      stop();
      delay(2000);
      backward();
      delay(50);
      turnright();
      delay(700);
    } else if (distance2 <= distance3) { // If right is more open than left
      if (distance3 > 10) { // If right is spacious, it's a junction
        turnright(); // Turn right
        delay(500);
      } else { // If right is not spacious, it's a wall
        backward();
        delay(75);
        stop();
        delay(50);
        turnright();
        delay(500);
      }
    } else if (distance2 >= distance3) { // If left is more open than right
      if (distance3 > 10) { // If left is spacious, it's a junction
        turnleft(); // Turn left
        delay(500);
      } else { // If left is not spacious, it's a wall
        backward();
        delay(75);
        stop();
        delay(50);
        turnleft();
        delay(500);
      }
    }
  } else if (distance2 <= 3.3) { // Fine-tuning logic, turn right
    stop();
    delay(50);
    turnright();
    delay(170);
  } else if (distance3 <= 3.3) { // Fine-tuning logic, turn left
    stop();
    delay(50);
    turnleft();
    delay(170);
  } else {
    forward();
    delay(50);
  }
  if ((int)distance11 == (int)distance1 && (int)distance22 == (int)distance2 && (int)distance33 == (int)distance3) {
    backward();
    delay(550);
    stop();
    delay(100);
    turnright();
    forward();
    delay(100);
  }
}

void forward() {
  Serial.println("forward");
  digitalWrite(leftMotor1, HIGH);
  digitalWrite(leftMotor2, LOW);
  digitalWrite(rightMotor1, HIGH);
  digitalWrite(rightMotor2, LOW);
  analogWrite(E1, 60);
  analogWrite(E2, 60);
}

void backward() {
  Serial.println("backward");
  digitalWrite(leftMotor1, LOW);
  digitalWrite(leftMotor2, HIGH);
  digitalWrite(rightMotor1, LOW);
  digitalWrite(rightMotor2, HIGH);
  analogWrite(E1, 60);
  analogWrite(E2, 60);
}

void stop() {
  Serial.println("stop");
  digitalWrite(leftMotor1, LOW);
  digitalWrite(leftMotor2, LOW);
  digitalWrite(rightMotor1, LOW);
  digitalWrite(rightMotor2, LOW);
  analogWrite(E1, 50);
  analogWrite(E2, 50);
}

void turnleft() {
  Serial.println("turn left");
  digitalWrite(leftMotor1, HIGH);
  digitalWrite(leftMotor2, LOW);
  digitalWrite(rightMotor1, LOW);
  digitalWrite(rightMotor2, HIGH);
  analogWrite(E1, 100);
  analogWrite(E2, 100);
}

void turnright() {
  Serial.println("turn right");
  digitalWrite(leftMotor1, LOW);
  digitalWrite(leftMotor2, HIGH);
  digitalWrite(rightMotor1, HIGH);
  digitalWrite(rightMotor2, LOW);
  analogWrite(E1, 100);
  analogWrite(E2, 100);
}

// Get the distance from the low sensor
float getDistance1() {
  digitalWrite(outputPin1, LOW);
  delayMicroseconds(2);
  digitalWrite(outputPin1, HIGH);
  delayMicroseconds(10);
  digitalWrite(outputPin1, LOW);
  long duration = pulseIn(inputPin1, HIGH);
  distance11 = distance1;
  distance1 = duration * 0.034 / 2;
  Serial.println(distance1);
  return distance1;
}

// Get the distance from the left sensor
float getDistance2() {
  digitalWrite(outputPin2, LOW);
  delayMicroseconds(2);
  digitalWrite(outputPin2, HIGH);
  delayMicroseconds(10);
  digitalWrite(outputPin2, LOW);
  long duration = pulseIn(inputPin2, HIGH);
  distance22 = distance2;
  distance2 = duration * 0.034 / 2;
  Serial.println(distance2);
  return distance2;
}

// Get the distance from the right sensor
float getDistance3()
{
  digitalWrite(outputPin3, LOW); 
  delayMicroseconds(2);
  digitalWrite(outputPin3, HIGH);
  delayMicroseconds(10);
  digitalWrite(outputPin3, LOW); 
  long duration = pulseIn(inputPin3, HIGH); 
  distance33 = distance3;
  distance3= duration*0.034/2; 
  Serial.println(distance3);
  return distance3;
}

// Get the distance from the high sensor
float getDistance4()
{
  digitalWrite(outputPin4, LOW); 
  delayMicroseconds(2);
  digitalWrite(outputPin4, HIGH); 
  delayMicroseconds(10);
  digitalWrite(outputPin4, LOW); 
  long duration = pulseIn(inputPin4, HIGH); 
  distance44 = distance4;
  distance4= duration*0.034/2; 
  Serial.println(distance4);
  return distance4;
}





