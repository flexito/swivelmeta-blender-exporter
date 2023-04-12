from ..swivelmeta_component import SwivelMetaComponent
from ..types import Category, PanelType, NodeType
from bpy.props import StringProperty, FloatVectorProperty, FloatProperty


class Hyperbeam(SwivelMetaComponent):
    _definition = {
        'name': 'presenter',
        'display_name': 'Presenter',
        'category': Category.EXPERIMENTAL,
        'node_type': NodeType.NODE,
        'panel_type': [PanelType.OBJECT],
        'icon': 'USER'
    }

    id: StringProperty(
        name="Presenter ID",
        description="Unique ID for presenter",
        default=""
    )

    uiLocation: FloatVectorProperty(
        name="UI Location",
        description="Location for UI panel",
        unit='LENGTH',
        subtype="XYZ",
        default=(0.0, 0.0, 0.0))

    uiRotation: FloatProperty(
        name="UI Rotation",
        description="UI panel rotation",
        subtype="ANGLE",
        default=0.0,
        min=0.0,
        max=360.0)
