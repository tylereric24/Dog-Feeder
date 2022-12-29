#include <Servo.h>
#include <ArduinoBLE.h>


Servo dogFeeder; //servo object
void setupFeeder() 
{
  dogFeeder.attach(9); //set arduino pin D9
}

BLEService ledService("180A"); // BLE LED Service

// BLE LED Switch Characteristic - custom 128-bit UUID, read and writable by central
BLEByteCharacteristic switchCharacteristic("2A57", BLERead | BLEWrite);

void setup()
{
  Serial.begin(9600);
  setupFeeder();
  
  while (!Serial);

  // set built in LED pin to output mode
//  pinMode(LED_BUILTIN, OUTPUT);

  // begin initialization
  if (!BLE.begin()) 
  {
    Serial.println("starting Dog Feeder Project");

    while (1);
  }

  // set advertised local name and service UUID:
  BLE.setLocalName("Nano 33 IoT");
  BLE.setAdvertisedService(ledService);

  // add the characteristic to the service
  ledService.addCharacteristic(switchCharacteristic);

  // add service
  BLE.addService(ledService);

  // set the initial value for the characteristic:
  switchCharacteristic.writeValue(0);

  // start advertising
  BLE.advertise();

  Serial.println("Dog Feeder");
}

void loop() 
{
  // listen for BLE peripherals to connect:
  BLEDevice central = BLE.central();

  // if a central is connected to peripheral:
  if(central) 
  {
    Serial.print("Connected to central: ");
    // print the central's MAC address:
    Serial.println(central.address());

    // while the central is still connected to peripheral:
    while(central.connected()) 
    {
      // if the remote device wrote to the characteristic,
      // use the value to control the arm of the servo:
      if(switchCharacteristic.written()) 
        {
          if(switchCharacteristic.value() == 1) //opens once
          {
            dogFeeder.write(0); //set start point degrees
 		        delay(1000);
		        dogFeeder.write(360); //moves it open		
		        delay(1000); 
		        dogFeeder.write(360); //closes
          }
          if(switchCharacteristic.value() == 2) //opens 2 times
          {
            dogFeeder.write(0); //set start point degrees
 		        delay(1000);
		        dogFeeder.write(360); //moves it open		
		        delay(1000); 
		        dogFeeder.write(360); //closes
		        delay(1000);
		        dogFeeder.write(360); //moves it open		
		        delay(1000); 
		        dogFeeder.write(360); //closes
          }
          if(switchCharacteristic.value() == 3) //opens 3 times
          {
            dogFeeder.write(0); //set start point degrees
 		        delay(1000);
		        dogFeeder.write(360); //moves it open		
		        delay(1000); 
		        dogFeeder.write(360); //closes
		        delay(1000);
		        dogFeeder.write(360); //moves it open		
		        delay(1000); 
		        dogFeeder.write(360); //closes
		        delay(1000);
		        dogFeeder.write(360); //moves it open		
		        delay(1000); 
		        dogFeeder.write(360); //closes
          }
        }
    } //end of while
  } //end of if central
} //end of loop() 
