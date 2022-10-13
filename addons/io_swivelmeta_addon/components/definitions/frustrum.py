from bpy.props import BoolProperty
from ..swivelmeta_component import SwivelMetaComponent
from ..types import Category, PanelType, NodeType


class Frustrum(SwivelMetaComponent):
    _definition = {
        'name': 'frustrum',
        'display_name': 'Frustum',
        'category': Category.OBJECT,
        'node_type': NodeType.NODE,
        'panel_type': [PanelType.OBJECT],
        'icon': 'IMAGE_PLANE'
    }

    culled: BoolProperty(
        name="Culled", description="Ignore entities outside of the camera frustrum. Frustrum culling can cause problems with some animations", default=True)
