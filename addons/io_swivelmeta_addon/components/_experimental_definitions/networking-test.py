from bpy.types import Object
from ..swivelmeta_component import SwivelMetaComponent
from ..types import Category, PanelType, NodeType
from .networked import migrate_networked


class NetworkingTest(SwivelMetaComponent):
    _definition = {
        'name': 'networking-test',
        'display_name': 'Networking Test',
        'category': Category.EXPERIMENTAL,
        'node_type': NodeType.NODE,
        'panel_type': [PanelType.OBJECT],
        'deps': ['networked'],
        'icon': 'UV_SYNC_SELECT'
    }

    @classmethod
    def migrate(cls, version):
        migrate_networked(cls.get_name())
