#Completed game - experiment and adjust to suit your circuit

from machine import Pin,ADC,PWM
from time import sleep

#Configure the servo pins for PWM output
servo1=PWM(Pin(0))
servo2=PWM(Pin(1))

servo1.freq(50)
servo2.freq(50)

#Configure the potentiometer pins for ADC input
potentiometer1=ADC(Pin(26))
potentiometer2=ADC(Pin(27))



LDR=ADC(Pin(28))    #Configure LDR potential divider pin as ADC input
buzzer=PWM(Pin(15)) #Configure buzzer pin for PWM output
Buzzerpower = Pin(14, Pin.OUT, value=1)
score=0             #Start game with no points

tones = { "B0": 31, "C1": 33, "CS1": 35, "D1": 37, "DS1": 39, "E1": 41, "F1": 44, "FS1": 46, "G1": 49, "GS1": 52, "A1": 55, "AS1": 58, "B1": 62, "C2": 65, "CS2": 69, "D2": 73, "DS2": 78, "E2": 82, "F2": 87, "FS2": 93, "G2": 98, "GS2": 104, "A2": 110, "AS2": 117, "B2": 123, "C3": 131, "CS3": 139, "D3": 147, "DS3": 156, "E3": 165, "F3": 175, "FS3": 185, "G3": 196, "GS3": 208, "A3": 220, "AS3": 233, "B3": 247, "C4": 262, "CS4": 277, "D4": 294, "DS4": 311, "E4": 330, "F4": 349, "FS4": 370, "G4": 392, "GS4": 415, "A4": 440, "AS4": 466, "B4": 494, "C5": 523, "CS5": 554, "D5": 587, "DS5": 622, "E5": 659, "F5": 698, "FS5": 740, "G5": 784, "GS5": 831, "A5": 880, "AS5": 932, "B5": 988, "C6": 1047, "CS6": 1109, "D6": 1175, "DS6": 1245, "E6": 1319, "F6": 1397, "FS6": 1480, "G6": 1568, "GS6": 1661, "A6": 1760, "AS6": 1865, "B6": 1976, "C7": 2093, "CS7": 2217, "D7": 2349, "DS7": 2489, "E7": 2637, "F7": 2794, "FS7": 2960, "G7": 3136, "GS7": 3322, "A7": 3520, "AS7": 3729, "B7": 3951, "C8": 4186, "CS8": 4435, "D8": 4699, "DS8": 4978 }
song = ["E5","G5","A5","P","E5","G5","B5","A5","P","E5","G5","A5","P","G5","E5"]
#CHANGE THIS TO ANOTHER SONG

def playsong(mysong):
    for i in range(len(mysong)):
        if (mysong[i] == "P"):
            bequiet()
        else:
            playtone(tones[mysong[i]])
        sleep(0.3)
    bequiet()

def playtone(frequency):
    buzzer.duty_u16(1000)
    buzzer.freq(frequency)

def bequiet():
    buzzer.duty_u16(0)
              
def reset():
    '''Reset score variable and provide user feedback before a new game'''
    global score
    score=0
    beep(2)
    print("Ready for new game")
    
def beep(numBeeps):
    '''Turn the buzzer on and off a given number of times'''
    print("Beep")
    for i in range(numBeeps):
        buzzer.duty_u16(1000)
        buzzer.freq(1000)
        sleep(0.2)
        buzzer.duty_u16(0)
        sleep(0.1)

def winningSound():
    '''Play a nice winning sound'''
    print("Winner!")
    playsong(song)
    #add a better winning sound here - eg loop through a range of frequencies in quick succession
        
reset()

while True:
    #these lines set the duty cycle to a value between 3000 & 7000
    #which corresponds to a pulse width of 1ms to 2ms
    servo1Value=int(3000+potentiometer1.read_u16()*4000/65536)
    servo2Value=int(3000+potentiometer2.read_u16()*4000/65536)
    servo1.duty_u16(servo1Value)
    servo2.duty_u16(servo2Value)

    if LDR.read_u16()<500: #Strong light detected - change this value to suit your room and LDR
        score=score+10
        buzzer.freq(score+100)
        buzzer.duty_u16(score+1000)
        print(score)
        if score>1000:      #If the game has been won, play a sound and get ready for the next round
            winningSound()
            reset()
    else:                   #Strong light not detected .. do nothing (turn the buzzer off)
        buzzer.duty_u16(0)

    sleep(0.1)

