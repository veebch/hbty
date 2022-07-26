[![YouTube Channel Views](https://img.shields.io/youtube/channel/views/UCz5BOU9J9pB_O0B8-rDjCWQ?label=YouTube&style=social)](https://www.youtube.com/channel/UCz5BOU9J9pB_O0B8-rDjCWQ)

# hbty

Pico party. It will wait until the lights go dim, light its fake flickery candle and play happy birthday on its tiny buzzer.

# Components
- Raspberry pi pico
- 220 ohm resistor
- Yellow LED
- Buzzer
- Photoresistor

# Assembly 

Solder the components directly to the board (see photo). 

Buzzer to GND and GP15. Photoresistor to GND and GP26 and GND to resistor to LED cathode (short leg), LED anode (long leg) to GP16.

Copy the code to a file called `main.py` at the root directory of the pico. Now every time you plug it in, it will be poised to sing Happy Birthday (once) when the lights go down.
