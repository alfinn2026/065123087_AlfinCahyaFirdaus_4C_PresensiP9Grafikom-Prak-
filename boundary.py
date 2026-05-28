from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController

app = Ursina()

# GROUND
ground = Entity(
    model='plane',
    collider='box',
    scale=65,
    texture='grass',
    texture_scale=(4, 4)
)

wall_height = 5
wall_thickness = 1
ground_size = 65

# TEMBOK DEPAN
Entity(
    model='cube',
    position=(0, wall_height/2, ground_size/2),
    scale=(ground_size, wall_height, wall_thickness),
    collider='box',
    visible=False
)

# TEMBOK BELAKANG
Entity(
    model='cube',
    position=(0, wall_height/2, -ground_size/2),
    scale=(ground_size, wall_height, wall_thickness),
    collider='box',
    visible=False
)

# TEMBOK KANAN
Entity(
    model='cube',
    position=(ground_size/2, wall_height/2, 0),
    scale=(wall_thickness, wall_height, ground_size),
    collider='box',
    visible=False
)

# TEMBOK KIRI
Entity(
    model='cube',
    position=(-ground_size/2, wall_height/2, 0),
    scale=(wall_thickness, wall_height, ground_size),
    collider='box',
    visible=False
)

# KUBUS
Entity(
    model='cube',
    origin_y=-0.5,
    scale=2,
    texture='brick',
    texture_scale=(1, 2),
    collider='box'
)

# CAMERA EDITOR
editor_camera = EditorCamera(
    enabled=False,
    ignore_paused=True
)

# PLAYER
player = FirstPersonController(
    model='cube',
    z=-10,
    color=color.red,
    origin_y=-0.5,
    speed=8,
    collider='box'
)

player.collider = BoxCollider(
    player,
    Vec3(0, 1, 0),
    Vec3(1, 2, 1),
)

# LIGHT
sun = DirectionalLight()
sun.look_at(Vec3(1, -1, -1))

Sky()

app.run()