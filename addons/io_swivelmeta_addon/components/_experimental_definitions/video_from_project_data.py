from ..swivelmeta_component import SwivelMetaComponent
from ..types import Category, PanelType, NodeType

class VideoFromProjectData(SwivelMetaComponent):
    _definition = {
        'name': 'video-from-project-data',
        'display_name': 'Video From Project Data',
        'category': Category.MEDIA,
        'node_type': NodeType.NODE,
        'panel_type': [PanelType.OBJECT],
        'icon': 'FILE_MOVIE'
    }

