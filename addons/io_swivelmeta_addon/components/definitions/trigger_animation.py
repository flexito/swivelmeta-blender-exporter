from bpy.props import PointerProperty, StringProperty, BoolProperty, FloatProperty
from bpy.types import Object
from ..swivelmeta_component import SwivelMetaComponent
from ..types import Category, PanelType, NodeType


class TriggerAnimation(SwivelMetaComponent):
    _definition = {
        'name': 'trigger-animation',
        'display_name': 'Trigger Animation',
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
