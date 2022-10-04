from bpy.props import PointerProperty, StringProperty, BoolProperty, FloatProperty
from bpy.types import Object
from ..swivelmeta_component import SwivelMetaComponent
from ..types import Category, PanelType, NodeType


class AnimationTrigger(SwivelMetaComponent):
    _definition = {
        'name': 'animation-trigger',
        'display_name': 'Animation Trigger',
        'category': Category.ANIMATION,
        'node_type': NodeType.NODE,
        'panel_type': [PanelType.OBJECT],
        'icon': 'PIVOT_BOUNDBOX'
    }

    animatedObject: PointerProperty(
        name="Animated Object",
        description="Object to be animated",
        type=Object
    )

    track: StringProperty(
        name="Animation Track Name",
        description="Name of track to be animated",
        default=""
    )

    clickable: BoolProperty(
        name="Clickable",
        description="Teleports when the user clicks this object",
        default=True
    )

    proximity: BoolProperty(
        name="Proximity Trigger",
        description="Teleports when the user gets close to this object",
        default=True
    )

    proximityDistance: FloatProperty(
        name="Proximity Distance",
        description="Distance from teleporter before teleport initiated",
        default=1.0,
        min=0.0
    )
