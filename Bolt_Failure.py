bl_info = {
    "name": "Bolt Failure",
    "author": "Liu Yang",
    "version": (0, 0, 1),
    "blender": (2, 80, 0),
    "location": "View3D > Sidebar > Edit Tab",
    "description": "Bar Combine",
     "category": "Object",
}
import bpy
import random
from bpy.types import (
    AddonPreferences,
    Operator,
    Panel,
    Menu,
)
from bpy.props import (
    BoolProperty,
    StringProperty,
    EnumProperty,
    IntProperty,
    FloatProperty,
)
path_fatigue=r"F://kit//abschlussarbeit//test//fatigue.blend/Object/"
path_overload = r"F://kit//abschlussarbeit//test//overload.blend/Object/"
path_corrosion = r"F:\\kit\\abschlussarbeit\\fotos\\Corrosion.jpg"
class BoltFailure(bpy.types.Panel):
    bl_label = "Bolt Failure"
    bl_idname = "Bolt Failure"
    bl_space_type = "VIEW_3D"
    bl_region_type = 'UI'
    bl_category = "BoltFailure"

    def draw(self, context):
        layout = self.layout
        layout.operator(Corrosion.bl_idname,text='Corrosion')
        layout.operator(Break.bl_idname,text='Break')
        layout.operator(Headfail.bl_idname,text = 'Headfail')
        layout.operator(Fail_random_m3.bl_idname,text = 'Random_M3')
        layout.operator(Fail_random_m6.bl_idname,text = 'Random_M6')
        layout.operator(Fail_random_m3_noBreak.bl_idname,text = 'Random_M3_noBreak')
        layout.operator(Fail_random_m6_noBreak.bl_idname,text = 'Random_M6_noBreak')
        





