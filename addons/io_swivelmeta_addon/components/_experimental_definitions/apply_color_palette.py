from bpy.props import StringProperty
from ..swivelmeta_component import SwivelMetaComponent
from ..types import Category, PanelType, NodeType


class ApplyColorPalette(SwivelMetaComponent):
    _definition = {
        'name': 'apply-color-palette',
        'display_name': 'Apply Color Palette',
        'category': Category.MATERIAL,
        'node_type': NodeType.NODE,
        'panel_type': [PanelType.OBJECT],
        'icon': 'RESTRICT_COLOR_ON'
    }

    primaryColorKey: StringProperty(
        name="Primary color",
        description="Name of material to be replaced with the project's primary color (optional)",
        default=""
    )

    secondaryColorKey: StringProperty(
        name="Secondary color",
        description="Name of material to be replaced with the project's secondary color (optional)",
        default=""
    )

    tertiaryColorKey: StringProperty(
        name="Tertiary color",
        description="Name of material to be replaced with the project's tertiary color (optional)",
        default=""
    )
