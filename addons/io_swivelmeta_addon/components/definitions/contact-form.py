from bpy.props import StringProperty
from ..swivelmeta_component import SwivelMetaComponent
from ..types import Category, PanelType, NodeType


class ContactForm(SwivelMetaComponent):
    _definition = {
        'name': 'contact-form',
        'display_name': 'Contact Form',
        'category': Category.APPLICATION,
        'node_type': NodeType.NODE,
        'panel_type': [PanelType.OBJECT],
        'icon': 'OUTLINER_DATA_GP_LAYER'
    }

    id: StringProperty(
        name="ID",
        description="Unique identifier for this form. Should use only alphanumeric characters and not include spaces.",
        default=""
    )

    displayName: StringProperty(
        name="DisplayName",
        description="Name as it should appear in the admin app UI",
        default=""
    )

    description: StringProperty(
        name="Description",
        description="Description of this this form.",
        default=""
    )
