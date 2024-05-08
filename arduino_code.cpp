#ARDUINO CODE:

#include <Arduino.h>
#include <WiFi.h>
String data;
const char* ssid = "OMOTECH_2.4GHz";
const char* password = "Omotech@23";
const int port = 80;  // Specify the port to listen on

// Create a WiFi server object on the specified port
WiFiServer server(port);

void setup() {
    Serial.begin(115200);
    pinMode(LED_D0, OUTPUT);
    pinMode(LED_D1, OUTPUT);
    pinMode(LED_D2, OUTPUT);
    pinMode(LED_D3, OUTPUT);
    pinMode(D0, OUTPUT);
    pinMode(D1, OUTPUT);
    pinMode(D2, OUTPUT);
    pinMode(D3, OUTPUT);
    // Connect to the WiFi network
    Serial.println("Connecting to WiFi...");
    WiFi.begin(ssid, password);
    digitalWrite(LED_D0, HIGH);
    // Wait for connection
    while (WiFi.status() != WL_CONNECTED) {
        digitalWrite(LED_D0, HIGH);
        delay(100);
        digitalWrite(LED_D0, LOW);
        delay(100);
        Serial.println("Connecting...");
    }
    Serial.println("Connected to WiFi!");
    digitalWrite(LED_D0, LOW);
    // Optional: Print the IP address
    Serial.println("IP Address: ");
    Serial.println(WiFi.localIP());

    // Start the server
    server.begin();
    Serial.println("Server started. Waiting for connections...");
}

void loop() {
    // Check if a client has connected
    WiFiClient client = server.available();
    if (client) {
        Serial.println("Client connected!");

        // Read data from the client while it's connected
        while (client.connected()) {
            if (client.available()) {
              digitalWrite(LED_D1, HIGH);
                // Read data from the client
                data = client.readStringUntil('\n');
                Serial.print("Received data: ");
                Serial.println(data);
                // Optional: Echo the received data back to the client
                client.println("Received: " + data);
            }
        }

        // When the client disconnects
        client.stop();
        digitalWrite(LED_D1, LOW);
        Serial.println("Client disconnected.");
    }
    if (data == "emergency")
    {
     
       digitalWrite(LED_D3, HIGH);
       digitalWrite(D3, HIGH);
       digitalWrite(LED_D2, LOW);
       digitalWrite(D2, LOW);
       digitalWrite(LED_D1, LOW);
       digitalWrite(D1, LOW);
        delay(3000);
        Serial.println("it is green");
        digitalWrite(LED_D1, HIGH);
        digitalWrite(D1, HIGH);
        digitalWrite(LED_D3, LOW);
       digitalWrite(D3, LOW);
       digitalWrite(LED_D2, LOW);
       digitalWrite(D2, LOW);
        delay(1000);
        Serial.println("it is yellow");
        digitalWrite(LED_D2, HIGH);
        digitalWrite(D2, HIGH);
        digitalWrite(LED_D1, LOW);
       digitalWrite(D1, LOW);
       digitalWrite(LED_D3, LOW);
       digitalWrite(D3, LOW);
        delay(1000);
        Serial.println("it is red");
         digitalWrite(LED_D1, HIGH);
         digitalWrite(D1, HIGH);
        digitalWrite(LED_D3, LOW);
       digitalWrite(D3, LOW);
       digitalWrite(LED_D2, LOW);
       digitalWrite(D2, LOW);
        delay(1000);
        Serial.println("it is yellow");
        data="no";
     
    }
    else
    {
     
      digitalWrite(LED_D3, HIGH);
      digitalWrite(D3, HIGH);
       digitalWrite(LED_D2, LOW);
       digitalWrite(D2, LOW);
       digitalWrite(LED_D1, LOW);
       digitalWrite(D1, LOW);
        delay(1000);
        Serial.println("it is green");
        digitalWrite(LED_D1, HIGH);
        digitalWrite(D1, HIGH);
        digitalWrite(LED_D3, LOW);
       digitalWrite(D3, LOW);
       digitalWrite(LED_D2, LOW);
       digitalWrite(D2, LOW);
        delay(1000);
        Serial.println("it is yellow");
        digitalWrite(LED_D2, HIGH);
        digitalWrite(D2, HIGH);
        digitalWrite(LED_D1, LOW);
       digitalWrite(D1, LOW);
       digitalWrite(LED_D3, LOW);
       digitalWrite(D3, LOW);
        delay(1000);
        Serial.println("it is red");
         digitalWrite(LED_D1, HIGH);
        digitalWrite(D1, HIGH);
        digitalWrite(LED_D3, LOW);
       digitalWrite(D3, LOW);
       digitalWrite(LED_D2, LOW);
       digitalWrite(D2, LOW);
        delay(1000);
        Serial.println("it is yellow");
       
    }

    delay(100); // Add a small delay to avoid high CPU usage
}