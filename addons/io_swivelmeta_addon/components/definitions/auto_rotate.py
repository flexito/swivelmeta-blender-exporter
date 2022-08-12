from bpy.props import FloatVectorProperty
from ..swivelmeta_component import SwivelMetaComponent
from ..types import Category, PanelType, NodeType


class AutoRotate(SwivelMetaComponent):
    _definition = {
        'name': 'auto-rotate',
        'display_name': 'Auto Rotate',
        'category': Category.ANIMATION,
        'node_type': NodeType.NODE,
        'panel_type': [PanelType.OBJECT],
        'icon': 'ORIENTATION_GIMBAL'
    }

    rotationSpeed: FloatVectorProperty(
        name="Rotation speed",
        description="Sets rotation speed in Blender coordinates",
        size=3,
        subtype="XYZ",
        default=[0, 0, 0.1]
    )

