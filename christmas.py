from machine import Pin, PWM
from utime import sleep

# =====================
# Jingle Bells - frequencies and timings from BASIC source
# =====================
frequencies = [
    659, 659, 659,                          # Line 10
    659, 659, 659,                          # Line 20
    659, 784, 523, 587, 659,                # Line 30
    698, 698, 698, 698, 698, 659,           # Line 40
    659, 659, 659, 587, 587,                # Line 50
    659, 587, 784, 659, 659, 659,           # Line 60
    659, 659, 659, 659, 784, 523,           # Line 70
    587, 659, 698, 698, 698, 698,           # Line 80
    698, 659, 659, 659, 784, 784,           # Line 90
    698, 587, 523                           # Line 100
]

timings = [
    0.25, 0.25, 0.5,                        # Line 10
    0.25, 0.25, 0.5,                        # Line 20
    0.25, 0.25, 0.25, 0.25, 1,              # Line 30
    0.25, 0.25, 0.25, 0.25, 0.25, 0.25,    # Line 40
    0.25, 0.25, 0.25, 0.25, 0.25,           # Line 50
    0.25, 0.5, 0.5, 0.25, 0.25, 0.5,        # Line 60
    0.25, 0.25, 0.5, 0.25, 0.25, 0.25,      # Line 70
    0.25, 1, 0.25, 0.25, 0.25, 0.25,        # Line 80
    0.25, 0.25, 0.25, 0.25, 0.25, 0.25,     # Line 90
    0.25, 0.25, 1                           # Line 100
]

# =====================
# Audio helpers
# =====================
def playtone(freq, buzzer):
    buzzer.freq(freq)
    buzzer.duty_u16(60000)

def bequiet(buzzer):
    buzzer.duty_u16(0)

# =====================
# Play song
# =====================
def playsong(freqs, durs, buzzerpin):
    sleep(1)  # dramatic pause
    buzzer = PWM(Pin(buzzerpin))
    buzzer.duty_u16(0)
    for freq, dur in zip(freqs, durs):
        playtone(freq, buzzer)
        sleep(dur)
        bequiet(buzzer)
        sleep(0.02)  # short gap for articulation

# =====================
# Main
# =====================
buzzerpin = 15
playsong(frequencies, timings, buzzerpin)
