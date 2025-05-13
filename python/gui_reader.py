from gpiozero import DistanceSensor
from guizero import App, Text

sensor = DistanceSensor(echo=18,trigger=17)

def mes():
    cm = sensor.distance * 100
    inch = cm / 2.5
    reading_text.value = str(cm)

app = App(width=300, height=150)
reading_text = Text(app, size=100) 
reading_text.repeat(1000, mes)
app.display()
