from ..swivelmeta_component import SwivelMetaComponent
from ..types import Category, PanelType, NodeType
from .networked import migrate_networked
from bpy.props import StringProperty, FloatVectorProperty, FloatProperty, BoolProperty


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

    showUI: BoolProperty(
        name="Show UI",
        description="Show full avatar control UI",
        default=False)

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

    @classmethod
    def migrate(cls, version):
        migrate_networked(cls.get_name())
