from bpy.props import FloatProperty, IntProperty
from ..swivelmeta_component import SwivelMetaComponent
from ..types import Category, PanelType, NodeType


class EcommerceProduct(SwivelMetaComponent):
    _definition = {
        'name': 'ecommerce-product',
        'display_name': 'E-Commerce Product',
        'category': Category.ECOMMERCE,
        'node_type': NodeType.NODE,
        'panel_type': [PanelType.OBJECT],
        'icon': 'SCENE_DATA'
    }

    displayRadius: FloatProperty(
        name="Display Radius",
        description="This sets the size of the product and image carousel; should roughly match the radius of your display",
        default=1.0,
        min=0.25
    )

    displayIndex: IntProperty(
        name="Display Index",
        description="Determines order in which to fill the displays (i.e. if only one product is available, the display with the lowest Display Index will be used.",
        default=1,
        min=1
    )
