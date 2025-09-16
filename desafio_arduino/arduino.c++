// João Gustavo, João Pedro e Gabriel Moreira

#include <Servo.h>
#include "DHT.h"

#define DHTPIN 2
#define DHTTYPE DHT11
#define BUZZER_PIN 10
#define BUTTON_PIN 6 

DHT dht(DHTPIN, DHTTYPE);
Servo meuServo;

void setup() {
  Serial.begin(9600);
  dht.begin();
  meuServo.attach(9);  
  pinMode(BUZZER_PIN, OUTPUT);
  pinMode(BUTTON_PIN, INPUT_PULLUP);  
}

void loop() {
  float temp = dht.readTemperature();  

  bool botaoPressionado = digitalRead(BUTTON_PIN) == LOW;  

  if (isnan(temp)) {
    Serial.println("Erro na leitura do DHT11!");
  } else {
    Serial.print("Temperatura: ");
    Serial.print(temp);
    Serial.println(" °C");

    if (temp > 28) {
      digitalWrite(BUZZER_PIN, HIGH);
    } else {
      digitalWrite(BUZZER_PIN, LOW);
    }

    if (temp > 30 || botaoPressionado) {
      for (int angulo = 0; angulo <= 180; angulo++) {
        meuServo.write(angulo);
        delay(10);
      }
      for (int angulo = 180; angulo >= 0; angulo--) {
        meuServo.write(angulo);
        delay(10);
      }
    }
  }

  delay(1000);
}