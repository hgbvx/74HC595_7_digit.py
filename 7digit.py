# Simple 7 segment 1-digit display library
# CC - common cathode
# Shift register - 74HC595
# Raspberry pico
# @Michal Rojewski
# 03.2020
#

from machine import Pin
import time

data = Pin(19, Pin.OUT, value=0)
clock = Pin(18, Pin.OUT, value=0)
latch = Pin(16, Pin.OUT, value=0)

def bit8_array(num): #returns 8bit value in array
    x=[]
    for i in range(8):
        x.append(num%2)
        num=int(num/2)
    return x

def display_digit(digit): #displaying digit on 7 segment display
    
    if digit == 0:
        x = 63
    if digit == 1:
        x = 6
    if digit == 2:
        x = 91
    if digit == 3:
        x = 79
    if digit == 4:
        x = 102
    if digit == 5:
        x = 109
    if digit == 6:
        x = 125
    if digit == 7:
        x = 7
    if digit == 8:
        x = 127
    if digit == 9:
        x = 103
    
    bit_nr = bit8_array(x)
    
    for i in bit_nr:
        data.value(i)
        clock.value(1)
        clock.value(0)
    latch.value(1)
    latch.value(0)
        

display_digit(4)

# for i in a:
#     print(i)
#     data.value(i)
#     clock.value(1)
#     clock.value(0)
# latch.value(1)
# latch.value(0)


#for value in [63,6,91,79,102,109,125,7,127,103]:
 #   print(value)

# while True:
#     for value in [63,6,91,79,102,109,125,7,127,103]:
#         bits = [value >> i & 1 for i in range(7,-1,-1)]
#         for i in range(7,-1,-1):
#             print(bits[i])
#             data.value(bits[i])
#             clock.value(1)
#             clock.value(0)
#         print()
#         latch.value(1)
#         latch.value(0)
# 
#         time.sleep_ms(000)