class Break(Operator):
    bl_label = "Break"
    bl_idname = "fail.bre"
    bl_options = {'REGISTER', 'UNDO'}
    bf_Break_List = [('None','None','None'),
                     ('bf_Break_Overload','Over Load','Over Load'),
                     ('bf_Break_Fatigue','Fatigue','Fatigue Failure'),
                     ('bf_Break_Hydrogen','Hydrogen','Hydrogen Brittleness')]
    bf_Break_Type:EnumProperty(
            attr='bf_Break_Type',
            name='Break Type',
            description='Choose the type of break',
            items=bf_Break_List,default='None'
            )
    Bolt_List = [('None', 'None', 'None'),
                       ('M3', 'M3', 'M3'),
                       ('M6', 'M6', 'M6')]
    Bolt_Type: EnumProperty(
            attr='bolt_Type',
            name='Bolt Type',
            description='Choose the bolt type you would like',
            items=Bolt_List, default='None'
            )  
    Shank_Length: FloatProperty(
            attr='Shank_Length',
            name='Shank Length', default=0,
            min=0, soft_min=0, max=50,
            description='Length of the unthreaded shank',
            unit='LENGTH',
            )   
  
    def invoke(self, context, event):
        wm = context.window_manager
        return wm.invoke_props_dialog(self)
    
    
    def draw(self, context):
        layout = self.layout
        layout.prop(self,'Bolt_Type')
        layout.prop(self,'Shank_Length')
        layout.prop(self,'bf_Break_Type')
    def bf_fatigue_m3(self):
            length = self.Shank_Length
            coe = 0.8*length+3.2
            obj_above = bpy.context.active_object
            x=obj_above.location[0]
            y=obj_above.location[1]
            z=obj_above.location[2]
            bpy.ops.object.duplicate_move(OBJECT_OT_duplicate={"linked":False, "mode":'TRANSLATION'}, TRANSFORM_OT_translate={"value":(0, 0, 0), "orient_type":'GLOBAL', "orient_matrix":((0, 0, 0), (0, 0, 0), (0, 0, 0)), "orient_matrix_type":'GLOBAL', "constraint_axis":(False, False, False), "mirror":False, "use_proportional_edit":False, "proportional_edit_falloff":'SMOOTH', "proportional_size":1, "use_proportional_connected":False, "use_proportional_projected":False, "snap":False, "snap_target":'CLOSEST', "snap_point":(0, 0, 0), "snap_align":False, "snap_normal":(0, 0, 0), "gpencil_strokes":False, "cursor_transform":False, "texture_space":False, "remove_on_cancel":False, "release_confirm":False, "use_accurate":False, "use_automerge_and_split":False})
            obj_low = bpy.context.active_object
            obj_low.location[0]=x
            obj_low.location[1]=y
            obj_low.location[2]=z
            bpy.ops.object.select_all(action='DESELECT')
            bpy.ops.object.mode_set(mode='EDIT')
            bpy.ops.mesh.select_all(action='SELECT')
            bpy.ops.mesh.bisect(plane_co=(x-0.479469, y-3.81415, z+4.26963+length-coe), plane_no=(0.0101329, -0.0831298, 0.996487), use_fill=False, clear_outer=True, xstart=623, xend=922, ystart=401, yend=429)
            bpy.ops.object.mode_set(mode='OBJECT')
            bpy.context.view_layer.objects.active = obj_above
            bpy.ops.object.mode_set(mode='EDIT')
            bpy.ops.mesh.select_all(action='SELECT')
            bpy.ops.mesh.bisect(plane_co=(x-0.479469, y-3.81415, z+4.26963+length-coe), plane_no=(0.0101329, -0.0831298, 0.996487), use_fill=False, clear_inner=True, xstart=623, xend=922, ystart=401, yend=429)
            bpy.ops.object.mode_set(mode='OBJECT')
            bpy.ops.wm.append(filepath="fatigue.blender", 
            directory=path_fatigue,
            filename="fatigue_m3")
            surface = bpy.context.selected_objects
            surface[0].location[0] = x
            surface[0].location[1] = y
            surface[0].location[2] = z+0.2*(length-6)
            bpy.ops.object.duplicate_move(OBJECT_OT_duplicate={"linked":False, "mode":'TRANSLATION'}, TRANSFORM_OT_translate={"value":(0, 0, 0), "orient_type":'GLOBAL', "orient_matrix":((0, 0, 0), (0, 0, 0), (0, 0, 0)), "orient_matrix_type":'GLOBAL', "constraint_axis":(False, False, False), "mirror":False, "use_proportional_edit":False, "proportional_edit_falloff":'SMOOTH', "proportional_size":1, "use_proportional_connected":False, "use_proportional_projected":False, "snap":False, "snap_target":'CLOSEST', "snap_point":(0, 0, 0), "snap_align":False, "snap_normal":(0, 0, 0), "gpencil_strokes":False, "cursor_transform":False, "texture_space":False, "remove_on_cancel":False, "release_confirm":False, "use_accurate":False, "use_automerge_and_split":False})
            bpy.data.objects[obj_above.name].select_set(True)
            bpy.ops.object.join()
            bpy.ops.object.select_all(action='DESELECT')
            bpy.context.view_layer.objects.active = obj_low
            bpy.data.objects[obj_low.name].select_set(True)
            bpy.data.objects[surface[0].name].select_set(True)
            bpy.ops.object.join()
    def bf_Hydrogen_m3(self):
            length = self.Shank_Length
            obj_above = bpy.context.active_object
            x=obj_above.location[0]
            y=obj_above.location[1]
            z=obj_above.location[2]
            bpy.ops.object.duplicate_move(OBJECT_OT_duplicate={"linked":False, "mode":'TRANSLATION'}, TRANSFORM_OT_translate={"value":(0, 0, 0), "orient_type":'GLOBAL', "orient_matrix":((0, 0, 0), (0, 0, 0), (0, 0, 0)), "orient_matrix_type":'GLOBAL', "constraint_axis":(False, False, False), "mirror":False, "use_proportional_edit":False, "proportional_edit_falloff":'SMOOTH', "proportional_size":1, "use_proportional_connected":False, "use_proportional_projected":False, "snap":False, "snap_target":'CLOSEST', "snap_point":(0, 0, 0), "snap_align":False, "snap_normal":(0, 0, 0), "gpencil_strokes":False, "cursor_transform":False, "texture_space":False, "remove_on_cancel":False, "release_confirm":False, "use_accurate":False, "use_automerge_and_split":False})
            obj_low = bpy.context.active_object
            obj_low.location[0]=x
            obj_low.location[1]=y
            obj_low.location[2]=z
            bpy.ops.object.select_all(action='DESELECT')
            bpy.ops.object.mode_set(mode='EDIT')
            bpy.ops.mesh.select_all(action='SELECT')
            bpy.ops.mesh.bisect(plane_co=(x-0.479469, y-3.81415, z+4.26963+length-6), plane_no=(0.0101329, -0.0831298, 0.996487), use_fill=True, clear_outer=True, xstart=623, xend=922, ystart=401, yend=429)
            bpy.ops.object.mode_set(mode='OBJECT')
            bpy.context.view_layer.objects.active = obj_above
            bpy.ops.object.mode_set(mode='EDIT')
            bpy.ops.mesh.select_all(action='SELECT')
            bpy.ops.mesh.bisect(plane_co=(x-0.479469, y-3.81415, z+4.26963+length-6), plane_no=(0.0101329, -0.0831298, 0.996487), use_fill=True, clear_inner=True, xstart=623, xend=922, ystart=401, yend=429)
            bpy.ops.object.mode_set(mode='OBJECT')  
    def bf_Hydrogen_m6(self):
            length = self.Shank_Length
            obj_above = bpy.context.active_object
            x=obj_above.location[0]
            y=obj_above.location[1]
            z=obj_above.location[2]
            bpy.ops.object.duplicate_move(OBJECT_OT_duplicate={"linked":False, "mode":'TRANSLATION'}, TRANSFORM_OT_translate={"value":(0, 0, 0), "orient_type":'GLOBAL', "orient_matrix":((0, 0, 0), (0, 0, 0), (0, 0, 0)), "orient_matrix_type":'GLOBAL', "constraint_axis":(False, False, False), "mirror":False, "use_proportional_edit":False, "proportional_edit_falloff":'SMOOTH', "proportional_size":1, "use_proportional_connected":False, "use_proportional_projected":False, "snap":False, "snap_target":'CLOSEST', "snap_point":(0, 0, 0), "snap_align":False, "snap_normal":(0, 0, 0), "gpencil_strokes":False, "cursor_transform":False, "texture_space":False, "remove_on_cancel":False, "release_confirm":False, "use_accurate":False, "use_automerge_and_split":False})
            obj_low = bpy.context.active_object
            obj_low.location[0]=x
            obj_low.location[1]=y
            obj_low.location[2]=z
            bpy.ops.object.select_all(action='DESELECT')
            bpy.ops.object.mode_set(mode='EDIT')
            bpy.ops.mesh.select_all(action='SELECT')
            bpy.ops.mesh.bisect(plane_co=(x-0.479469, y-3.81415, z+4.26963+length-8), plane_no=(0.0101329, -0.0831298, 0.996487), use_fill=True, clear_outer=True, xstart=623, xend=922, ystart=401, yend=429)
            bpy.ops.object.mode_set(mode='OBJECT')
            bpy.context.view_layer.objects.active = obj_above
            bpy.ops.object.mode_set(mode='EDIT')
            bpy.ops.mesh.select_all(action='SELECT')
            bpy.ops.mesh.bisect(plane_co=(x-0.479469, y-3.81415, z+4.26963+length-8), plane_no=(0.0101329, -0.0831298, 0.996487), use_fill=True, clear_inner=True, xstart=623, xend=922, ystart=401, yend=429)
            bpy.ops.object.mode_set(mode='OBJECT') 
    def bf_fatigue_m6(self):
            length = self.Shank_Length
            coe = 0.8*length+6
            obj_above = bpy.context.active_object
            x=obj_above.location[0]
            y=obj_above.location[1]
            z=obj_above.location[2]
            bpy.ops.object.duplicate_move(OBJECT_OT_duplicate={"linked":False, "mode":'TRANSLATION'}, TRANSFORM_OT_translate={"value":(0, 0, 0), "orient_type":'GLOBAL', "orient_matrix":((0, 0, 0), (0, 0, 0), (0, 0, 0)), "orient_matrix_type":'GLOBAL', "constraint_axis":(False, False, False), "mirror":False, "use_proportional_edit":False, "proportional_edit_falloff":'SMOOTH', "proportional_size":1, "use_proportional_connected":False, "use_proportional_projected":False, "snap":False, "snap_target":'CLOSEST', "snap_point":(0, 0, 0), "snap_align":False, "snap_normal":(0, 0, 0), "gpencil_strokes":False, "cursor_transform":False, "texture_space":False, "remove_on_cancel":False, "release_confirm":False, "use_accurate":False, "use_automerge_and_split":False})
            obj_low = bpy.context.active_object
            obj_low.location[0]=x
            obj_low.location[1]=y
            obj_low.location[2]=z
            bpy.ops.object.select_all(action='DESELECT')
            bpy.ops.object.mode_set(mode='EDIT')
            bpy.ops.mesh.select_all(action='SELECT')
            bpy.ops.mesh.bisect(plane_co=(x-0.479469, y-3.81415, z+4.26963+length-coe), plane_no=(0.0101329, -0.0831298, 0.996487), use_fill=False, clear_outer=True, xstart=623, xend=922, ystart=401, yend=429)
            bpy.ops.object.mode_set(mode='OBJECT')
            bpy.context.view_layer.objects.active = obj_above
            bpy.ops.object.mode_set(mode='EDIT')
            bpy.ops.mesh.select_all(action='SELECT')
            bpy.ops.mesh.bisect(plane_co=(x-0.479469, y-3.81415, z+4.26963+length-coe), plane_no=(0.0101329, -0.0831298, 0.996487), use_fill=False, clear_inner=True, xstart=623, xend=922, ystart=401, yend=429)
            bpy.ops.object.mode_set(mode='OBJECT')
            bpy.ops.wm.append(filepath="fatigue.blender", 
            directory=path_fatigue,
            filename="fatigue_m6")
            surface = bpy.context.selected_objects
            surface[0].location[0] = x
            surface[0].location[1] = y
            surface[0].location[2] = z+0.2*(length-20)
            bpy.ops.object.duplicate_move(OBJECT_OT_duplicate={"linked":False, "mode":'TRANSLATION'}, TRANSFORM_OT_translate={"value":(0, 0, 0), "orient_type":'GLOBAL', "orient_matrix":((0, 0, 0), (0, 0, 0), (0, 0, 0)), "orient_matrix_type":'GLOBAL', "constraint_axis":(False, False, False), "mirror":False, "use_proportional_edit":False, "proportional_edit_falloff":'SMOOTH', "proportional_size":1, "use_proportional_connected":False, "use_proportional_projected":False, "snap":False, "snap_target":'CLOSEST', "snap_point":(0, 0, 0), "snap_align":False, "snap_normal":(0, 0, 0), "gpencil_strokes":False, "cursor_transform":False, "texture_space":False, "remove_on_cancel":False, "release_confirm":False, "use_accurate":False, "use_automerge_and_split":False})
            bpy.data.objects[obj_above.name].select_set(True)
            bpy.ops.object.join()
            bpy.ops.object.select_all(action='DESELECT')
            bpy.context.view_layer.objects.active = obj_low
            bpy.data.objects[obj_low.name].select_set(True)
            bpy.data.objects[surface[0].name].select_set(True)
            bpy.ops.object.join()    
    def execute(self, context):
        if self.Bolt_Type == 'M3':
            if self.bf_Break_Type == 'bf_Break_Fatigue':
                self.bf_fatigue_m3()
            if self.bf_Break_Type == 'bf_Break_Hydrogen':
                self.bf_Hydrogen_m3()
        if self.Bolt_Type == 'M6':
            if self.bf_Break_Type == 'bf_Break_Hydrogen':
                self.bf_Hydrogen_m6()
            if self.bf_Break_Type == 'bf_Break_Fatigue':
                self.bf_fatigue_m6()
        return {'FINISHED'}


