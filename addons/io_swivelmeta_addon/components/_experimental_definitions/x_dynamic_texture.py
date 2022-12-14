from ..swivelmeta_component import SwivelMetaComponent
from ..types import Category, PanelType, NodeType


class DynamicTexture(SwivelMetaComponent):
    _definition = {
        'name': 'dynamic-texture',
        'display_name': 'Dynamic Texture',
        'category': Category.EXPERIMENTAL,
        'node_type': NodeType.NODE,
        'panel_type': [PanelType.OBJECT],
        'icon': 'IMAGE_DATA'
    }
