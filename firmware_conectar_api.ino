#include <WiFi.h>
#include <HTTPClient.h>
#include <ArduinoJson.h>

// mude para as config de wifi
const char* ssid = "";
const char* password = "";

// API local
const char* endpoint = ""; // o ip local pra testar

String tipos[] = {"entrada", "saida"};

void setup() {
  Serial.begin(9600); // verifique isso antes de iniciar

  WiFi.begin(ssid, password);
  Serial.print("Conectando ao Wi-Fi");
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }

  Serial.println("\nWi-Fi conectado!");
  randomSeed(analogRead(0));
}

void loop() {
  if (WiFi.status() == WL_CONNECTED) {

    // simula dados
    int matricula = random(1000, 9999);
    String tipo = tipos[random(0, 2)];
    String hora = "2025-07-06T08:" + String(random(10, 59)) + ":" + String(random(10, 59));

    // json
    StaticJsonDocument<128> doc;
    doc["matricula"] = String(matricula);
    doc["tipo"] = tipo;
    doc["timestamp"] = hora;

    String mensagem;
    serializeJson(doc, mensagem);

    // envia pra api
    HTTPClient http;
    http.begin(endpoint);
    http.addHeader("Content-Type", "application/json");

    int status = http.POST(mensagem);
    Serial.println("Enviado: " + mensagem);
    Serial.println("Status HTTP: " + String(status));

    http.end();
  } else {
    Serial.println("Wi-Fi desconectado. Tentando reconectar...");
    WiFi.begin(ssid, password);
  }

  delay(10000); // aguarda 10 segundos
}
