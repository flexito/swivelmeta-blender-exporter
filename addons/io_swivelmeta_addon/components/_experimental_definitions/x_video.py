from ..swivelmeta_component import SwivelMetaComponent
from ..types import Category, PanelType, NodeType
from bpy.props import StringProperty


class ExperimentalVideo(SwivelMetaComponent):
    _definition = {
        'name': 'x-video',
        'display_name': 'Experimental Video',
        'category': Category.UTILITIES,
        'node_type': NodeType.NODE,
        'panel_type': [PanelType.OBJECT],
        'icon': 'CAMERA_DATA'
    }

    src: StringProperty(
        name="Source URL",
        description="URL pointing to video file",
        default="https://"
    )
