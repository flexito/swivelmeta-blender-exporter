from bpy.props import FloatVectorProperty
from ..swivelmeta_component import SwivelMetaComponent
from ..types import Category, PanelType, NodeType


class Teleport(SwivelMetaComponent):
    _definition = {
        'name': 'teleport',
        'display_name': 'Teleport',
        'category': Category.NAVIGATION,
        'node_type': NodeType.NODE,
        'panel_type': [PanelType.OBJECT],
        'icon': 'LINKED'
    }

    destination: FloatVectorProperty(name="Destination",
                               description="Destination",
                               size=3,
                               subtype="XYZ",
                               default=[0, 0, 0
                               ])

