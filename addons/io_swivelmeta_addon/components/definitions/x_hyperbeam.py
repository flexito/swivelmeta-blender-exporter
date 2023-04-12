from ..swivelmeta_component import SwivelMetaComponent
from ..types import Category, PanelType, NodeType
from bpy.props import StringProperty


class Hyperbeam(SwivelMetaComponent):
    _definition = {
        'name': 'hyperbeam',
        'display_name': 'Hyperbeam',
        'category': Category.EXPERIMENTAL,
        'node_type': NodeType.NODE,
        'panel_type': [PanelType.OBJECT],
        'icon': 'RESTRICT_VIEW_OFF'
    }

    embedUrl: StringProperty(
        name="Embed URL",
        description="Hyperbeam Embed URL",
        default=""
    )
