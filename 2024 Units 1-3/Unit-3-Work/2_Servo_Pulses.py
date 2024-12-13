from machine import Pin,ADC,PWM
import time

servo1=PWM(Pin(0))
servo2=PWM(Pin(1))
servo1.freq(50)
servo2.freq(50)

def move_servo(angle):
    # Convert angle to duty cycle (0° -> 0.5ms, 90° -> 1.5ms, 180° -> 2.5ms)
    min_duty = 1000  # 1ms
    max_duty = 9000  # 2ms
    duty = int(min_duty + (angle / 180) * (max_duty - min_duty))
    servo1.duty_u16(duty) #Converts the binary signal to unicode value
    servo2.duty_u16(duty)

# Example: sweep servo from 0° to 180° and back
while True:
    for angle in range(0, 181, 3): 
# Servo only goes 180 degrees, hence a range of 180. 3 represents how many steps/positions it moves.
        move_servo(angle)
        time.sleep(0.02) # the move 
    for angle in range(180, -1, -3):
# Servo only goes 180 degrees, hence a range of 180. But the values are now descending. 3 represents how many steps/positions it moves.
        move_servo(angle)
        time.sleep(0.02)