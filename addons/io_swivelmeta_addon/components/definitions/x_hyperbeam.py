from ..swivelmeta_component import SwivelMetaComponent
from ..types import Category, PanelType, NodeType
from bpy.props import StringProperty, FloatProperty


class Hyperbeam(SwivelMetaComponent):
    _definition = {
        'name': 'hyperbeam',
        'display_name': 'Hyperbeam',
        'category': Category.EXPERIMENTAL,
        'node_type': NodeType.NODE,
        'panel_type': [PanelType.OBJECT],
        'icon': 'RESTRICT_VIEW_OFF'
    }

    refDistance: FloatProperty(
        name="Ref Distance",
        description="Audio Reference Distance",
        default=0.5,
        min=0.01,
        max=10.0)
