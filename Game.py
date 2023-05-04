from ursina import *
from random import randint

app=Ursina()

field_size=19
Entity(model="quad", scale=60, texture='assets/blue_sky')
field=Entity(model="quad", color=color.rgba(255, 255, 0). scale=(12,18), position=(field_size//2, field_size//2)



app.run()
