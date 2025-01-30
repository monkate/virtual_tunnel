int E1 = 6;
int M1 = 5;
int E2 = 10;
int M2 = 9;
int E3 = 11;
int M3 = 3;
int E_switch = 13; //switches between "GND" & "3.3V"

void setup()
{
    pinMode(M1, OUTPUT);
    pinMode(E1, OUTPUT);
    pinMode(M2, OUTPUT);
    pinMode(E2, OUTPUT);
    pinMode(M3, OUTPUT);
    pinMode(E3, OUTPUT);
    pinMode(E_switch, INPUT);
    delay(500);
}

void loop()
{
    int ll = 1;
    ll = digitalRead(E_switch);
    if (ll == 0) //GND
    {
      analogWrite(E1,240);
      analogWrite(E2,210);
      analogWrite(E3,210);
      digitalWrite(M1, HIGH);   //PWM Speed Control
      digitalWrite(M2, HIGH);   //PWM Speed Control
      digitalWrite(M3, HIGH);   //PWM Speed Control
      //delay(2000); //wait for 2 sec
    }
    else //3.3V
    { 
      analogWrite(E1,240); //255 max; 50 min
      analogWrite(E2,210); //255 max; 50 min
      analogWrite(E3,210); //255 max; 50 min
      analogWrite(M1, LOW);   //PWM Speed Control
      analogWrite(M2, LOW);   //PWM Speed Control
      analogWrite(M3, LOW);   //PWM Speed Control
      //delay(6000);
    }

}