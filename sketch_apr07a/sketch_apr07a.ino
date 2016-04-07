void setup() {
  // put your setup code here, to run once:
Serial.begin(9600);
Serial.flush();
}
String inData;
void loop() {
  // if serial communication hath transpired
  while (Serial.available() > 0){
    char dataread = Serial.read();
    inData += dataread;
    if (dataread == '!'){
      int val1 = inData.charAt(0) - 48;
      int val2 = inData.charAt(1) - 48;
      int val3 = inData.charAt(2) - 48;
      int val4 = inData.charAt(3) - 48;
      int val0 = val1*1000+val2*100+val3*10+val4;
      Serial.println(val0);
      }
    }
}