class Corrosion(Operator):
    bl_label = "Corrosion"
    bl_idname = "fail.corro"
    bl_options = {'REGISTER', 'UNDO'}
    bf_Corrosion_Percent:IntProperty(
            attr='bf_Corrosion_Percent',
            name='Corrosion Percent', default=0,
            min=0, soft_min=1,
            max=100,
            description='Percent of the corrosion',
            )
    
    
    
    
    
    def invoke(self, context, event):
        wm = context.window_manager
        return wm.invoke_props_dialog(self)
    
    
    def draw(self, context):
        layout = self.layout
        layout.prop(self,'bf_Corrosion_Percent')
    def rustbin(self):
        BoltCorrosion=bpy.data.materials.new(name='Corrosion')
        BoltCorrosion.use_nodes=True
        bpy.context.object.active_material = BoltCorrosion
        principled1_node = BoltCorrosion.node_tree.nodes.get('Principled BSDF')
        Output_node = BoltCorrosion.node_tree.nodes.get('Material Output')
        principled1_node.location = (-234,460)
        principled1_node.inputs[0].default_value = (1,1,1,1)
        principled1_node.inputs[3].default_value = (1,1,1,1)
        principled1_node.inputs[4].default_value = 1
        principled1_node.inputs[5].default_value = 0.5
        principled1_node.inputs[7].default_value = 0.616
        Mix_node = BoltCorrosion.node_tree.nodes.new('ShaderNodeMixShader')
        Mix_node.location = (90,100)
        principled2_node = BoltCorrosion.node_tree.nodes.new('ShaderNodeBsdfPrincipled')
        principled2_node.location=(-234,-200)
        principled2_node.inputs[3].default_value = (1,1,1,1)
        principled2_node.inputs[4].default_value = 1
        principled2_node.inputs[5].default_value = 0.5
        principled2_node.inputs[7].default_value = 0.774
        Bump_node = BoltCorrosion.node_tree.nodes.new('ShaderNodeBump')
        Bump_node.location = (-450,0)
        Bump_node.invert = True
        Bump_node.inputs[1].default_value = 1.4
        Bump_node.inputs[0].default_value = 0
        ColorRamp1_node = BoltCorrosion.node_tree.nodes.new('ShaderNodeValToRGB')
        ColorRamp1_node.location = (-600,460)
        ColorRamp1_node.color_ramp.elements[1].position = 0.723
        ColorRamp1_node.color_ramp.elements[0].position = 0.805
        Voronoi_node = BoltCorrosion.node_tree.nodes.new('ShaderNodeTexVoronoi')
        Voronoi_node.location = (-700,0)
        Voronoi_node.inputs[2].default_value = 2
        ColorRamp2_node = BoltCorrosion.node_tree.nodes.new('ShaderNodeValToRGB')
        ColorRamp2_node.location = (-1100,0)
        ColorRamp2_node.color_ramp.elements[1].position = 0.909
        Noise_node = BoltCorrosion.node_tree.nodes.new('ShaderNodeTexNoise')
        Noise_node.location = (-1300,0)
        Noise_node.inputs[2].default_value = 0.5
        Noise_node.inputs[3].default_value = 16
        Noise_node.inputs[4].default_value = 0.833
        Mapping_node = BoltCorrosion.node_tree.nodes.new('ShaderNodeMapping')
        Mapping_node.location = (-1500,0)
        TexCoord_node = BoltCorrosion.node_tree.nodes.new('ShaderNodeTexCoord')
        TexCoord_node.location = (-1700,0)
        Img_node = BoltCorrosion.node_tree.nodes.new('ShaderNodeTexImage')
        Img_node.location = (-700,-500)
        Image = bpy.data.images.load (path_corrosion)
        Img_node.image = Image
        link = BoltCorrosion.node_tree.links.new
        link(Mix_node.outputs[0],Output_node.inputs[0])
        link(ColorRamp1_node.outputs[0],Mix_node.inputs[0])
        link(principled1_node.outputs[0],Mix_node.inputs[1])
        link(principled2_node.outputs[0],Mix_node.inputs[2])
        link(principled1_node.inputs[19],Bump_node.outputs[0])
        link(principled2_node.inputs[19],Bump_node.outputs[0])
        link(ColorRamp1_node.outputs[1],Bump_node.inputs[2])
        link(ColorRamp1_node.inputs[0],Voronoi_node.outputs[1])
        link(ColorRamp2_node.outputs[0],Voronoi_node.inputs[0])
        link(ColorRamp2_node.inputs[0],Noise_node.outputs[1])
        link(Mapping_node.outputs[0],Noise_node.inputs[0])
        link(Mapping_node.inputs[0],TexCoord_node.outputs[3])
        link(principled2_node.inputs[0],Img_node.outputs[0])
        if self.bf_Corrosion_Percent == 0:
            bpy.context.object.active_material.use_nodes = False
        elif self.bf_Corrosion_Percent < 50:
            ColorRamp2_node.color_ramp.elements[0].position =self.bf_Corrosion_Percent/263
        elif self.bf_Corrosion_Percent >=50 and self.bf_Corrosion_Percent <=95:
            ColorRamp2_node.color_ramp.elements[0].position =self.bf_Corrosion_Percent/350
        else :
            ColorRamp2_node.color_ramp.elements[0].position =self.bf_Corrosion_Percent/290        
    def execute(self, context):
        self.rustbin()
        return {'FINISHED'}
