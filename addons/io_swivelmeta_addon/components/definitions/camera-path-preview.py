from ..swivelmeta_component import SwivelMetaComponent
from ..types import Category, PanelType, NodeType
from bpy.props import PointerProperty
from bpy.types import Object


class CameraPathPreview(SwivelMetaComponent):
    _definition = {
        'name': 'camera-path-preview',
        'display_name': 'Camera Path Preview',
        'category': Category.UTILITIES,
        'node_type': NodeType.NODE,
        'panel_type': [PanelType.OBJECT],
        'icon': 'CAMERA_DATA'
    }

    camera: PointerProperty(
        name="Camera",
        description="Animated camera to preview",
        type=Object
    )
