from ursina import *

app = Ursina()

Sky()

DirectionalLight()

AmbientLight(
    color = color.rgba(100, 100, 100, 0.5)
)

ground = Entity (
    model = 'plane',
    texture = 'white_cube',
    texture_scale = (30, 30),
    scale = 30,
    color = color.gray,
    Collider = 'box',
)

player = Entity(
    model = 'sphere',
    color = color.red,
    scale = 1,
    position = (0, 1, 0),
    collider = 'sphere'
)

def update():
    speed = 5 * time.dt
    if held_keys['w']:
        player.z += speed

    if held_keys['s']:
        player.z -= speed

    if held_keys['a']:
        player.x -= speed

    if held_keys['d']:
        player.x += speed

    camera.position = player.position + Vec3(0, 5, -12)
    camera.look_at(player)

app.run()