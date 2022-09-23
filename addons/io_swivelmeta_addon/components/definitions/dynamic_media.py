from bpy.props import StringProperty
from ..swivelmeta_component import SwivelMetaComponent
from ..types import Category, PanelType, NodeType
import uuid


class DynamicMedia(SwivelMetaComponent):
    _definition = {
        'name': 'dynamic-media',
        'display_name': 'Dynamic Media',
        'category': Category.DYNAMIC_CONTENT,
        'node_type': NodeType.NODE,
        'panel_type': [PanelType.OBJECT],
        'icon': 'IMAGE_DATA'
    }

    id: StringProperty(
        name="ID",
        description="Unique identifier for use in the SwivelMeta Mixer app. Should only contain alphanumeric characters",
        default=""
    )

    name: StringProperty(
        name="Name",
        description="Name of media element as shown in SwivelMeta Mixer app",
        default=""
    )

    description: StringProperty(
        name="Description",
        description="Description of media element as shown in SwivelMeta Mixer app",
        default=""
    )

    src: StringProperty(
        name="Media Source",
        description="Default media source URL",
        default="https://"
    )
