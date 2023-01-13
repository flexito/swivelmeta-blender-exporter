from bpy.props import StringProperty
from ..swivelmeta_component import SwivelMetaComponent
from ..types import Category, PanelType, NodeType


class Model(SwivelMetaComponent):
    _definition = {
        'name': 'model',
        'display_name': '3d Model',
        'category': Category.MEDIA,
        'node_type': NodeType.NODE,
        'panel_type': [PanelType.OBJECT],
        'icon': 'MESH_MONKEY'
    }

    src: StringProperty(
        name="Source",
        description="Source URL for GLB model",
        default=""
    )
