from ..swivelmeta_component import SwivelMetaComponent
from ..types import Category, PanelType, NodeType


class DynamicLink(SwivelMetaComponent):
    _definition = {
        'name': 'dynamic-link',
        'display_name': 'Dynamic Link',
        'category': Category.ECOMMERCE,
        'node_type': NodeType.NODE,
        'panel_type': [PanelType.OBJECT],
        'icon': 'LINKED'
    }
