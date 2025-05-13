from gpiozero import MotionSensor,Buzzer
import time
buzzer= Buzzer(18)
def buzz(pitch, duration):
    period = 1.0 / pitch
    delay = period / 2
    cycles = int(duration * pitch)
    buzzer.beep(on_time=period, off_time=period, n=int(cycles/2))
pir = MotionSensor(23)

while True:
    pir.wait_for_motion()
    print("Motion detected!")
    buzz(20,0.25)
    time.sleep(0.3)
