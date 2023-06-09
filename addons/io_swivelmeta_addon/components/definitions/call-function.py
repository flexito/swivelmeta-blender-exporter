from ..swivelmeta_component import SwivelMetaComponent
from ..types import Category, PanelType, NodeType
from bpy.props import EnumProperty, FloatProperty
from bpy.types import Object


class CallFunction(SwivelMetaComponent):
    _definition = {
        'name': 'call-function',
        'display_name': 'Call Function',
        'category': Category.APPLICATION,
        'node_type': NodeType.NODE,
        'panel_type': [PanelType.OBJECT],
        'icon': 'CONSOLE'
    }

    functionCall: EnumProperty(
        name="Function",
        description="Which function this trigger should call",
        items=[("SHARE_SCREEN", "Share Screen", "Calls the share screen function"),
               ("SHARE_WEBCAM", "Share Webcam", "Calls the webcam feature"),
               ("INVITE", "Invite", "Invite friend to space")],
        default="SHARE_SCREEN")

    triggerType: EnumProperty(
        name="Trigger Type",
        description="Select type of trigger",
        items=[("PROXIMITY", "Proximity", "Will trigger when user gets close to this object"),
               ("CLICKABLE", "Clickable", "Will trigger when user clicks this object")],
        default="CLICKABLE")

    proximityDistance: FloatProperty(
        name="Proximity Distance",
        description="Distance from object's origin before teleport is triggered",
        default=1.0,
        min=0.0
    )
