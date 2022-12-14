from bpy.props import IntProperty
from ..swivelmeta_component import SwivelMetaComponent
from ..types import Category, PanelType, NodeType


class EcommerceVendorMedia(SwivelMetaComponent):
    _definition = {
        'name': 'ecommerce-vendor-media',
        'display_name': 'E-Commerce Vendor Media',
        'category': Category.ECOMMERCE,
        'node_type': NodeType.NODE,
        'panel_type': [PanelType.OBJECT],
        'icon': 'IMAGE_DATA'
    }

    displayIndex: IntProperty(
        name="Display Index",
        description="Determines order in which to fill the media displays (i.e. if only one product is available, the display with the lowest Display Index will be used.",
        default=1,
        min=1
    )
