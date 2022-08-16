from bpy.props import BoolProperty, FloatProperty
from ..swivelmeta_component import SwivelMetaComponent
from ..types import Category, PanelType, NodeType


class EcommerceVendorLogo(SwivelMetaComponent):
    _definition = {
        'name': 'ecommerce-product-image',
        'display_name': 'E-Commerce Product Image',
        'category': Category.ECOMMERCE,
        'node_type': NodeType.NODE,
        'panel_type': [PanelType.OBJECT],
        'icon': 'IMAGE_DATA'
    }

    showControls: BoolProperty(
        name="Show Controls",
        description="Show next and previous buttons",
        default=True
    )

    autoAdvance: BoolProperty(
        name="Auto Advance",
        description="Automatically advance images",
        default=True
    )

    autoAdvanceTiming: FloatProperty(
        name="Auto Advance Timing",
        description="Number of seconds before the next image is shown",
        default=5.0,
        min=0.01
    )