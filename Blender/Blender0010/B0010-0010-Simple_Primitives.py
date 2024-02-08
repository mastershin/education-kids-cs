import bpy
# Blender Tutorial 0010: Create Primitive Objects using Blender Python (bpy library)
# (C) 2024 Mastershin AI. MIT License.

bpy.ops.object.select_all(action='DESELECT')

# Iterate over all objects in the scene
#for obj in bpy.context.scene.objects:
#    if obj.type == 'MESH':
#        obj.select_set(True)
#        

# or in one-liner
[obj.select_set(True) for obj in bpy.context.scene.objects if obj.type == 'MESH']
# actually remove the selected object
bpy.ops.object.delete()

# Main Object Creation Part:

#bpy.ops.mesh.primitive_grid_add(size=20, location=(0, 0, 0))

bpy.ops.mesh.primitive_cylinder_add(radius=1, depth=2, location=(-15, 0, 0)) # , vertices=32)
bpy.ops.mesh.primitive_cone_add(radius1=1, depth=2, location=(-10, 0, 0)) # , vertices=32)
bpy.ops.mesh.primitive_torus_add(location=(-5, 0, 0), major_radius=1, minor_radius=0.5) # , major_segments=48, minor_segments=12)
bpy.ops.mesh.primitive_cube_add(size=1, location=(0, 0, 0))
bpy.ops.mesh.primitive_plane_add(size=1, location=(5, 0, 0))
bpy.ops.mesh.primitive_circle_add(radius=1, location=(10, 0, 0)) # , vertices=32)
bpy.ops.mesh.primitive_monkey_add(size=2, location=(15, 0, 0))

