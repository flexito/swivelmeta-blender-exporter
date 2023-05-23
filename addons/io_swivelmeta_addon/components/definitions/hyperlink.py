from ..swivelmeta_component import SwivelMetaComponent
from ..types import Category, PanelType, NodeType
from bpy.props import StringProperty, BoolProperty
from bpy.types import Object


class IntraRoomTeleport(SwivelMetaComponent):
    _definition = {
        'name': 'hyperlink',
        'display_name': 'Hyperlink',
        'category': Category.APPLICATION,
        'node_type': NodeType.NODE,
        'panel_type': [PanelType.OBJECT],
        'icon': 'LIBRARY_DATA_DIRECT'
    }

    url: StringProperty(
        name="Link URL",
        description="Link URL",
        default="https://"
    )

    newTab: BoolProperty(
        name="New Tab",
        description="If true, opens link in new tab. If false, opens the link in this tab.",
        default=True
    )
