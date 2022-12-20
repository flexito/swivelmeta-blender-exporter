from bpy.props import StringProperty
from ..swivelmeta_component import SwivelMetaComponent
from ..types import Category, PanelType, NodeType


class VideoTexture(SwivelMetaComponent):
    _definition = {
        'name': 'video-texture',
        'display_name': 'Video Texture',
        'category': Category.MATERIAL,
        'node_type': NodeType.NODE,
        'panel_type': [PanelType.OBJECT],
        'icon': 'FILE_MOVIE'
    }

    url: StringProperty(
        name="Video URL",
        description="Video texture to be mapped on object",
        default=""
    )