class Headfail(bpy.types.Operator):
    bl_label = "Head Fail"
    bl_idname = "fail.head"
    bl_options = {'REGISTER', 'UNDO'}
    bf_Bit_List = [('None','None','None'),
                     ('bf_Allen','Allen','Allen'),
                     ('bf_Torx','Torx','Torx'),
                     ('bf_Phillips','Phillips','Phillips')]
    bf_Bit_Type:EnumProperty(
            attr='bf_Bit_Type',
            name='Bit Type',
            description='Choose the type of bit',
            items=bf_Bit_List,default='None'
            )
    Bolt_List = [('None', 'None', 'None'),
                       ('M3', 'M3', 'M3'),
                       ('M6', 'M6', 'M6')]
    Bolt_Type: EnumProperty(
            attr='bolt_Type',
            name='Bolt Type',
            description='Choose the bolt type you would like',
            items=Bolt_List, default='None'
            )  
    Shank_Length: FloatProperty(
            attr='Shank_Length',
            name='Shank Length', default=0,
            min=0, soft_min=0, max=50,
            description='Length of the unthreaded shank',
            unit='LENGTH',
            )      
    Hf_radius: FloatProperty(
            attr='Hf_radius',
            name='Headfailure radius', default=0,
            min=0, soft_min=0, max=4,
            description='Radius of the headfailure',
            unit='LENGTH',
            )        
    
    
    
    def invoke(self, context, event):
        wm = context.window_manager
        return wm.invoke_props_dialog(self)
    
    
    def draw(self, context):
        layout = self.layout
        layout.prop(self,'Bolt_Type')
        layout.prop(self,'bf_Bit_Type')
        layout.prop(self,'Shank_Length')
        layout.prop(self,'Hf_radius')       
    def hf_Torx_m3(self):
        high = self.Shank_Length
        r = self.Hf_radius
        obj_bolt = bpy.context.active_object
        x = obj_bolt.location[0]
        y = obj_bolt.location[1]
        z = obj_bolt.location[2]
        bpy.ops.mesh.primitive_cone_add(radius1=1, radius2=r, depth=1.5, enter_editmode=False, align='WORLD', location=(0, 0, 0), scale=(1, 1, 1))
        obj_cone = bpy.context.active_object
        obj_cone.location[0] = x
        obj_cone.location[1] = y
        obj_cone.location[2] = z+7+high-6     
        bpy.context.view_layer.objects.active = obj_bolt
        bpy.data.objects[obj_bolt.name].select_set(True)
        bpy.ops.object.booltool_auto_difference()
        bpy.ops.mesh.primitive_cylinder_add(radius=1.5, depth=1, enter_editmode=False, align='WORLD', location=(0, 0, 0), scale=(1, 1, 1))
        obj_cyl = bpy.context.active_object
        obj_cyl.location[0] = x
        obj_cyl.location[1] = y
        obj_cyl.location[2] = z+6.2+high-6
        bpy.context.view_layer.objects.active = obj_bolt
        bpy.data.objects[obj_bolt.name].select_set(True)
        bpy.ops.object.booltool_auto_difference()
    def hf_Allen_m3(self):
        high = self.Shank_Length
        r = self.Hf_radius
        obj_bolt = bpy.context.active_object
        x = obj_bolt.location[0]
        y = obj_bolt.location[1]
        z = obj_bolt.location[2]
        bpy.ops.mesh.primitive_cone_add(radius1=1, radius2=r, depth=1.5, enter_editmode=False, align='WORLD', location=(0, 0, 0), scale=(1, 1, 1))
        obj_cone = bpy.context.active_object
        obj_cone.location[0] = x
        obj_cone.location[1] = y
        obj_cone.location[2] = z+6.8+high-6
        bpy.context.view_layer.objects.active = obj_bolt
        bpy.data.objects[obj_bolt.name].select_set(True)
        bpy.ops.object.booltool_auto_difference()
        bpy.ops.mesh.primitive_cylinder_add(radius=1.5, depth=1, enter_editmode=False, align='WORLD', location=(0, 0, 0), scale=(1, 1, 1))
        obj_cyl = bpy.context.active_object
        obj_cyl.location[0] = x
        obj_cyl.location[1] = y
        obj_cyl.location[2] = z+6.2+high-6
        bpy.context.view_layer.objects.active = obj_bolt
        bpy.data.objects[obj_bolt.name].select_set(True)
        bpy.ops.object.booltool_auto_difference()
    def hf_Phillips_m3(self):
        high = self.Shank_Length
        r = self.Hf_radius
        obj_bolt = bpy.context.active_object
        x = obj_bolt.location[0]
        y = obj_bolt.location[1]
        z = obj_bolt.location[2]
        bpy.ops.mesh.primitive_cone_add(radius1=0.3, radius2=r, depth=2, enter_editmode=False, align='WORLD', location=(0, 0, 0), scale=(1, 1, 1))
        obj = bpy.context.active_object
        obj.location[0] =x
        obj.location[1] =y
        obj.location[2] =z+7+high - 6
        bpy.context.view_layer.objects.active = obj_bolt
        bpy.data.objects[obj_bolt.name].select_set(True)
        bpy.ops.object.booltool_auto_difference()
    def hf_Allen_m6(self):
        high = self.Shank_Length
        r = self.Hf_radius
        obj_bolt = bpy.context.active_object
        x = obj_bolt.location[0]
        y = obj_bolt.location[1]
        z = obj_bolt.location[2]
        bpy.ops.mesh.primitive_cone_add(radius1=2, radius2=r, depth=3, enter_editmode=False, align='WORLD', location=(0, 0, 0), scale=(1, 1, 1))
        obj_cone = bpy.context.active_object
        obj_cone.location[0] = x
        obj_cone.location[1] = y
        obj_cone.location[2] = z+21+high-20     
        bpy.context.view_layer.objects.active = obj_bolt
        bpy.data.objects[obj_bolt.name].select_set(True)
        bpy.ops.object.booltool_auto_difference()
        bpy.ops.mesh.primitive_cylinder_add(radius=3, depth=2, enter_editmode=False, align='WORLD', location=(0, 0, 0), scale=(1, 1, 1))
        obj_cyl = bpy.context.active_object
        obj_cyl.location[0] = x
        obj_cyl.location[1] = y
        obj_cyl.location[2] = z+20.001+high-20
        bpy.context.view_layer.objects.active = obj_bolt
        bpy.data.objects[obj_bolt.name].select_set(True)
        bpy.ops.object.booltool_auto_difference()     
    def hf_Torx_m6(self):
        high = self.Shank_Length
        r = self.Hf_radius
        obj_bolt = bpy.context.active_object
        x = obj_bolt.location[0]
        y = obj_bolt.location[1]
        z = obj_bolt.location[2]
        bpy.ops.mesh.primitive_cone_add(radius1=2, radius2=r, depth=3, enter_editmode=False, align='WORLD', location=(0, 0, 0), scale=(1, 1, 1))
        obj_cone = bpy.context.active_object
        obj_cone.location[0] = x
        obj_cone.location[1] = y
        obj_cone.location[2] = z+22+high-20     
        bpy.context.view_layer.objects.active = obj_bolt
        bpy.data.objects[obj_bolt.name].select_set(True)
        bpy.ops.object.booltool_auto_difference()
        bpy.ops.mesh.primitive_cylinder_add(radius=2.9, depth=2, enter_editmode=False, align='WORLD', location=(0, 0, 0), scale=(1, 1, 1))
        obj_cyl = bpy.context.active_object
        obj_cyl.location[0] = x
        obj_cyl.location[1] = y
        obj_cyl.location[2] = z+20.001+high-20
        bpy.context.view_layer.objects.active = obj_bolt
        bpy.data.objects[obj_bolt.name].select_set(True)
        bpy.ops.object.booltool_auto_difference()
    def hf_Phillips_m6(self):
        high = self.Shank_Length
        r = self.Hf_radius
        obj_bolt = bpy.context.active_object
        x = obj_bolt.location[0]
        y = obj_bolt.location[1]
        z = obj_bolt.location[2]
        bpy.ops.mesh.primitive_cone_add(radius1=0.6, radius2=r, depth=4, enter_editmode=False, align='WORLD', location=(0, 0, 0), scale=(1, 1, 1))
        obj = bpy.context.active_object
        obj.location[0] =x
        obj.location[1] =y
        obj.location[2] =z+21+high - 20
        bpy.context.view_layer.objects.active = obj_bolt
        bpy.data.objects[obj_bolt.name].select_set(True)
        bpy.ops.object.booltool_auto_difference()
    def execute(self, context):
        if self.Bolt_Type == 'M3':
            if self.bf_Bit_Type == 'bf_Torx':
                self.hf_Torx_m3()      
            if self.bf_Bit_Type == 'bf_Allen':
                self.hf_Allen_m3()
            if self.bf_Bit_Type == 'bf_Phillips':
                self.hf_Phillips_m3()
        elif self.Bolt_Type == 'M6':
            if self.bf_Bit_Type == 'bf_Allen':
                self.hf_Allen_m6()
            if self.bf_Bit_Type == 'bf_Torx':
                self.hf_Torx_m6()
            if self.bf_Bit_Type == 'bf_Phillips':
                self.hf_Phillips_m6()
        return {'FINISHED'}    
