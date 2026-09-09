bl_info = {
    "name": "Material Replacer",
    "author": "BlenderMark",
    "version": (1, 0),
    "blender": (4, 5, 0),
    "location": "3D View > N Panel > Material Replacer",
    "description": "Replace one material with another",
    "category": "3D View",
}

import bpy

class MaterialReplacerPanel(bpy.types.Panel):
    bl_label = "  Material Replacer  "
    bl_idname = "MATERIAL_REPLACER_PT_panel"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'Material Replacer'

    def draw(self, context):
        layout = self.layout
        layout.prop_search(context.scene, "source_material", bpy.data, "materials", text="Old Material")
        layout.prop_search(context.scene, "target_material", bpy.data, "materials", text="New Material")
        layout.operator("material_replacer.replace_material", text="Replace Material")

class ReplaceMaterial(bpy.types.Operator):
    bl_idname = "material_replacer.replace_material"
    bl_label = "Replace Material"
    bl_description = "Replace Material"

    def execute(self, context):
        source_material = context.scene.source_material
        target_material = context.scene.target_material
        
        if source_material and target_material:
            for obj in bpy.data.objects:
                for slot in obj.material_slots:
                    if slot.material == source_material:
                        slot.material = target_material
        else:
            self.report({'INFO'}, "Both source and target materials must be selected")
        return {'FINISHED'}

def register():
    bpy.utils.register_class(MaterialReplacerPanel)
    bpy.utils.register_class(ReplaceMaterial)
    bpy.types.Scene.source_material = bpy.props.PointerProperty(type=bpy.types.Material, description="Material To Be Replaced")
    bpy.types.Scene.target_material = bpy.props.PointerProperty(type=bpy.types.Material, description="New Material")
    ReplaceMaterial.bl_description = "Replace Material"

def unregister():
    bpy.utils.unregister_class(MaterialReplacerPanel)
    bpy.utils.unregister_class(ReplaceMaterial)
    del bpy.types.Scene.source_material
    del bpy.types.Scene.target_material

if __name__ == "__main__":
    register()