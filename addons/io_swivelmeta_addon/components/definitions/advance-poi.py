from ..swivelmeta_component import SwivelMetaComponent
from ..types import Category, PanelType, NodeType


class AdvancePOI(SwivelMetaComponent):
    _definition = {
        'name': 'advance-poi',
        'display_name': 'Advance POI',
        'category': Category.AUTOTOUR,
        'node_type': NodeType.NODE,
        'panel_type': [PanelType.OBJECT],
        'icon': 'ANIM'
    }
