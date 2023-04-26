from bpy.props import FloatProperty
from bpy.types import Object
from ..swivelmeta_component import SwivelMetaComponent
from ..types import Category, PanelType, NodeType
from .networked import migrate_networked


class NetworkedLights(SwivelMetaComponent):
    _definition = {
        'name': 'networked-cube',
        'display_name': 'Networked Cube',
        'category': Category.EXPERIMENTAL,
        'node_type': NodeType.NODE,
        'panel_type': [PanelType.OBJECT],
        'deps': ['networked'],
        'icon': 'UV_SYNC_SELECT'
    }

    hue: FloatProperty(
        name="Hue",
        description="Hue for cube material",
        min=0.0,
        max=1.0,
        default=0.5)

    @classmethod
    def migrate(cls, version):
        migrate_networked(cls.get_name())
