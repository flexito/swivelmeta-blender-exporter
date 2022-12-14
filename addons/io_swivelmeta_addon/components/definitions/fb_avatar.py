from bpy.props import StringProperty
from ..swivelmeta_component import SwivelMetaComponent
from ..types import Category, PanelType, NodeType


class victorTest(SwivelMetaComponent):
    _definition = {
        'name': 'fb-character',
        'display_name': 'FB Character',
        'category': Category.EXPERIMENTAL,
        'node_type': NodeType.NODE,
        'panel_type': [PanelType.OBJECT],
        'icon': 'CON_ARMATURE'
    }
