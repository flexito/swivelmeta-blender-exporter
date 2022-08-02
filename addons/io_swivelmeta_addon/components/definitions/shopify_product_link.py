from bpy.props import StringProperty
from ..swivelmeta_component import SwivelMetaComponent
from ..types import Category, PanelType, NodeType


class ShopifyProductLink(SwivelMetaComponent):
    _definition = {
        'name': 'shopify_product_link',
        'display_name': 'Shopify Product Link',
        'category': Category.ECOMMERCE,
        'node_type': NodeType.NODE,
        'panel_type': [PanelType.OBJECT, PanelType.BONE],
        'icon': 'LINKED'
    }

    href: StringProperty(name="Link URL", description="Link URL",
                         default="https://swivelmeta.io")

