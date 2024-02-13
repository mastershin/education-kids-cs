import bpy
import math

###################################################################################
# Danger: Ensure we're in object mode and clear / delete all the object
###################################################################################
def delete_all():
    # Change to Object Mode
    if bpy.ops.object.mode_set.poll():
        bpy.ops.object.mode_set(mode='OBJECT')
    bpy.ops.object.select_all(action='DESELECT')
    [obj.select_set(True) for obj in bpy.context.scene.objects if obj.type == 'MESH']
    bpy.ops.object.delete()
delete_all()
###################################################################################

###################################################################################
# Set up animation
###################################################################################
class Planet:
    def __init__(self, name, radius, distance, orbital_speed, color):
        self.name = name
        self.radius = radius
        self.distance = distance
        self.angle = 0
        self.orbital_speed = orbital_speed  # This could represent the angle step or a period
        self.color = color  # RGB values as a tuple
        self.object = None
        self.create_planet()

    def create_planet(self):
        # Create a UV sphere with the given radius and move it to its initial location
        bpy.ops.mesh.primitive_uv_sphere_add(radius=self.radius, location=(self.distance, 0, 0))
        self.object = bpy.context.object
        self.object.name = self.name

        # Set planet color
        mat = bpy.data.materials.new(name=f"{self.name}_Material")
        mat.diffuse_color = (*self.color, 1)  # RGB and alpha
        self.object.data.materials.append(mat)

    def update_location2(self, frame):
        # Update the planet's location based on its current angle
        x = cos(radians(self.angle)) * self.distance
        y = sin(radians(self.angle)) * self.distance
        self.object.location = (x, y, 0)
        self.object.keyframe_insert(data_path="location", frame=frame)

        # Increment the angle for the next frame
        self.angle += self.angle_step

    def update_location(self, frame, num_frames):
        # Calculate the angle based on the orbital speed and the current frame
        # Ensure continuous movement by considering the total number of frames and the planet's speed
        self.angle = (360 / num_frames) * self.orbital_speed * frame % 360
        x = math.cos(math.radians(self.angle)) * self.distance
        y = math.sin(math.radians(self.angle)) * self.distance
        self.object.location = (x, y, 0)
        self.object.keyframe_insert(data_path="location", frame=frame)
        
def setup_animation(planets, num_frames):
    scene = bpy.context.scene
    scene.frame_start = 1
    scene.frame_end = num_frames

    for frame in range(1, num_frames + 1):
        for planet in planets:
            planet.update_location(frame, num_frames)

planets = [
    Planet("Sun", radius=3, distance=0, orbital_speed=0, color=(1, 1, 0)),  # Yellow Sun
    Planet("Earth", radius=1, distance=10, orbital_speed=2, color=(0, 0, 1)),  # Blue Earth
    Planet("Mars", radius=0.5, distance=15, orbital_speed=4, color=(1, 0, 0)),  # Red Mars
    Planet("Alien1", radius=0.5, distance=20, orbital_speed=6, color=(1, 0, 0)),  # Red Mars
    Planet("Alient2", radius=0.5, distance=25, orbital_speed=8, color=(1, 0, 0)),  # Red Mars        
]
setup_animation(planets, num_frames=360)
