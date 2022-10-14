from bpy.props import PointerProperty, StringProperty, BoolProperty, FloatProperty
from bpy.types import Object
from ..swivelmeta_component import SwivelMetaComponent
from ..types import Category, PanelType, NodeType
from .networked import migrate_networked


class TriggerFlipFlopAnimation(SwivelMetaComponent):
    _definition = {
        'name': 'trigger-flipflop-animation',
        'display_name': 'Trigger Flip-Flop Animation',
        'category': Category.TRIGGERS,
        'node_type': NodeType.NODE,
        'panel_type': [PanelType.OBJECT],
        'icon': 'TRACKING'
    }

    networked: BoolProperty(
        name="Networked",
        description="If true, this animation will be played for all users",
        default=False)

    targetObject: PointerProperty(
        name="Target Object",
        description="Object with animations to be triggered",
        type=Object
    )

    openTrack: StringProperty(
        name="Open Track",
        description="Name of track to be animated during open event",
        default=""
    )

    closeTrack: StringProperty(
        name="Close Track",
        description="Name of track to be animated during close event",
        default=""
    )

    proximity: BoolProperty(
        name="Proximity Trigger",
        description="Triggers animation when the user gets close to this object's origin",
        default=False)

    proximityDistance: FloatProperty(
        name="Proximity Distance",
        description="Distance from object's origin before animation is triggered",
        default=1.0,
        min=0.0
    )

    @classmethod
    def migrate(cls, version):
        migrate_networked(cls.get_name())
