from ..swivelmeta_component import SwivelMetaComponent
from ..types import Category, PanelType, NodeType


class ShopifyVendorLogo(SwivelMetaComponent):
    _definition = {
        'name': 'shopify_vendor_logo',
        'display_name': 'Shopify Vendor Logo',
        'category': Category.ECOMMERCE,
        'node_type': NodeType.NODE,
        'panel_type': [PanelType.OBJECT],
        'icon': 'IMAGE_DATA'
    }

