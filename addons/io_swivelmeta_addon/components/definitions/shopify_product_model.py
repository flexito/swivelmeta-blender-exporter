from bpy.props import FloatProperty, BoolProperty
from ..swivelmeta_component import SwivelMetaComponent
from ..types import Category, PanelType, NodeType


class ShopifyProductModel(SwivelMetaComponent):
    _definition = {
        'name': 'shopify_product_model',
        'display_name': 'Shopify Product Model',
        'category': Category.ECOMMERCE,
        'node_type': NodeType.NODE,
        'panel_type': [PanelType.OBJECT],
        'icon': 'SCENE_DATA'
    }

    resizeToFit: BoolProperty(
        name="Resize To Fit",
        description="Scale model to fit within given radius",
        default=True
    )

    radius: FloatProperty(
        name="Bounding Radius",
        description="Maximum radius of model imported model",
        default=1.0,
        min=0.01
    )