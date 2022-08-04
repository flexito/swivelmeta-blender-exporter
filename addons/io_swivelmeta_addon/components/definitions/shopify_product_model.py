from ..swivelmeta_component import SwivelMetaComponent
from ..types import Category, PanelType, NodeType


class ShopifyProductModel(SwivelMetaComponent):
    _definition = {
        'name': 'shopify_product_model',
        'display_name': 'Shopify Product Model',
        'category': Category.ECOMMERCE,
        'node_type': NodeType.NODE,
        'panel_type': [PanelType.OBJECT],
        'icon': 'LINKED'
    }

