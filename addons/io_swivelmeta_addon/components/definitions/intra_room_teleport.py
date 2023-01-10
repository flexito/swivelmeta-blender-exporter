from ..swivelmeta_component import SwivelMetaComponent
from ..types import Category, PanelType, NodeType
from bpy.props import BoolProperty, PointerProperty, FloatProperty
from bpy.types import Object

class IntraRoomTeleport(SwivelMetaComponent):
    _definition = {
        'name': 'intra-room-teleport',
        'display_name': 'Intra-room Teleport',
        'category': Category.NAVIGATION,
        'node_type': NodeType.NODE,
        'panel_type': [PanelType.OBJECT],
        'icon': 'TRACKING_REFINE_FORWARDS'
    }

    destinationObject: PointerProperty(
        name="Destination",
        description="Destination object the avatar will teleport to",
        type=Object
    )
    
    clickable: BoolProperty(
        name="Clickable",
        description="Teleports when the user clicks this object",
        default=True)

    proximity: BoolProperty(
        name="Proximity Trigger",
        description="Teleports when the user gets close to this object",
        default=True)

    proximityDistance: FloatProperty(
        name="Proximity Distance",
        description="Distance from teleporter before teleport initiated",
        default=1.0,
        min=0.0,
        soft_min=0.0)