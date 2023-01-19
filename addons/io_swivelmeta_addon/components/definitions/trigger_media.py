from bpy.props import StringProperty, PointerProperty, EnumProperty, FloatProperty, BoolProperty
from bpy.types import Object
from ..swivelmeta_component import SwivelMetaComponent
from ..types import Category, PanelType, NodeType


class TriggerMedia(SwivelMetaComponent):
    _definition = {
        'name': 'trigger-media',
        'display_name': 'Trigger Media',
        'category': Category.TRIGGERS,
        'node_type': NodeType.NODE,
        'panel_type': [PanelType.OBJECT],
        'icon': 'PLAY'
    }

    targetObject: PointerProperty(
        name="Target Object",
        description="Object to hold video element",
        type=Object
    )

    type: EnumProperty(
        name="Trigger Type",
        description="Select type of trigger",
        items=[("proximity", "Proximity", "Will trigger when user gets close to this object"),
               ("clickable", "Clickable", "Will trigger when user clicks this object")],
        default="proximity")

    proximityDistance: FloatProperty(
        name="Proximity Distance",
        description="Distance from trigger before teleport initiated",
        default=1.0,
        min=0.0
    )
