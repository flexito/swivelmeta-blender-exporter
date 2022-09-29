from bpy.props import StringProperty
from ..swivelmeta_component import SwivelMetaComponent
from ..types import Category, PanelType, NodeType


class victorTest(SwivelMetaComponent):
    _definition = {
        'name': 'victor-test',
        'display_name': 'Victor Test',
        'category': Category.MATERIAL,
        'node_type': NodeType.NODE,
        'panel_type': [PanelType.OBJECT],
        'icon': 'FILE_MOVIE'
    }

    url: StringProperty(
        name="Video URL",
        description="",
        default=""
    )
