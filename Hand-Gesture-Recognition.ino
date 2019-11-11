#include<Wire.h>
#include <LiquidCrystal.h>

const int MPU=0x68;
int16_t AcX,AcY,AcZ,Tmp;
int l=9,r=8,u=7,d=6;
const int rs = 10, en = 11, d4 = 5, d5 = 4, d6 = 3, d7 = 2;

LiquidCrystal lcd(rs, en, d4, d5, d6, d7);

// Set this to true for ML train
bool train = false; 

void setup(){
  lcd.begin(16, 2);
  Wire.begin();
  Wire.beginTransmission(MPU);
  Wire.write(0x6B);
  Wire.write(0);    
  Wire.endTransmission(true);
  pinMode(l, OUTPUT);
  pinMode(r, OUTPUT);
  pinMode(u, OUTPUT);
  pinMode(d, OUTPUT);
  Serial.begin(9600);
}
void loop(){
  lcd.clear();
  Wire.beginTransmission(MPU);
  Wire.write(0x3B);  
  Wire.endTransmission(false);
  Wire.requestFrom(MPU,12,true);  
  AcX=Wire.read()<<8|Wire.read();    
  AcY=Wire.read()<<8|Wire.read();
  AcZ=Wire.read()<<8|Wire.read();
  Serial.println(AcX);
  Serial.println(AcY);
  Serial.println(AcZ);

  char c[16]="                ";
  for(int i=0;i<15;i++)
  {
    c[i]=Serial.read();
  }
  
  lcd.setCursor(0,0);
  lcd.print("Gesture Output");
  lcd.setCursor(0,1);
  lcd.print(c);

  if(train)
    delay(100);
  else
    delay(300);
}