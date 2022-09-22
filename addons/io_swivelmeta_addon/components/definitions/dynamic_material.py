from bpy.props import StringProperty, FloatProperty, FloatVectorProperty
from ..swivelmeta_component import SwivelMetaComponent
from ..types import Category, PanelType, NodeType


class DynamicMaterial(SwivelMetaComponent):
    _definition = {
        'name': 'dynamic-material',
        'display_name': 'Dynamic Material',
        'category': Category.DYNAMIC_CONTENT,
        'node_type': NodeType.NODE,
        'panel_type': [PanelType.OBJECT],
        'icon': 'MATERIAL_DATA'
    }

    name: StringProperty(
        name="Name",
        description="Name of material as shown in SwivelMeta Builder app",
        default=""
    )

    description: StringProperty(
        name="Description",
        description="Description of material as shown in SwivelMeta Builder app",
        default=""
    )
