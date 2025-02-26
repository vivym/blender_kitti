# -*- coding: utf-8 -*-
""""""

from .bpy_helper import needs_bpy_bmesh


@needs_bpy_bmesh()
def enable_cycles_render_devices(*, bpy):
    # setup render devices. Use all.
    cycles_prefs = bpy.context.preferences.addons["cycles"].preferences
    cycles_prefs.compute_device_type = "CUDA"
    cycles_prefs.get_devices()
    try:
        # blender2.81+
        for device_type in cycles_prefs.get_device_types(bpy.context):
            cycles_prefs.get_devices_for_type(device_type[0])
    except AttributeError:
        pass
    for device in cycles_prefs.devices:
        device.use = True


@needs_bpy_bmesh()
def setup_system(enable_gpu_rendering: bool = True, scene=None, *, bpy):
    if enable_gpu_rendering:
        enable_cycles_render_devices()
        if scene is None:
            scene = bpy.context.scene
        scene.cycles.device = "GPU"
