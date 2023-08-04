from ..swivelmeta_component import SwivelMetaComponent
from ..types import Category, PanelType, NodeType
from bpy.props import StringProperty


class SwitchRooms(SwivelMetaComponent):
    _definition = {
        'name': 'switch-room',
        'display_name': 'Switch Room',
        'category': Category.APPLICATION,
        'node_type': NodeType.NODE,
        'panel_type': [PanelType.OBJECT, PanelType.BONE],
        'icon': 'TRACKING_FORWARDS_SINGLE'
    }

    roomID: StringProperty(
        name="Room ID",
        description="Hubs Room ID to fast-switch to",
        default="")
