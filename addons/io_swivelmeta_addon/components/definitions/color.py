from ..swivelmeta_component import SwivelMetaComponent
from ..types import Category, PanelType, NodeType
from bpy.props import StringProperty
from bpy.types import Object


class Color(SwivelMetaComponent):
    _definition = {
        'name': 'color',
        'display_name': 'Color',
        'category': Category.MATERIAL,
        'node_type': NodeType.NODE,
        'panel_type': [PanelType.OBJECT],
        'icon': 'CAMERA_DATA'
    }

    colorHex: StringProperty(
        name="Color Hex Code",
        description="Replaces all materials' diffuse and emissive colors. Should begin with a # sign (i.e. #ff0000)",
        default="#ffffff"
    )