class Fail_random_m3(bpy.types.Operator):
    bl_label = "Failure random_m3"
    bl_idname = "fail.random_m3"
    bl_options = {'REGISTER', 'UNDO'}
    
    
    
    
    def draw(self, context):
        layout = self.layout
        
    def get_failure(self):
        a=[1,2,3]
        k = random.randint(1,3)
        n = random.sample(a,k)
        return n
    def get_bolt(self):
        i = random.randint(1,3)
        if i == 1:
            bpy.ops.mesh.bolt_add(align='WORLD', location=(0, 0, 0), rotation=(0, 0, 0), change=False, bf_Model_Type='bf_Model_Bolt', bf_Head_Type='bf_Head_Hex', bf_Bit_Type='bf_Bit_Allen', bf_Nut_Type='bf_Nut_Hex', bf_Shank_Length=0, bf_Shank_Dia=3, bf_Phillips_Bit_Depth=1.14315, bf_Allen_Bit_Depth=1.5, bf_Allen_Bit_Flat_Distance=2.5, bf_Torx_Size_Type='bf_Torx_T10', bf_Torx_Bit_Depth=1.5, bf_Hex_Head_Height=2, bf_Hex_Head_Flat_Distance=5.5, bf_12_Point_Head_Height=3, bf_12_Point_Head_Flat_Distance=3, bf_12_Point_Head_Flange_Dia=5.72, bf_CounterSink_Head_Dia=6.3, bf_Cap_Head_Height=3, bf_Cap_Head_Dia=5.5, bf_Dome_Head_Dia=5.6, bf_Pan_Head_Dia=5.6, bf_Philips_Bit_Dia=1.82, bf_Thread_Length=20, bf_Major_Dia=3, bf_Pitch=0.35, bf_Minor_Dia=2.62111, bf_Crest_Percent=10, bf_Root_Percent=10, bf_Div_Count=36, bf_Hex_Nut_Height=2.4, bf_Hex_Nut_Flat_Distance=5.5, bf_12_Point_Nut_Height=3, bf_12_Point_Nut_Flat_Distance=3, bf_12_Point_Nut_Flange_Dia=5.72)
        if i == 2:
            bpy.ops.mesh.bolt_add(align='WORLD', location=(0, 0, 0), rotation=(0, 0, 0), change=False, bf_Model_Type='bf_Model_Bolt', bf_Head_Type='bf_Head_Hex', bf_Bit_Type='bf_Bit_Torx', bf_Nut_Type='bf_Nut_Hex', bf_Shank_Length=0, bf_Shank_Dia=3, bf_Phillips_Bit_Depth=1.14315, bf_Allen_Bit_Depth=1.5, bf_Allen_Bit_Flat_Distance=2.5, bf_Torx_Size_Type='bf_Torx_T10', bf_Torx_Bit_Depth=1.5, bf_Hex_Head_Height=2, bf_Hex_Head_Flat_Distance=5.5, bf_12_Point_Head_Height=3, bf_12_Point_Head_Flat_Distance=3, bf_12_Point_Head_Flange_Dia=5.72, bf_CounterSink_Head_Dia=6.3, bf_Cap_Head_Height=3, bf_Cap_Head_Dia=5.5, bf_Dome_Head_Dia=5.6, bf_Pan_Head_Dia=5.6, bf_Philips_Bit_Dia=1.82, bf_Thread_Length=20, bf_Major_Dia=3, bf_Pitch=0.35, bf_Minor_Dia=2.62111, bf_Crest_Percent=10, bf_Root_Percent=10, bf_Div_Count=36, bf_Hex_Nut_Height=2.4, bf_Hex_Nut_Flat_Distance=5.5, bf_12_Point_Nut_Height=3, bf_12_Point_Nut_Flat_Distance=3, bf_12_Point_Nut_Flange_Dia=5.72)
        if i == 3:
            bpy.ops.mesh.bolt_add(align='WORLD', location=(0, 0, 0), rotation=(0, 0, 0), change=False, bf_Model_Type='bf_Model_Bolt', bf_Head_Type='bf_Head_Hex', bf_Bit_Type='bf_Bit_Philips', bf_Nut_Type='bf_Nut_Hex', bf_Shank_Length=0, bf_Shank_Dia=3, bf_Phillips_Bit_Depth=1.14315, bf_Allen_Bit_Depth=1.5, bf_Allen_Bit_Flat_Distance=2.5, bf_Torx_Size_Type='bf_Torx_T10', bf_Torx_Bit_Depth=1.5, bf_Hex_Head_Height=2, bf_Hex_Head_Flat_Distance=5.5, bf_12_Point_Head_Height=3, bf_12_Point_Head_Flat_Distance=3, bf_12_Point_Head_Flange_Dia=5.72, bf_CounterSink_Head_Dia=6.3, bf_Cap_Head_Height=3, bf_Cap_Head_Dia=5.5, bf_Dome_Head_Dia=5.6, bf_Pan_Head_Dia=5.6, bf_Philips_Bit_Dia=1.82, bf_Thread_Length=20, bf_Major_Dia=3, bf_Pitch=0.35, bf_Minor_Dia=2.62111, bf_Crest_Percent=10, bf_Root_Percent=10, bf_Div_Count=36, bf_Hex_Nut_Height=2.4, bf_Hex_Nut_Flat_Distance=5.5, bf_12_Point_Nut_Height=3, bf_12_Point_Nut_Flat_Distance=3, bf_12_Point_Nut_Flange_Dia=5.72)
        return i
    def execute(self, context):
        overload = random.randint(1,63)
        n = self.get_failure()
        n.sort()
        r_m3_allen = random.uniform(1.4,1.7)
        r_m3_torx = random.uniform(1.3,1.6)
        r_m3_phillips = random.uniform(0.8,1.2)
        if overload <= 4 :
            bpy.ops.wm.append(filepath="overload.blender", 
            directory=path_overload,
            filename="Overload_m3_allen")
            bolt = bpy.context.selected_objects[0]
            bpy.context.view_layer.objects.active = bolt
            for x in n :
                if x == 1:
                    percent = random.randint(1,100)
                    bpy.ops.fail.corro(bf_Corrosion_Percent=percent)
                if x == 2:
                    bpy.ops.fail.head(bf_Bit_Type='bf_Allen',Bolt_Type='M3', Shank_Length=20,Hf_radius = r_m3_allen)
                if x == 3:
                    pass
        elif overload >4 and overload <= 8:
            bpy.ops.wm.append(filepath="overload.blender", 
            directory=path_overload,
            filename="Overload_m3_torx")
            bolt = bpy.context.selected_objects[0]
            bpy.context.view_layer.objects.active = bolt
            for x in n :
                if x == 1:
                    percent = random.randint(1,100)
                    bpy.ops.fail.corro(bf_Corrosion_Percent=percent)
                if x == 2:
                    bpy.ops.fail.head(bf_Bit_Type='bf_Torx', Bolt_Type='M3',Shank_Length=20,Hf_radius = r_m3_torx)
                if x == 3:
                    pass
        elif overload >8 and overload <= 12:
            bpy.ops.wm.append(filepath="overload.blender", 
            directory=path_overload,
            filename="Overload_m3_phillips")
            bolt = bpy.context.selected_objects[0]
            bpy.context.view_layer.objects.active = bolt
            for x in n :
                if x == 1:
                    percent = random.randint(1,100)
                    bpy.ops.fail.corro(bf_Corrosion_Percent=percent)
                if x == 2:
                    bpy.ops.fail.head(bf_Bit_Type='bf_Phillips', Bolt_Type='M3', Shank_Length=20,Hf_radius = r_m3_phillips)
                if x == 3:
                    pass
        else:
            i = self.get_bolt()
            for x in n :
                if x == 1:
                    percent = random.randint(1,100)
                    bpy.ops.fail.corro(bf_Corrosion_Percent=percent)
                if x == 3:
                    breaktype = random.randint(1,2)
                    if breaktype == 1:
                        bpy.ops.fail.bre(bf_Break_Type='bf_Break_Fatigue', Bolt_Type='M3', Shank_Length=20)
                    if breaktype == 2:
                        bpy.ops.fail.bre(bf_Break_Type='bf_Break_Hydrogen', Bolt_Type='M3', Shank_Length=20)
                if x == 2:
                    if i == 1 :
                        bpy.ops.fail.head(bf_Bit_Type='bf_Allen', Bolt_Type='M3',Shank_Length=20,Hf_radius = r_m3_allen)
                    if i == 2:
                        bpy.ops.fail.head(bf_Bit_Type='bf_Torx', Bolt_Type='M3',Shank_Length=20,Hf_radius = r_m3_torx)
                    if i == 3:
                        bpy.ops.fail.head(bf_Bit_Type='bf_Phillips',Bolt_Type='M3', Shank_Length=20,Hf_radius = r_m3_phillips)
      
        return {'FINISHED'}
