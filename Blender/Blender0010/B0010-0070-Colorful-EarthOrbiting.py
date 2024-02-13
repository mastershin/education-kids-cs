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
# Create a sun
###################################################################################
bpy.ops.mesh.primitive_uv_sphere_add(radius=3, location=(0,0,0))
obj = bpy.context.object
# Set sun color
mat = bpy.data.materials.new(name="Sun_Material")
mat.diffuse_color = (1, 1, 0, 1)  # RGB and alpha
obj.data.materials.append(mat)


###################################################################################
# Create earth
###################################################################################
bpy.ops.mesh.primitive_uv_sphere_add(radius=1, location=(10,0,0))
earth = bpy.context.object
# Set sun color
mat = bpy.data.materials.new(name="Earth_Material")
mat.diffuse_color = (0, 0, 1, 1)  # RGB and alpha
earth.data.materials.append(mat)

###################################################################################
# Set up animation
###################################################################################

# deselect all
bpy.ops.object.select_all(action='DESELECT')

num_frames = 360
scene = bpy.context.scene
scene.frame_start = 1
scene.frame_end = num_frames  # One frame per degree

for frame in range(num_frames):

    # rotate, calculate the angle in radians
    # angle = math.radians(frame)  # Vary speed slightly for each sphere
    
    angle = frame % 360 * 5
    
    x = math.cos(math.radians(angle)) * 10
    y = math.sin(math.radians(angle)) * 10
    z = 0
    # z = math.sin(math.radians(angle)) * 5

    earth.location = (x, y, z)
    # Insert keyframe for location
    earth.keyframe_insert(data_path="location", frame=frame)
