from bpy.props import StringProperty
from ..swivelmeta_component import SwivelMetaComponent
from ..types import Category, PanelType, NodeType


class PostToDiscord(SwivelMetaComponent):
    _definition = {
        'name': 'post-to-discord',
        'display_name': 'Post to Discord',
        'category': Category.EXPERIMENTAL,
        'node_type': NodeType.NODE,
        'panel_type': [PanelType.OBJECT],
        'icon': 'ALIGN_LEFT'
    }

    channel: StringProperty(
        name="Channel",
        description="Discord channel you would like users to post to.",
        default=""
    )