class Fail_random_m6(bpy.types.Operator):
    bl_label = "Failure random_m6"
    bl_idname = "fail.random_m6"
    bl_options = {'REGISTER', 'UNDO'}
    
    
    
    
    def draw(self, context):
        layout = self.layout
        
    def get_failure(self):
        a=[1,2,3]
        k = random.randint(1,3)
        n = random.sample(a,k)
        return n
    def get_bolt(self):
        i = random.randint(1,3)
        if i == 1:
            bpy.ops.mesh.bolt_add(align='WORLD', location=(0, 0, 0), rotation=(0, 0, 0), change=False, bf_Model_Type='bf_Model_Bolt', bf_Head_Type='bf_Head_Hex', bf_Bit_Type='bf_Bit_Allen', bf_Nut_Type='bf_Nut_Hex', bf_Shank_Length=0, bf_Shank_Dia=6, bf_Phillips_Bit_Depth=2.44961, bf_Allen_Bit_Depth=3, bf_Allen_Bit_Flat_Distance=5, bf_Torx_Size_Type='bf_Torx_T30', bf_Torx_Bit_Depth=3, bf_Hex_Head_Height=4, bf_Hex_Head_Flat_Distance=10, bf_12_Point_Head_Height=6, bf_12_Point_Head_Flat_Distance=6, bf_12_Point_Head_Flange_Dia=10.22, bf_CounterSink_Head_Dia=12.6, bf_Cap_Head_Height=6, bf_Cap_Head_Dia=10, bf_Dome_Head_Dia=12, bf_Pan_Head_Dia=12, bf_Philips_Bit_Dia=3.9, bf_Thread_Length=20, bf_Major_Dia=6, bf_Pitch=0.75, bf_Minor_Dia=5.1881, bf_Crest_Percent=10, bf_Root_Percent=10, bf_Div_Count=36, bf_Hex_Nut_Height=5, bf_Hex_Nut_Flat_Distance=10, bf_12_Point_Nut_Height=6, bf_12_Point_Nut_Flat_Distance=6, bf_12_Point_Nut_Flange_Dia=10.22)
        if i == 2:
            bpy.ops.mesh.bolt_add(align='WORLD', location=(0, 0, 0), rotation=(0, 0, 0), change=False, bf_Model_Type='bf_Model_Bolt', bf_Head_Type='bf_Head_Hex', bf_Bit_Type='bf_Bit_Torx', bf_Nut_Type='bf_Nut_Hex', bf_Shank_Length=0, bf_Shank_Dia=6, bf_Phillips_Bit_Depth=2.44961, bf_Allen_Bit_Depth=3, bf_Allen_Bit_Flat_Distance=5, bf_Torx_Size_Type='bf_Torx_T30', bf_Torx_Bit_Depth=3, bf_Hex_Head_Height=4, bf_Hex_Head_Flat_Distance=10, bf_12_Point_Head_Height=6, bf_12_Point_Head_Flat_Distance=6, bf_12_Point_Head_Flange_Dia=10.22, bf_CounterSink_Head_Dia=12.6, bf_Cap_Head_Height=6, bf_Cap_Head_Dia=10, bf_Dome_Head_Dia=12, bf_Pan_Head_Dia=12, bf_Philips_Bit_Dia=3.9, bf_Thread_Length=20, bf_Major_Dia=6, bf_Pitch=0.75, bf_Minor_Dia=5.1881, bf_Crest_Percent=10, bf_Root_Percent=10, bf_Div_Count=36, bf_Hex_Nut_Height=5, bf_Hex_Nut_Flat_Distance=10, bf_12_Point_Nut_Height=6, bf_12_Point_Nut_Flat_Distance=6, bf_12_Point_Nut_Flange_Dia=10.22)
        if i == 3:
            bpy.ops.mesh.bolt_add(align='WORLD', location=(0, 0, 0), rotation=(0, 0, 0), change=False, bf_Model_Type='bf_Model_Bolt', bf_Head_Type='bf_Head_Hex', bf_Bit_Type='bf_Bit_Philips', bf_Nut_Type='bf_Nut_Hex', bf_Shank_Length=0, bf_Shank_Dia=6, bf_Phillips_Bit_Depth=2.44961, bf_Allen_Bit_Depth=3, bf_Allen_Bit_Flat_Distance=5, bf_Torx_Size_Type='bf_Torx_T30', bf_Torx_Bit_Depth=3, bf_Hex_Head_Height=4, bf_Hex_Head_Flat_Distance=10, bf_12_Point_Head_Height=6, bf_12_Point_Head_Flat_Distance=6, bf_12_Point_Head_Flange_Dia=10.22, bf_CounterSink_Head_Dia=12.6, bf_Cap_Head_Height=6, bf_Cap_Head_Dia=10, bf_Dome_Head_Dia=12, bf_Pan_Head_Dia=12, bf_Philips_Bit_Dia=3.9, bf_Thread_Length=20, bf_Major_Dia=6, bf_Pitch=0.75, bf_Minor_Dia=5.1881, bf_Crest_Percent=10, bf_Root_Percent=10, bf_Div_Count=36, bf_Hex_Nut_Height=5, bf_Hex_Nut_Flat_Distance=10, bf_12_Point_Nut_Height=6, bf_12_Point_Nut_Flat_Distance=6, bf_12_Point_Nut_Flange_Dia=10.22)
        return i
    def execute(self, context):
        overload = random.randint(1,63)
        n = self.get_failure()
        n.sort()
        r_m6_allen = random.uniform(2.7,3.1)
        r_m6_torx = random.uniform(2.7,3.3)
        r_m6_phillips = random.uniform(1.8,2.3)
        if overload <= 4 :
            bpy.ops.wm.append(filepath="overload.blender", 
            directory=path_overload,
            filename="Overload_m6_allen")
            bolt = bpy.context.selected_objects[0]
            bpy.context.view_layer.objects.active = bolt
            for x in n :
                if x == 1:
                    percent = random.randint(1,100)
                    bpy.ops.fail.corro(bf_Corrosion_Percent=percent)
                if x == 2:
                    bpy.ops.fail.head(bf_Bit_Type='bf_Allen',Bolt_Type='M6', Shank_Length=20,Hf_radius = r_m6_allen)
                if x == 3:
                    pass
        elif overload >4 and overload <= 8:
            bpy.ops.wm.append(filepath="overload.blender", 
            directory=path_overload,
            filename="Overload_m6_torx")
            bolt = bpy.context.selected_objects[0]
            bpy.context.view_layer.objects.active = bolt
            for x in n :
                if x == 1:
                    percent = random.randint(1,100)
                    bpy.ops.fail.corro(bf_Corrosion_Percent=percent)
                if x == 2:
                    bpy.ops.fail.head(bf_Bit_Type='bf_Torx', Bolt_Type='M6',Shank_Length=20,Hf_radius = r_m6_torx)
                if x == 3:
                    pass
        elif overload >8 and overload <= 12:
            bpy.ops.wm.append(filepath="overload.blender", 
            directory=path_overload,
            filename="Overload_m6_phillips")
            bolt = bpy.context.selected_objects[0]
            bpy.context.view_layer.objects.active = bolt
            for x in n :
                if x == 1:
                    percent = random.randint(1,100)
                    bpy.ops.fail.corro(bf_Corrosion_Percent=percent)
                if x == 2:
                    bpy.ops.fail.head(bf_Bit_Type='bf_Phillips', Bolt_Type='M6', Shank_Length=20,Hf_radius = r_m6_phillips)
                if x == 3:
                    pass
        else:
            i = self.get_bolt()
            for x in n :
                if x == 1:
                    percent = random.randint(1,100)
                    bpy.ops.fail.corro(bf_Corrosion_Percent=percent)
                if x == 3:
                    breaktype = random.randint(1,2)
                    if breaktype == 1:
                        bpy.ops.fail.bre(bf_Break_Type='bf_Break_Fatigue', Bolt_Type='M6', Shank_Length=20)
                    if breaktype == 2:
                        bpy.ops.fail.bre(bf_Break_Type='bf_Break_Hydrogen', Bolt_Type='M6', Shank_Length=20)
                if x == 2:
                    if i == 1 :
                        bpy.ops.fail.head(bf_Bit_Type='bf_Allen', Bolt_Type='M6',Shank_Length=20,Hf_radius = r_m6_allen)
                    if i == 2:
                        bpy.ops.fail.head(bf_Bit_Type='bf_Torx', Bolt_Type='M6',Shank_Length=20,Hf_radius = r_m6_torx)
                    if i == 3:
                        bpy.ops.fail.head(bf_Bit_Type='bf_Phillips',Bolt_Type='M6', Shank_Length=20,Hf_radius = r_m6_phillips)
      
        return {'FINISHED'}
