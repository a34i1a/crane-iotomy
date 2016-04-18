void setup() {
  // put your setup code here, to run once:
Serial.begin(9600);
Serial.flush();
pinMode(7, OUTPUT);
pinMode(5, OUTPUT);
pinMode(2, OUTPUT);
}
String inData;
int val0 = 255;
int value0 = 163;
int valued = 255;
int valRead = 0;
//int valToWrite = 255;
void loop() {
  // if serial communication hath transpired
  while (Serial.available() > 0){
    //String dataread = Serial.readString();
    char dataread = Serial.read();
    inData += dataread;
    Serial.println("charRead=");
    Serial.println(dataread - 48);
    if (dataread == '!') {
      //int val1 = inData.charAt(0) - 48;
      int val1 = inData.charAt(0) - 48;
      int val2 = inData.charAt(1) - 48;
      int val3 = inData.charAt(2) - 48;
      valRead = val1*100+val2*10+val3;
    //  int valRead = dataread.toInt();
      Serial.println("valRead=");
      Serial.println(valRead);
      if (valRead <= 255){
      if (valRead < 0){valRead=0;}
      val0 = valRead;
      inData = "";
      Serial.println("writing to pin 5");
      }
      else if (valRead > 255 && valRead <= 510)
      {
        value0 = valRead-255;
        inData = "";
        Serial.println("writing to pin 7");
       }
       else if (valRead > 510 && valRead <= 765)
       {
        valued = valRead-510;
        inData = "";
        Serial.println("writing to pin 2");
        }
      Serial.flush();
      
    }
  }
  //valToWrite = map(val0,0,999,0,255);
  //Serial.println("pin 5");
//Serial.println(val0);
  analogWrite(5, val0);
  //Serial.println("pin 7");
  //Serial.println(value0);
  analogWrite(7, value0);
  //Serial.println("pin 2");
  //Serial.println(valued);
  analogWrite(2, valued);
  delay(1000); 
  Serial.flush();
  
}
