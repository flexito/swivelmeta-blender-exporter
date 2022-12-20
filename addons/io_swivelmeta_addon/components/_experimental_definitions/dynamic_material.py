from bpy.props import StringProperty, FloatProperty, FloatVectorProperty, PointerProperty
from bpy.types import Material
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

    id: StringProperty(
        name="ID",
        description="Unique identifier for use in the SwivelMeta Mixer app. Should only contain alphanumeric characters",
        default=""
    )

    name: StringProperty(
        name="Name",
        description="Name of material as shown in SwivelMeta Mixer app",
        default=""
    )

    description: StringProperty(
        name="Description",
        description="Description of material as shown in SwivelMeta Mixer app",
        default=""
    )

    proxyMaterial: PointerProperty(
        name="Proxy Material",
        description="Material to be configured in the SwivelMeta Mixer app",
        type=Material
    )