class Fail_random_m3_noBreak(bpy.types.Operator):
    bl_label = "Failure random_m3_noBreak"
    bl_idname = "fail.random_m3nobreak"
    bl_options = {'REGISTER', 'UNDO'}
    
    bf_Bit_List = [('None','None','None'),
                     ('bf_Allen','Allen','Allen'),
                     ('bf_Torx','Torx','Torx'),
                     ('bf_Phillips','Phillips','Phillips')]
    bf_Bit_Type:EnumProperty(
            attr='bf_Bit_Type',
            name='Bit Type',
            description='Choose the type of bit',
            items=bf_Bit_List,default='None'
            )
    bf_Corrosion_Percent:IntProperty(
            attr='bf_Corrosion_Percent',
            name='Corrosion Percent', default=0,
            min=0, soft_min=1,
            max=100,
            description='Percent of the corrosion',
            )
    
    
    def draw(self, context):
        layout = self.layout
        layout.prop(self,'bf_Bit_Type')
        layout.prop(self,'bf_Corrosion_Percent')
    def invoke(self, context, event):
        wm = context.window_manager
        return wm.invoke_props_dialog(self)
    def get_failure(self):
        a=[1,2]
        k = random.randint(1,2)
        n = random.sample(a,k)
        return n
    def get_bolt(self):
        if self.bf_Bit_Type == 'bf_Allen':
            bpy.ops.mesh.bolt_add(align='WORLD', location=(0, 0, 0), rotation=(0, 0, 0), change=False, bf_Model_Type='bf_Model_Bolt', bf_Head_Type='bf_Head_Hex', bf_Bit_Type='bf_Bit_Allen', bf_Nut_Type='bf_Nut_Hex', bf_Shank_Length=0, bf_Shank_Dia=3, bf_Phillips_Bit_Depth=1.14315, bf_Allen_Bit_Depth=1.5, bf_Allen_Bit_Flat_Distance=2.5, bf_Torx_Size_Type='bf_Torx_T10', bf_Torx_Bit_Depth=1.5, bf_Hex_Head_Height=2, bf_Hex_Head_Flat_Distance=5.5, bf_12_Point_Head_Height=3, bf_12_Point_Head_Flat_Distance=3, bf_12_Point_Head_Flange_Dia=5.72, bf_CounterSink_Head_Dia=6.3, bf_Cap_Head_Height=3, bf_Cap_Head_Dia=5.5, bf_Dome_Head_Dia=5.6, bf_Pan_Head_Dia=5.6, bf_Philips_Bit_Dia=1.82, bf_Thread_Length=20, bf_Major_Dia=3, bf_Pitch=0.35, bf_Minor_Dia=2.62111, bf_Crest_Percent=10, bf_Root_Percent=10, bf_Div_Count=36, bf_Hex_Nut_Height=2.4, bf_Hex_Nut_Flat_Distance=5.5, bf_12_Point_Nut_Height=3, bf_12_Point_Nut_Flat_Distance=3, bf_12_Point_Nut_Flange_Dia=5.72)
        if self.bf_Bit_Type == 'bf_Torx':
            bpy.ops.mesh.bolt_add(align='WORLD', location=(0, 0, 0), rotation=(0, 0, 0), change=False, bf_Model_Type='bf_Model_Bolt', bf_Head_Type='bf_Head_Hex', bf_Bit_Type='bf_Bit_Torx', bf_Nut_Type='bf_Nut_Hex', bf_Shank_Length=0, bf_Shank_Dia=3, bf_Phillips_Bit_Depth=1.14315, bf_Allen_Bit_Depth=1.5, bf_Allen_Bit_Flat_Distance=2.5, bf_Torx_Size_Type='bf_Torx_T10', bf_Torx_Bit_Depth=1.5, bf_Hex_Head_Height=2, bf_Hex_Head_Flat_Distance=5.5, bf_12_Point_Head_Height=3, bf_12_Point_Head_Flat_Distance=3, bf_12_Point_Head_Flange_Dia=5.72, bf_CounterSink_Head_Dia=6.3, bf_Cap_Head_Height=3, bf_Cap_Head_Dia=5.5, bf_Dome_Head_Dia=5.6, bf_Pan_Head_Dia=5.6, bf_Philips_Bit_Dia=1.82, bf_Thread_Length=20, bf_Major_Dia=3, bf_Pitch=0.35, bf_Minor_Dia=2.62111, bf_Crest_Percent=10, bf_Root_Percent=10, bf_Div_Count=36, bf_Hex_Nut_Height=2.4, bf_Hex_Nut_Flat_Distance=5.5, bf_12_Point_Nut_Height=3, bf_12_Point_Nut_Flat_Distance=3, bf_12_Point_Nut_Flange_Dia=5.72)
        if self.bf_Bit_Type == 'bf_Phillips':
            bpy.ops.mesh.bolt_add(align='WORLD', location=(0, 0, 0), rotation=(0, 0, 0), change=False, bf_Model_Type='bf_Model_Bolt', bf_Head_Type='bf_Head_Hex', bf_Bit_Type='bf_Bit_Philips', bf_Nut_Type='bf_Nut_Hex', bf_Shank_Length=0, bf_Shank_Dia=3, bf_Phillips_Bit_Depth=1.14315, bf_Allen_Bit_Depth=1.5, bf_Allen_Bit_Flat_Distance=2.5, bf_Torx_Size_Type='bf_Torx_T10', bf_Torx_Bit_Depth=1.5, bf_Hex_Head_Height=2, bf_Hex_Head_Flat_Distance=5.5, bf_12_Point_Head_Height=3, bf_12_Point_Head_Flat_Distance=3, bf_12_Point_Head_Flange_Dia=5.72, bf_CounterSink_Head_Dia=6.3, bf_Cap_Head_Height=3, bf_Cap_Head_Dia=5.5, bf_Dome_Head_Dia=5.6, bf_Pan_Head_Dia=5.6, bf_Philips_Bit_Dia=1.82, bf_Thread_Length=20, bf_Major_Dia=3, bf_Pitch=0.35, bf_Minor_Dia=2.62111, bf_Crest_Percent=10, bf_Root_Percent=10, bf_Div_Count=36, bf_Hex_Nut_Height=2.4, bf_Hex_Nut_Flat_Distance=5.5, bf_12_Point_Nut_Height=3, bf_12_Point_Nut_Flat_Distance=3, bf_12_Point_Nut_Flange_Dia=5.72)
    def execute(self, context):
        n = self.get_failure()
        n.sort()
        self.get_bolt()
        r_m3_allen = random.uniform(1.4,1.7)
        r_m3_torx = random.uniform(1.3,1.6)
        r_m3_phillips = random.uniform(0.8,1.2)
        percent = self.bf_Corrosion_Percent
        bpy.ops.fail.corro(bf_Corrosion_Percent=percent)
        for x in n :
            if x == 2:
                if self.bf_Bit_Type == 'bf_Allen' :
                    bpy.ops.fail.head(bf_Bit_Type='bf_Allen', Bolt_Type='M3',Shank_Length=20,Hf_radius = r_m3_allen)
                if self.bf_Bit_Type == 'bf_Torx':
                    bpy.ops.fail.head(bf_Bit_Type='bf_Torx', Bolt_Type='M3',Shank_Length=20,Hf_radius = r_m3_torx)
                if self.bf_Bit_Type == 'bf_Phillips':
                    bpy.ops.fail.head(bf_Bit_Type='bf_Phillips',Bolt_Type='M3', Shank_Length=20,Hf_radius = r_m3_phillips)     
        return {'FINISHED'}
