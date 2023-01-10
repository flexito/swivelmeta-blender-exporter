from bpy.props import StringProperty
from ..swivelmeta_component import SwivelMetaComponent
from ..types import Category, PanelType, NodeType


class Mixer(SwivelMetaComponent):
    _definition = {
        'name': 'mixer',
        'display_name': 'Mixer',
        'category': Category.MIXER,
        'node_type': NodeType.NODE,
        'panel_type': [PanelType.OBJECT],
        'icon': 'UV_SYNC_SELECT'
    }

    id: StringProperty(
        name="ID",
        description="Unique identifier for use in the SwivelMeta Mixer app. Should only contain alphanumeric characters",
        default=""
    )

    name: StringProperty(
        name="Name",
        description="Name as shown in SwivelMeta Mixer app",
        default=""
    )

    description: StringProperty(
        name="Description",
        description="Description as shown in SwivelMeta Mixer app",
        default=""
    )
