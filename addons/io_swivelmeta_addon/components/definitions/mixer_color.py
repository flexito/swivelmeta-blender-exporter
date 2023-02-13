from bpy.props import StringProperty, FloatVectorProperty
from ..swivelmeta_component import SwivelMetaComponent
from ..types import Category, PanelType, NodeType
from ..utils import toHex


class MixerColor(SwivelMetaComponent):

    def update_hex_color(self, context):
        self.hexColor = toHex(self.color[0], self.color[1], self.color[2])

    def update_color(self, context):
        self.color = [
            int(self.hexColor[1:3], 16) / 255,
            int(self.hexColor[3:5], 16) / 255,
            int(self.hexColor[5:7], 16) / 255,
            1
        ]

    _definition = {
        'name': 'mixer-color',  # name of the A-Frame component
        'display_name': 'Mixer Color',  # name displayed in Blender
        'category': Category.EXPERIMENTAL,  # category in Blender
        'node_type': NodeType.NODE,
        # panel in Blender where the component will be displayed
        'panel_type': [PanelType.OBJECT],
        # icon in Blender that will be displayed next to the component name
        'icon': 'SHADING_SOLID'
    }

    color: FloatVectorProperty(
        name="Color",
        description="Color",
        subtype='COLOR',
        default=(1.0, 1.0, 1.0, 1.0),
        size=4,
        min=0,
        max=1,
        update=update_hex_color
    )

    hexColor: StringProperty(
        name="Hex Color",
        description="Hex color value. (e.g. #ff0000 or 0xff0000 or ff0000) are all valid values.",
        default="ffffff",
    )
