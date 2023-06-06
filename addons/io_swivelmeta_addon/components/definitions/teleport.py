from ..swivelmeta_component import SwivelMetaComponent
from ..types import Category, PanelType, NodeType
from bpy.props import PointerProperty, EnumProperty, FloatProperty
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

    teleportSpeed: FloatProperty(
        name="Teleport Speed",
        description="Teleport speed in meters/second",
        default=3.0,
        min=0.0
    )

    triggerType: EnumProperty(
        name="Trigger Type",
        description="Select type of trigger",
        items=[("PROXIMITY", "Proximity", "Will trigger when user gets close to this object"),
               ("CLICKABLE", "Clickable", "Will trigger when user clicks this object")],
        default="CLICKABLE")

    proximityDistance: FloatProperty(
        name="Proximity Distance",
        description="Distance from object's origin before teleport is triggered",
        default=1.0,
        min=0.0
    )