class Fail_random_m6_noBreak(bpy.types.Operator):
    bl_label = "Failure random_m6_noBreak"
    bl_idname = "fail.random_m6nobreak"
    bl_options = {'REGISTER', 'UNDO'}
    bf_Bit_List = [('None','None','None'),
                     ('bf_Allen','Allen','Allen'),
                     ('bf_Torx','Torx','Torx'),
                     ('bf_Phillips','Phillips','Phillips')]
    bf_Bit_Type:EnumProperty(
            attr='bf_Bit_Type',
            name='Bit Type',
            description='Choose the type of bit',
            items=bf_Bit_List,default='None'
            )
    bf_Corrosion_Percent:IntProperty(
            attr='bf_Corrosion_Percent',
            name='Corrosion Percent', default=0,
            min=0, soft_min=1,
            max=100,
            description='Percent of the corrosion',
            )    
    
    
    
    def draw(self, context):
        layout = self.layout
        layout.prop(self,'bf_Bit_Type')
        layout.prop(self,'bf_Corrosion_Percent')
    def get_failure(self):
        a=[1,2]
        k = random.randint(1,2)
        n = random.sample(a,k)
        return n
    def get_bolt(self):
        if self.bf_Bit_Type == 'bf_Allen':
            bpy.ops.mesh.bolt_add(align='WORLD', location=(0, 0, 0), rotation=(0, 0, 0), change=True, bf_Model_Type='bf_Model_Bolt', bf_Head_Type='bf_Head_Hex', bf_Bit_Type='bf_Bit_Allen', bf_Nut_Type='bf_Nut_Hex', bf_Shank_Length=0, bf_Shank_Dia=6, bf_Phillips_Bit_Depth=2.44961, bf_Allen_Bit_Depth=3, bf_Allen_Bit_Flat_Distance=5, bf_Torx_Size_Type='bf_Torx_T30', bf_Torx_Bit_Depth=3, bf_Hex_Head_Height=4, bf_Hex_Head_Flat_Distance=10, bf_12_Point_Head_Height=6, bf_12_Point_Head_Flat_Distance=6, bf_12_Point_Head_Flange_Dia=10.22, bf_CounterSink_Head_Dia=12.6, bf_Cap_Head_Height=6, bf_Cap_Head_Dia=10, bf_Dome_Head_Dia=12, bf_Pan_Head_Dia=12, bf_Philips_Bit_Dia=3.9, bf_Thread_Length=20, bf_Major_Dia=6, bf_Pitch=0.75, bf_Minor_Dia=5.1881, bf_Crest_Percent=10, bf_Root_Percent=10, bf_Div_Count=36, bf_Hex_Nut_Height=5, bf_Hex_Nut_Flat_Distance=10, bf_12_Point_Nut_Height=6, bf_12_Point_Nut_Flat_Distance=6, bf_12_Point_Nut_Flange_Dia=10.22)
        if self.bf_Bit_Type == 'bf_Torx':
            bpy.ops.mesh.bolt_add(align='WORLD', location=(0, 0, 0), rotation=(0, 0, 0), change=False, bf_Model_Type='bf_Model_Bolt', bf_Head_Type='bf_Head_Hex', bf_Bit_Type='bf_Bit_Torx', bf_Nut_Type='bf_Nut_Hex', bf_Shank_Length=0, bf_Shank_Dia=6, bf_Phillips_Bit_Depth=2.44961, bf_Allen_Bit_Depth=3, bf_Allen_Bit_Flat_Distance=5, bf_Torx_Size_Type='bf_Torx_T30', bf_Torx_Bit_Depth=3, bf_Hex_Head_Height=4, bf_Hex_Head_Flat_Distance=10, bf_12_Point_Head_Height=6, bf_12_Point_Head_Flat_Distance=6, bf_12_Point_Head_Flange_Dia=10.22, bf_CounterSink_Head_Dia=12.6, bf_Cap_Head_Height=6, bf_Cap_Head_Dia=10, bf_Dome_Head_Dia=12, bf_Pan_Head_Dia=12, bf_Philips_Bit_Dia=3.9, bf_Thread_Length=20, bf_Major_Dia=6, bf_Pitch=0.75, bf_Minor_Dia=5.1881, bf_Crest_Percent=10, bf_Root_Percent=10, bf_Div_Count=36, bf_Hex_Nut_Height=5, bf_Hex_Nut_Flat_Distance=10, bf_12_Point_Nut_Height=6, bf_12_Point_Nut_Flat_Distance=6, bf_12_Point_Nut_Flange_Dia=10.22)
        if self.bf_Bit_Type == 'bf_Phillips':
            bpy.ops.mesh.bolt_add(align='WORLD', location=(0, 0, 0), rotation=(0, 0, 0), change=False, bf_Model_Type='bf_Model_Bolt', bf_Head_Type='bf_Head_Hex', bf_Bit_Type='bf_Bit_Philips', bf_Nut_Type='bf_Nut_Hex', bf_Shank_Length=0, bf_Shank_Dia=6, bf_Phillips_Bit_Depth=2.44961, bf_Allen_Bit_Depth=3, bf_Allen_Bit_Flat_Distance=5, bf_Torx_Size_Type='bf_Torx_T30', bf_Torx_Bit_Depth=3, bf_Hex_Head_Height=4, bf_Hex_Head_Flat_Distance=10, bf_12_Point_Head_Height=6, bf_12_Point_Head_Flat_Distance=6, bf_12_Point_Head_Flange_Dia=10.22, bf_CounterSink_Head_Dia=12.6, bf_Cap_Head_Height=6, bf_Cap_Head_Dia=10, bf_Dome_Head_Dia=12, bf_Pan_Head_Dia=12, bf_Philips_Bit_Dia=3.9, bf_Thread_Length=20, bf_Major_Dia=6, bf_Pitch=0.75, bf_Minor_Dia=5.1881, bf_Crest_Percent=10, bf_Root_Percent=10, bf_Div_Count=36, bf_Hex_Nut_Height=5, bf_Hex_Nut_Flat_Distance=10, bf_12_Point_Nut_Height=6, bf_12_Point_Nut_Flat_Distance=6, bf_12_Point_Nut_Flange_Dia=10.22)
    def invoke(self, context, event):
        wm = context.window_manager
        return wm.invoke_props_dialog(self)   
    def execute(self, context):
        n = self.get_failure()
        n.sort()
        self.get_bolt()
        percent = self.bf_Corrosion_Percent
        bpy.ops.fail.corro(bf_Corrosion_Percent=percent)
        r_m6_allen = random.uniform(2.7,3.1)
        r_m6_torx = random.uniform(2.7,3.3)
        r_m6_phillips = random.uniform(1.8,2.3)
        for x in n :
            if x == 2:
                if self.bf_Bit_Type == 'bf_Allen' :
                    bpy.ops.fail.head(bf_Bit_Type='bf_Allen', Bolt_Type='M6',Shank_Length=20,Hf_radius = r_m6_allen)
                if self.bf_Bit_Type == 'bf_Torx':
                    bpy.ops.fail.head(bf_Bit_Type='bf_Torx', Bolt_Type='M6',Shank_Length=20,Hf_radius = r_m6_torx)
                if self.bf_Bit_Type == 'bf_Phillips':
                    bpy.ops.fail.head(bf_Bit_Type='bf_Phillips',Bolt_Type='M6', Shank_Length=20,Hf_radius = r_m6_phillips)     
        return {'FINISHED'}    
classes = [BoltFailure,Break,Corrosion,Headfail,Fail_random_m3,Fail_random_m6,Fail_random_m3_noBreak,Fail_random_m6_noBreak]



def register():
    for cls in classes:
        bpy.utils.register_class(cls)

def unregister():
    for cls in classes:
        bpy.utils.unregister_class(cls)



if __name__ == "__main__":
    register()