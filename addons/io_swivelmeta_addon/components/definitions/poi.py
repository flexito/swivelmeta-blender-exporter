from ..swivelmeta_component import SwivelMetaComponent
from ..types import Category, PanelType, NodeType
from bpy.props import IntProperty, StringProperty, FloatProperty, BoolProperty, PointerProperty
from bpy.types import Object


class PointOfInterest(SwivelMetaComponent):
    _definition = {
        'name': 'poi',
        'display_name': 'Point of Interest',
        'category': Category.NAVIGATION,
        'node_type': NodeType.NODE,
        'panel_type': [PanelType.OBJECT],
        'icon': 'PINNED'
    }

    index: IntProperty(
        name="Index",
        description="Which order to play and/or display this POI",
        default=1,
        min=1
    )

    showInUI: BoolProperty(
        name="Show in UI",
        description="If true, displays this POI in the UI",
        default=True
    )

    includeInAutoTour: BoolProperty(
        name="Include in Autotour",
        description="If true, will be included in the autotour",
        default=True
    )

    displayName: StringProperty(
        name="Display Name",
        description="Name to be displayed in UI"
    )

    delay: FloatProperty(
        name="Delay",
        description="Delay in seconds before advancing to next POI",
        default=1.0,
        min=0.0
    )

    speed: FloatProperty(
        name="Speed",
        description="Sets to the speed (meters per second) at which the user travels TO this POI.",
        default=5.0,
        min=0.5
    )

    requireAction: BoolProperty(
        name="Require Action",
        description="If true, requires user to click a button in order to advance",
        default=False
    )

    endAutoTour: BoolProperty(
        name="End Autotour",
        description="If true, this POI will stop the autotour completely and prevent it from looping.",
        default=False
    )
