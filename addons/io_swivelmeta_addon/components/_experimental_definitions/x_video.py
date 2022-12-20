from bpy.props import BoolProperty, EnumProperty, StringProperty
from ..swivelmeta_component import SwivelMetaComponent
from ..types import Category, PanelType, NodeType
from ..consts import PROJECTION_MODE


class LocalVideo(SwivelMetaComponent):
    _definition = {
        'name': 'local-video',
        'display_name': 'Local Video',
        'category': Category.MEDIA,
        'node_type': NodeType.NODE,
        'panel_type': [PanelType.OBJECT, PanelType.BONE],
        'deps': ['audio-params'],
        'icon': 'FILE_MOVIE'
    }

    src: StringProperty(
        name="Video URL",
        description="Video URL",
        default="https://"
    )

    projection: EnumProperty(
        name="Projection",
        description="Projection",
        items=PROJECTION_MODE,
        default="flat"
    )

    autoPlay: BoolProperty(
        name="Auto Play",
        description="Auto Play",
        default=True
    )

    controls: BoolProperty(
        name="Show controls",
        description="Show Controls",
        default=True
    )

    loop: BoolProperty(
        name="Loop",
        description="Loop",
        default=True
    )
