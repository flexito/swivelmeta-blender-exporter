from .io import gltf_exporter
from . import (nodes, components)
from . import preferences
bl_info = {
    "name": "SwivelMeta Blender Addon",
    "author": "SwivelMeta",
    "description": "Tools for developing GLTF assets for SwivelMeta",
    "blender": (3, 1, 2),
    "version": (1, 0, 0),
    "location": "",
    "wiki_url": "https://swivelmeta.io",
    "tracker_url": "https://swivelmeta.io",
    "support": "COMMUNITY",
    "warning": "",
    "category": "Generic"
}


def register():
    preferences.register()
    gltf_exporter.register()
    nodes.register()
    components.register()
    print("Register SwivelMeta Addon")


def unregister():
    components.unregister()
    nodes.unregister()
    gltf_exporter.unregister()
    preferences.unregister()
    print("Unregister SwivelMeta Addon")


# called by gltf-blender-io after it has loaded


glTF2ExportUserExtension = gltf_exporter.glTF2ExportUserExtension
glTF2_pre_export_callback = gltf_exporter.glTF2_pre_export_callback
glTF2_post_export_callback = gltf_exporter.glTF2_post_export_callback


def register_panel():
    return gltf_exporter.register_export_panel()
