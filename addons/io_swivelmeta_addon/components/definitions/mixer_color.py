from bpy.props import StringProperty, FloatVectorProperty, BoolProperty
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

    def update_visible(self, context):
        self.color = self.color.is_hidden

    def draw(self, context, layout, panel_type):
        '''Draw method to be called by the panel. The base class method will print all the component properties'''
        for key in self.__annotations__.keys():
            if key == "color" and self.hideColorWheel == True:
                continue  # Skips drawing the color wheel || color property
            elif not self.bl_rna.properties[key].is_hidden:
                layout.prop(data=self, property=key)

    _definition = {
        'name': 'mixer-color',  # name of the A-Frame component
        'display_name': 'Mixer Color',  # name displayed in Blender
        'category': Category.EXPERIMENTAL,  # category in Blender
        'node_type': NodeType.NODE,
        # panel in Blender where the component will be displayed
        'panel_type': [PanelType.OBJECT],
        # icon in Blender that will be displayed next to the component name
        'icon': 'COLOR'
    }

    color: FloatVectorProperty(
        name="Color",
        description="Updating this value will update the hex color value automatically. Hide the color wheel to only use the hex color value, or to keep from accidentally changing the color",
        subtype='COLOR',
        default=(1.0, 1.0, 1.0, 1.0),
        size=4,
        min=0,
        max=1,
        update=update_hex_color
    )

    hexColor: StringProperty(
        name="Hex Color",
        description="Hex color value. (e.g. #ff0000 or 0xff0000 or ff0000) are all valid values",
        default="ffffff",
    )

    hideColorWheel: BoolProperty(
        name="Hide Color Wheel?",
        description="Set to true to hide the color wheel in the UI",
        default=False,
        # update=update_visible
    )
