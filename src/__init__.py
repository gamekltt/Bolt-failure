bl_info = {
    "name": "Damaged Bolt Sub Version",
    "author": "Liu Yang",
    "version": (0, 0, 1),
    "blender": (2, 80, 0),
    "location": "View3D > Sidebar > Edit Tab",
    "description": "Bar Combine",
    "category": "Object",
}

from bpy.props import (
    BoolProperty,
    StringProperty,
    EnumProperty,
    IntProperty,
    FloatProperty,
)
from bpy.types import (
    AddonPreferences,
    Operator,
    Panel,
    Menu,
)
import random
import bpy
from .damaged_bolt import *

classes = [BoltFailure, Break, Corrosion, Headfail, Fail_random_m3,
           Fail_random_m6, Fail_random_m3_noBreak, Fail_random_m6_noBreak]


def register():
    for cls in classes:
        bpy.utils.register_class(cls)


def unregister():
    for cls in classes:
        bpy.utils.unregister_class(cls)
