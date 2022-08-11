from bpy.props import FloatProperty, BoolProperty, StringProperty
from ..swivelmeta_component import SwivelMetaComponent
from ..types import Category, PanelType, NodeType


class ShopifyProductModel(SwivelMetaComponent):
    _definition = {
        'name': 'shopify-product-model',
        'display_name': 'Shopify Product Model',
        'category': Category.ECOMMERCE,
        'node_type': NodeType.NODE,
        'panel_type': [PanelType.OBJECT],
        'icon': 'SCENE_DATA'
    }

    centerModel: BoolProperty(
        name="Center model",
        description="Center the product model based on its bounding box",
        default=True
    )

    alignWithBase: BoolProperty(
        name="Align with base",
        description="Reposition the product model vertically so that it sits on top of the display",
        default=True
    )

    scaleToBounds: BoolProperty(
        name="Scale to bounds",
        description="Scale model up or down to fit given dimension",
        default=True
    )

    dimension: FloatProperty(
        name="Dimension",
        description="If scale to bounds is checked, determines the size a model should be",
        default=1.0,
        min=0.01
    )

    url: StringProperty(
        name="Default model URL",
        description="URL for placeholder glb/gltf (optional)",
        default=""
    )