from ..swivelmeta_component import SwivelMetaComponent
from ..types import Category, PanelType, NodeType
from bpy.props import PointerProperty
from bpy.types import Object


class DynamicNavMesh(SwivelMetaComponent):
    _definition = {
        'name': 'dynamic-nav-mesh',
        'display_name': 'Dynamic Nav Mesh',
        'category': Category.MATERIAL,
        'node_type': NodeType.NODE,
        'panel_type': [PanelType.OBJECT],
        'icon': 'DUPLICATE'
    }

    sourceObject: PointerProperty(
        name="Nav Mesh",
        description="Nav mesh to use when triggered",
        type=Object
    )
