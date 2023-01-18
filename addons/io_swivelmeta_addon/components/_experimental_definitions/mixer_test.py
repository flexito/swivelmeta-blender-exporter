from ..swivelmeta_component import SwivelMetaComponent
from ..types import Category, PanelType, NodeType


class MixerTest(SwivelMetaComponent):
    _definition = {
        'name': 'mixer-test',
        'display_name': 'Mixer Test',
        'category': Category.MIXER,
        'node_type': NodeType.NODE,
        'panel_type': [PanelType.OBJECT],
        'icon': 'UV_SYNC_SELECT'
    }
