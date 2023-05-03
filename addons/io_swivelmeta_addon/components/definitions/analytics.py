from bpy.props import StringProperty
from ..swivelmeta_component import SwivelMetaComponent
from ..types import Category, PanelType, NodeType


class Analytics(SwivelMetaComponent):
    _definition = {
        'name': 'analytics',
        'display_name': 'Analytics',
        'category': Category.MIXER,
        'node_type': NodeType.NODE,
        'panel_type': [PanelType.OBJECT],
        'icon': 'OUTLINER_DATA_LIGHT'
    }

    id: StringProperty(
        name="ID",
        description="Unique identifier for SwivelMeta Mixer analytics tab",
        default=""
    )

    description: StringProperty(
        name="Description",
        description="User-friendly description of what's being recorded",
        default=""
    )
