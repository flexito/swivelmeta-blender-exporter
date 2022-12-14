from ..swivelmeta_component import SwivelMetaComponent
from ..types import Category, PanelType, NodeType


class EcommerceVendorLogo(SwivelMetaComponent):
    _definition = {
        'name': 'ecommerce-vendor-logo',
        'display_name': 'E-Commerce Vendor Logo',
        'category': Category.ECOMMERCE,
        'node_type': NodeType.NODE,
        'panel_type': [PanelType.OBJECT],
        'icon': 'IMAGE_DATA'
    }

