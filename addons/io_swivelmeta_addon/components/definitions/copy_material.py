from ..swivelmeta_component import SwivelMetaComponent
from ..types import Category, PanelType, NodeType
from bpy.props import PointerProperty, StringProperty
from bpy.types import Object


class IntraRoomTeleport(SwivelMetaComponent):
    _definition = {
        'name': 'copy-material',
        'display_name': 'Copy Material',
        'category': Category.MATERIAL,
        'node_type': NodeType.NODE,
        'panel_type': [PanelType.OBJECT],
        'icon': 'DUPLICATE'
    }

    sourceObject: PointerProperty(
        name="Source",
        description="Source object to copy material from",
        type=Object
    )
