from bpy.props import FloatProperty, StringProperty
from ..swivelmeta_component import SwivelMetaComponent
from ..types import Category, PanelType, NodeType


class AvatarAnimationTrigger(SwivelMetaComponent):
    _definition = {
        'name': 'avatar-animation-trigger',
        'display_name': 'Avatar Animation Trigger',
        'category': Category.AVATAR,
        'node_type': NodeType.NODE,
        'panel_type': [PanelType.OBJECT],
        'icon': 'ARMATURE_DATA'
    }

    action: StringProperty(name="Action Prefix", description="Plays all actions with this prefix when avatar enters given radius",
                         default="anim-prefix")
    
    radius: FloatProperty(name="Radius",
                         description="Radius",
                         default=1.0)

