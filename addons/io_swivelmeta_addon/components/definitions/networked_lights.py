from bpy.props import PointerProperty, StringProperty
from bpy.types import Object
from ..swivelmeta_component import SwivelMetaComponent
from ..types import Category, PanelType, NodeType
from .networked import migrate_networked


class NetworkedLights(SwivelMetaComponent):
    _definition = {
        'name': 'networked-lights',
        'display_name': 'Networked Lights',
        'category': Category.EXPERIMENTAL,
        'node_type': NodeType.NODE,
        'panel_type': [PanelType.OBJECT],
        'deps': ['networked'],
        'icon': 'UV_SYNC_SELECT'
    }

    target: PointerProperty(
        name="Target",
        description="Object to be animated",
        type=Object
    )

    colors: StringProperty(
        name="Colors",
        description="Input color hex values separated by commas (i.e. #ff0000,#00ff00,#0000ff)",
        default="#ffffff"
    )

    @classmethod
    def migrate(cls, version):
        migrate_networked(cls.get_name())
