[![YouTube Channel Views](https://img.shields.io/youtube/channel/views/UCz5BOU9J9pB_O0B8-rDjCWQ?label=YouTube&style=social)](https://www.youtube.com/channel/UCz5BOU9J9pB_O0B8-rDjCWQ)

# Micropython Birthday 'Candle'

Pico party. It will wait until the lights go dim, light its fake flickery candle and play happy birthday on its tiny buzzer. If you just want to add a flickery nightlight to a project, you can just omit the buzzer part.

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

# Video

[![Explainer vid](http://img.youtube.com/vi/56xwBkNzca4/0.jpg)](http://www.youtube.com/watch?v=56xwBkNzca4 "Video Title")

# Christmas Version (Jingle Bells)

In the file [christmas.py](/christmas.py) The LDR is removed and the flickering LED is replaced with a 820nm red led which is connected to VSYS so that it is nice and bright.
