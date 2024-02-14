import bpy
import random
# Blender Tutorial 0020: Create Random Height Buildings using Blender Python
# (C) 2024 Mastershin AI.com - MIT License.

###################################################################################
# Danger: Ensure we're in object mode and clear / delete all the object
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
# Main Object Creation Part:
###################################################################################

bpy.ops.mesh.primitive_grid_add(size=50, location=(0, 0, 0))

for x in range(-20, 20, 5):
    for y in range(-20, 20, 5):
        
        bpy.ops.mesh.primitive_cube_add(size=1, location=(x, y, 0))
        
        obj = bpy.context.object

        height = random.randint(5, 10)
        obj.scale.z = height
        obj.location.z += height / 2
        


#bpy.ops.mesh.primitive_cylinder_add(radius=1, depth=2, location=(-15, 0, 0)) # , vertices=32)
#bpy.ops.mesh.primitive_cone_add(radius1=1, depth=2, location=(-10, 0, 0)) # , vertices=32)
#bpy.ops.mesh.primitive_torus_add(location=(-5, 0, 0), major_radius=1, minor_radius=0.5) # , major_segments=48, minor_segments=12)
#bpy.ops.mesh.primitive_cube_add(size=1, location=(0, 0, 0))
#bpy.ops.mesh.primitive_plane_add(size=1, location=(5, 0, 0))
#bpy.ops.mesh.primitive_circle_add(radius=1, location=(10, 0, 0)) # , vertices=32)
#bpy.ops.mesh.primitive_monkey_add(size=2, location=(15, 0, 0))


# Ensure we have a camera in the scene
if not bpy.context.scene.camera:
    bpy.ops.object.camera_add()
    camera = bpy.context.object
else:
    camera = bpy.context.scene.camera
    
# Set the camera to look at (0, 0, 0) using a 'TRACK TO' constraint
if "Track To" not in camera.constraints:
    track_to_constraint = camera.constraints.new(type='TRACK_TO')
    track_to_constraint.target = bpy.data.objects.new("Empty", None)
    bpy.context.scene.collection.objects.link(track_to_constraint.target)
    track_to_constraint.target.location = (0, 0, 0)
    track_to_constraint.up_axis = 'UP_Y'
    track_to_constraint.track_axis = 'TRACK_NEGATIVE_Z'

# Animation settings
fps = bpy.context.scene.render.fps
duration = 50  # Duration in seconds
start_frame = 1
end_frame = fps * duration

# Define start and end positions for the camera
start_position = (20, -20, 20)  # Starting position of the camera
end_position = (20, 20, 20)    # Ending position of the camera

# Set initial camera position and insert a keyframe
camera.location = start_position
camera.keyframe_insert(data_path="location", frame=start_frame)

# Set final camera position and insert a keyframe
camera.location = end_position
camera.keyframe_insert(data_path="location", frame=end_frame)

# Ensure the camera is always looking at the target by updating the 'Track To' constraint
camera.constraints["Track To"].target.location = (0, 0, 0)

# Optionally, set interpolation to linear for smooth camera movement
for fcurve in camera.animation_data.action.fcurves:
    for keyframe in fcurve.keyframe_points:
        keyframe.interpolation = 'LINEAR'