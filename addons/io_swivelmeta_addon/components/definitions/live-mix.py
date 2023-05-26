from bpy.props import StringProperty
from ..swivelmeta_component import SwivelMetaComponent
from ..types import Category, PanelType, NodeType


class LiveMix(SwivelMetaComponent):
    _definition = {
        'name': 'live-mix',
        'display_name': 'Live Mix',
        'category': Category.MIXER,
        'node_type': NodeType.NODE,
        'panel_type': [PanelType.OBJECT],
        'icon': 'SHADERFX'
    }

    id: StringProperty(
        name="Mixer ID",
        description="Mixer ID for the media to be configured",
        default=""
    )
