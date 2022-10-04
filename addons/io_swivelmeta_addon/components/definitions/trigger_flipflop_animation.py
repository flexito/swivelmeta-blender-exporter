from bpy.props import PointerProperty, StringProperty, EnumProperty, FloatProperty
from bpy.types import Object
from ..swivelmeta_component import SwivelMetaComponent
from ..types import Category, PanelType, NodeType


class TriggerFlipFlopAnimation(SwivelMetaComponent):
    _definition = {
        'name': 'trigger-flipflop-animation',
        'display_name': 'Trigger Flip-Flop Animation',
        'category': Category.ANIMATION,
        'node_type': NodeType.NODE,
        'panel_type': [PanelType.OBJECT],
        'icon': 'TRACKING'
    }

    triggerObject: PointerProperty(
        name="Trigger Object",
        description="Object that triggers the animation",
        type=Object
    )

    openTrack: StringProperty(
        name="Open Animation Track Name",
        description="Name of track to be animated during open event",
        default=""
    )

    closeTrack: StringProperty(
        name="Close Animation Track Name",
        description="Name of track to be animated during close event",
        default=""
    )

    triggerType: EnumProperty(
        name="Trigger Type",
        description="Sets how users will trigger the animation",
        items=[("CLICKABLE", "Clickable", "Animation triggered by clicking the Trigger Object"),
               ("PROXIMITY", "Proximity", "Animation triggered when avatars get close to the Trigger Object")],
        default="CLICKABLE")

    proximityDistance: FloatProperty(
        name="Proximity Distance",
        description="Avatar distance from Trigger Object before animation is triggered",
        default=1.0,
        min=0.0
    )
