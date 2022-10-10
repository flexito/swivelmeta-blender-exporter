from bpy.props import StringProperty, BoolProperty, FloatProperty
from ..swivelmeta_component import SwivelMetaComponent
from ..types import Category, PanelType, NodeType


class DynamicTeleport(SwivelMetaComponent):
    _definition = {
        'name': 'dynamic-teleport',
        'display_name': 'Dynamic Teleport',
        'category': Category.DYNAMIC_CONTENT,
        'node_type': NodeType.NODE,
        'panel_type': [PanelType.OBJECT],
        'icon': 'LINKED'
    }

    id: StringProperty(
        name="ID",
        description="Unique identifier for use in the SwivelMeta Mixer app. Should only contain alphanumeric characters",
        default=""
    )

    name: StringProperty(
        name="Name",
        description="Name of link as shown in SwivelMeta Builder app",
        default=""
    )

    description: StringProperty(
        name="Description",
        description="Description of link as shown in SwivelMeta Builder app",
        default=""
    )

    url: StringProperty(
        name="Link URL",
        description="Default URL the link should point to",
        default="https://"
    )

    proximity: BoolProperty(
        name="Proximity Trigger",
        description="Teleports when the user gets close to this object's origin",
        default=False)

    proximityDistance: FloatProperty(
        name="Proximity Distance",
        description="Teleport trigger distance",
        default=1.0,
        min=0.0
    )
