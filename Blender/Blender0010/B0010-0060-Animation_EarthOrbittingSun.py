import bpy
import math

###################################################################################
# Danger: Ensure we're in object mode and clear / delete all the object
###################################################################################
# Change to Object Mode
if bpy.ops.object.mode_set.poll():
    bpy.ops.object.mode_set(mode='OBJECT')

bpy.ops.object.select_all(action='DESELECT')

# Iterate over all objects in the scene
#for obj in bpy.context.scene.objects:
#    if obj.type == 'MESH':
#        obj.select_set(True)

# or in one-liner
[obj.select_set(True) for obj in bpy.context.scene.objects if obj.type == 'MESH']
# actually remove the selected object
bpy.ops.object.delete()
###################################################################################

###################################################################################
# Create a sun
###################################################################################
bpy.ops.mesh.primitive_uv_sphere_add(radius=3, location=(0,0,0))

###################################################################################
# Create earth
###################################################################################
bpy.ops.mesh.primitive_uv_sphere_add(radius=1, location=(10,0,0))
earth = bpy.context.object

###################################################################################
# Set up animation
###################################################################################
num_frames = 360
scene = bpy.context.scene
scene.frame_start = 1
scene.frame_end = num_frames  # One frame per degree

for frame in range(num_frames):

    # rotate, calculate the angle in radians
    angle = math.radians(frame)  # Vary speed slightly for each sphere
    x = math.cos(angle) * 10
    y = math.sin(angle) * 10

    earth.location = (x, y, 0)
    # Insert keyframe for location
    earth.keyframe_insert(data_path="location", frame=frame)
