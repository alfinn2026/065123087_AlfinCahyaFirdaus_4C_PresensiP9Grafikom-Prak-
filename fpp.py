from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController

app  = Ursina()

Sky()

DirectionalLight()

ground = Entity (
    model = 'plane',
    scale = (20,1,20),
    color = color.green,
    Collider = 'box',
)

player = FirstPersonController(
    position = (0, 1, -5),
    speed = 5
)

player.gravity = 0.5

player.cursor.visible = True

app.run()