from bpy.props import PointerProperty, StringProperty, BoolProperty, EnumProperty, FloatProperty
from bpy.types import Object
from ..swivelmeta_component import SwivelMetaComponent
from ..types import Category, PanelType, NodeType
from .networked import migrate_networked


class TriggerAnimation(SwivelMetaComponent):
    _definition = {
        'name': 'trigger-animation',
        'display_name': 'Trigger Animation',
        'category': Category.TRIGGERS,
        'node_type': NodeType.NODE,
        'panel_type': [PanelType.OBJECT],
        'deps': ['networked'],
        'icon': 'PIVOT_BOUNDBOX'
    }

    target: PointerProperty(
        name="Target",
        description="Object to be animated",
        type=Object
    )

    openAnimation: StringProperty(
        name="Open Animation",
        description="(required) NLA track name for the animation played once when the trigger is opened",
        default=""
    )

    openLoop: StringProperty(
        name="Open Loop",
        description="(optional) NLA track name for the looping animation that plays while trigger is opened",
        default=""
    )

    closeAnimation: StringProperty(
        name="Close Animation",
        description="(optional) NLA track name for the animation played once when the trigger is closed",
        default=""
    )

    closeLoop: StringProperty(
        name="Close Loop",
        description="(optional) NLA track name for the looping animation that plays while trigger is closed",
        default=""
    )

    type: EnumProperty(
        name="Trigger Type",
        description="Select type of trigger",
        items=[("PROXIMITY", "Proximity", "Will trigger when user gets close to this object"),
               ("CLICKABLE", "Clickable", "Will trigger when user clicks this object")],
        default="PROXIMITY")

    proximityDistance: FloatProperty(
        name="Proximity Distance",
        description="Distance from object's origin before animation is triggered",
        default=1.0,
        min=0.0
    )

    playOnce: BoolProperty(
        name="Play Once",
        description="If true, plays the open animation once and prevents repeat",
        default=False)

    networked: BoolProperty(
        name="Networked",
        description="Whether or not this animation should be experienced by other users",
        default=True)

    @classmethod
    def migrate(cls, version):
        migrate_networked(cls.get_name())
