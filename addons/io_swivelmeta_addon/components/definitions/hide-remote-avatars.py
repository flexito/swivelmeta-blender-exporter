from bpy.props import StringProperty
from ..swivelmeta_component import SwivelMetaComponent
from ..types import Category, PanelType, NodeType


class ContactForm(SwivelMetaComponent):
    _definition = {
        'name': 'hide-remote-avatars',
        'display_name': 'Hide Remote Avatars',
        'category': Category.APPLICATION,
        'node_type': NodeType.NODE,
        'panel_type': [PanelType.OBJECT],
        'icon': 'COMMUNITY'
    }
