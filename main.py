from machine import ADC, Pin, PWM
from utime import sleep
from urandom import randint, random
import _thread

tones = {
"B0": 31,
"C1": 33,
"CS1": 35,
"D1": 37,
"DS1": 39,
"E1": 41,
"F1": 44,
"FS1": 46,
"G1": 49,
"GS1": 52,
"A1": 55,
"AS1": 58,
"B1": 62,
"C2": 65,
"CS2": 69,
"D2": 73,
"DS2": 78,
"E2": 82,
"F2": 87,
"FS2": 93,
"G2": 98,
"GS2": 104,
"A2": 110,
"AS2": 117,
"B2": 123,
"C3": 131,
"CS3": 139,
"D3": 147,
"DS3": 156,
"E3": 165,
"F3": 175,
"FS3": 185,
"G3": 196,
"GS3": 208,
"A3": 220,
"AS3": 233,
"B3": 247,
"C4": 262,
"CS4": 277,
"D4": 294,
"DS4": 311,
"E4": 330,
"F4": 349,
"FS4": 370,
"G4": 392,
"GS4": 415,
"A4": 440,
"AS4": 466,
"B4": 494,
"C5": 523,
"CS5": 554,
"D5": 587,
"DS5": 622,
"E5": 659,
"F5": 698,
"FS5": 740,
"G5": 784,
"GS5": 831,
"A5": 880,
"AS5": 932,
"B5": 988,
"C6": 1047,
"CS6": 1109,
"D6": 1175,
"DS6": 1245,
"E6": 1319,
"F6": 1397,
"FS6": 1480,
"G6": 1568,
"GS6": 1661,
"A6": 1760,
"AS6": 1865,
"B6": 1976,
"C7": 2093,
"CS7": 2217,
"D7": 2349,
"DS7": 2489,
"E7": 2637,
"F7": 2794,
"FS7": 2960,
"G7": 3136,
"GS7": 3322,
"A7": 3520,
"AS7": 3729,
"B7": 3951,
"C8": 4186,
"CS8": 4435,
"D8": 4699,
"DS8": 4978
}

 song = ["D5","D5","E5","D5","G5","FS5","P", \
        "D5","D5","E5","D5","A5","G5","P", \
        "D5","D5","D6","B5","G5","FS5","E5","P", \
        "C6","C6","B5","G5","A5","G5"]        
 

# f is crotchet
# h is quaver
# d is minim

timing = ["h","h","f","f","f","d","h", \
        "h","h","f","f","f","d","h", \
        "h","h","f","f","f","f","f","h",  \
        "h","h","f","f","f","d"]


def playtone(frequency,buzzer):
    buzzer.duty_u16(6000)
    buzzer.freq(frequency)

def bequiet(buzzer):
    buzzer.duty_u16(0)

def readLight(photoGP):
    photoRes = ADC(Pin(photoGP))
    light = photoRes.read_u16() # with no transform to brightness
    try:
        light =round(10*65535/(light)-10,2)
    except:
        light=100000
    return light

def playsong(mysong, mytiming,buzzerpin):
    sleep(4) # dramatic pause
    notelength=.45
    buzzer = PWM(Pin(buzzerpin))
    print(len(mysong),len(mytiming))
    for i in range(len(mysong)):
        if (mysong[i] == "P"):
            bequiet(buzzer)
        else:
            playtone(tones[mysong[i]],buzzer)
        if mytiming[i]=="f":
            sleep(notelength)
        elif mytiming[i]=="h":
            sleep(notelength/2)
        elif mytiming[i]=="d":
            sleep(notelength*2)
        bequiet(buzzer)
        sleep(.04) # A little between-note pause
        
def flickerloop():
    ledpin=16
    buzzerpin=15
    threshold = 600
    photoPIN = 26    
    pwm = PWM(Pin(ledpin))
    pwm.freq(1000)
    sang=False  # If you want it to skip the musical interlude, set to True and it will never play HBTY       
    while True:
        dazzle = readLight(photoPIN)
        print("Dazzle: " + str(dazzle))
        sleep(.1) # set a delay between readings
        if dazzle<threshold:
            if sang==False:
                try:
                    print("do a song")
                    _thread.start_new_thread(playsong, (song,timing, buzzerpin))
                except Exception as err:
                    print(err)
                sang=True
            flicker=randint(100,300)/100
            pwm.duty_u16(int(65025/flicker))
        else:
            pwm.duty_u16(0)


flickerloop()
