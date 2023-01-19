from ..swivelmeta_component import SwivelMetaComponent
from ..types import Category, PanelType, NodeType


class FullBodyCharacter(SwivelMetaComponent):
    _definition = {
        'name': 'full-body-character',
        'display_name': 'Full-Body Character',
        'category': Category.EXPERIMENTAL,
        'node_type': NodeType.NODE,
        'panel_type': [PanelType.OBJECT],
        'icon': 'ARMATURE_DATA'
    }
