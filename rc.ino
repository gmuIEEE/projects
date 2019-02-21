//Code for Transmitter Circuit

// Include RadioHead Amplitude Shift Keying Library
#include <RH_ASK.h>
// Include dependant SPI Library 
#include <SPI.h> 
 
// Create Amplitude Shift Keying Object
RH_ASK rf_driver;

int pinx= A5;
int piny =A4;
int pinz=A3;

int pinT=11;

int x=0;
int y=0;
int z=0;

void setup()
{
    // Initialize ASK Object
    rf_driver.init(); 
    Serial.begin(9600);  
    pinMode(pinT,OUTPUT);

}
 
void loop()
{
    x=analogRead(pinx);
    y=analogRead(piny);
    z=analogRead(pinz);

    if(y<300){
  Serial.println("right \t");
  const char *msg = "R";
    rf_driver.send((uint8_t *)msg, strlen(msg));
    rf_driver.waitPacketSent();
 //   delay(500);
  
}
if(y>370){
  Serial.println("left");
  const char *msg = "L";
    rf_driver.send((uint8_t *)msg, strlen(msg));
    rf_driver.waitPacketSent();
//    delay(500);
}
if(x<315){
  Serial.println("forward");
  const char *msg = "F";
    rf_driver.send((uint8_t *)msg, strlen(msg));
    rf_driver.waitPacketSent();
//    delay(500);
  
}
if(x>365){
  Serial.println("backward");
  const char *msg = "B";
    rf_driver.send((uint8_t *)msg, strlen(msg));
    rf_driver.waitPacketSent();
//    delay(500);
}

  if (x<365 && x>315 && y <370 && y>300) {
    Serial.println("stop");
  const char *msg = "S";
    rf_driver.send((uint8_t *)msg, strlen(msg));
    rf_driver.waitPacketSent();
//    delay(500);
  }

}








//Code for Reciever

#include <RH_ASK.h>
// Include dependant SPI Library 
#include <SPI.h> 
 
// Create Amplitude Shift Keying Object
RH_ASK rf_driver;

char message=0;


//Declaration Motors drivers
int m1 = 10;
int m2 = 9;
int m3=5;
int m4=6;


void setup()
{
    // Initialize ASK Object
    rf_driver.init();
    // Setup Serial Monitor
    Serial.begin(9600);
    pinMode(m1, OUTPUT);
pinMode(m2, OUTPUT);
pinMode(m3, OUTPUT);
pinMode(m4, OUTPUT);
}
 
void loop()
{
    // Set buffer to size of expected message
    uint8_t buf[1];
    uint8_t buflen = sizeof(buf);
    // Check if received packet is correct size
    if (rf_driver.recv(buf, &buflen))
    {
     message= *buf;
     //Serial.println(message);
if (message=='F') {
  Serial.println("this is forward");
  

  // forward
digitalWrite(m1,LOW);
digitalWrite(m2,HIGH);
digitalWrite(m3,LOW);
digitalWrite(m4,HIGH);
 
}

if (message=='L') {
  Serial.println("this is left");
 digitalWrite(m1,LOW);
digitalWrite(m2,LOW);
digitalWrite(m3,LOW);
digitalWrite(m4,HIGH);
}

if (message=='R') {
  Serial.println("this is right");
digitalWrite(m1,LOW);
digitalWrite(m2,HIGH);
digitalWrite(m3,LOW);
digitalWrite(m4,LOW);
}

if (message=='B') {
  Serial.println("this is backward");
digitalWrite(m1,HIGH);
digitalWrite(m2,LOW);
digitalWrite(m3,HIGH);
digitalWrite(m4,LOW);
}

      // Message received with valid checksum
      //Serial.print("Message Received: ");
//Serial.println((char*)buf);     
   
    }
}
