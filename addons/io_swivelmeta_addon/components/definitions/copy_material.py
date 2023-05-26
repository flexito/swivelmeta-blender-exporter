from ..swivelmeta_component import SwivelMetaComponent
from ..types import Category, PanelType, NodeType
from bpy.props import PointerProperty, BoolProperty, FloatProperty
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

    responsive: BoolProperty(
        name="Responsive",
        description="If checked, uses the Frame Width and Frame Height to autofit images in the display without stretching",
        default=False
    )

    frameWidth: FloatProperty(
        name="Frame Width",
        description="Width of frame for responsive scaling (unused if responsive is unchecked)",
        default=1.0,
        min=0.0
    )

    frameHeight: FloatProperty(
        name="Frame Height",
        description="Height of frame for responsive scaling (unused if responsive is unchecked)",
        default=1.0,
        min=0.0
    )
