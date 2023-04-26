from ..swivelmeta_component import SwivelMetaComponent
from ..types import Category, PanelType, NodeType
from bpy.props import PointerProperty
from bpy.types import Object


class Teleport(SwivelMetaComponent):
    _definition = {
        'name': 'teleport',
        'display_name': 'Teleport',
        'category': Category.NAVIGATION,
        'node_type': NodeType.NODE,
        'panel_type': [PanelType.OBJECT],
        'icon': 'TRACKING_REFINE_FORWARDS'
    }

    navPoint: PointerProperty(
        name="Destination",
        description="Destination Nav Point",
        type=Object
    )
