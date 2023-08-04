from ..swivelmeta_component import SwivelMetaComponent
from ..types import Category, PanelType, NodeType
from bpy.props import BoolProperty


class UserVisibility(SwivelMetaComponent):
    _definition = {
        'name': 'user-visibility',
        'display_name': 'User Visibility',
        'category': Category.APPLICATION,
        'node_type': NodeType.NODE,
        'panel_type': [PanelType.OBJECT],
        'icon': 'OBJECT_HIDDEN'
    }

    visibleForOwners: BoolProperty(
        name="Visible for Owners",
        description="Object is visible for designated owners",
        default=True
    )

    visibleForNonowners: BoolProperty(
        name="Visible for Non-owners",
        description="Object is visible for users not designated as owners",
        default=True
    )
