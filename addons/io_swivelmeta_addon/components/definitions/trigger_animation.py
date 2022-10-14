from bpy.props import PointerProperty, StringProperty, BoolProperty, FloatProperty
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

    networked: BoolProperty(
        name="Networked",
        description="If true, this animation will be played for all users",
        default=False)

    animatedObject: PointerProperty(
        name="Animated Object",
        description="Object to be animated",
        type=Object
    )

    track: StringProperty(
        name="Animation Track Name",
        description="Name of track to be played",
        default=""
    )

    @classmethod
    def migrate(cls, version):
        migrate_networked(cls.get_name())
