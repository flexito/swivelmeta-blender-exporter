from bpy.props import StringProperty
from ..swivelmeta_component import SwivelMetaComponent
from ..types import Category, PanelType, NodeType


class Dialog(SwivelMetaComponent):
    _definition = {
        'name': 'dialog',
        'display_name': 'Dialog',
        'category': Category.MEDIA,
        'node_type': NodeType.NODE,
        'panel_type': [PanelType.OBJECT],
        'icon': 'ERROR'
    }

    titleText: StringProperty(
        name="Title Text",
        description="Title text to be shown in the dialog",
        default=""
    )

    bodyText: StringProperty(
        name="Body Text",
        description="Body text to be shown in the dialog",
        default=""
    )
