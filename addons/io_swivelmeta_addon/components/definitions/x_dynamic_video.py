from bpy.props import EnumProperty
from ..swivelmeta_component import SwivelMetaComponent
from ..types import Category, PanelType, NodeType


class DynamicVideo(SwivelMetaComponent):
    _definition = {
        'name': 'dynamic-video',
        'display_name': 'Dynamic Video',
        'category': Category.EXPERIMENTAL,
        'node_type': NodeType.NODE,
        'panel_type': [PanelType.OBJECT],
        'icon': 'CAMERA_DATA'
    }

    channel: EnumProperty(
        name="Channel",
        description="Channel",
        items=[("video1", "Video 1", "Configures video 1 from builder app"),
               ("video2", "Video 2", "Configures video 2 from builder app"),
               ("video3", "Video 3", "Configures video 3 from builder app")],
        default="video1")
