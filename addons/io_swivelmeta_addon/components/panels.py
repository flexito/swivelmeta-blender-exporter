import bpy
from .types import PanelType
from .components_registry import get_component_by_name, get_components_registry
from .utils import get_object_source, dash_to_title


def draw_component_global(panel, context):
    layout = panel.layout
    panel_type = PanelType(panel.bl_context)
    components_registry = get_components_registry()
    for _, component_class in components_registry.items():
        component_class.draw_global(context, layout, panel_type)


def draw_component(panel, context, obj, row, component_item):
    component_name = component_item.name
    component_class = get_component_by_name(component_name)
    if component_class:
        panel_type = PanelType(panel.bl_context)
        if not panel_type in component_class.get_panel_type():
            return

        component_id = component_class.get_id()
        component = getattr(obj, component_id)

        has_properties = len(component_class.get_properties()) > 0

        col = row.box().column()
        top_row = col.row()

        if has_properties:
            top_row.prop(component_item, "expanded",
                         icon="TRIA_DOWN" if component_item.expanded else "TRIA_RIGHT",
                         icon_only=True, emboss=False
                         )

        display_name = component_class.get_display_name(
            dash_to_title(component_id))

        top_row.label(text=display_name)

        if not component_class.is_dep_only():
            remove_component_operator = top_row.operator(
                "wm.remove_swivelmeta_component",
                text="",
                icon="X"
            )
            remove_component_operator.component_name = component_name
            remove_component_operator.panel_type = panel.bl_context

        if has_properties and component_item.expanded:
            component.draw(context, col, panel_type)

    else:
        col = row.box().column()
        top_row = col.row()
        top_row.label(
            text=f"Unknown component '{component_name}'", icon="ERROR")
        remove_component_operator = top_row.operator(
            "wm.remove_swivelmeta_component",
            text="",
            icon="X"
        )
        remove_component_operator.component_name = component_name
        remove_component_operator.panel_type = panel.bl_context


def draw_components_list(panel, context):
    layout = panel.layout

    obj = get_object_source(context, panel.bl_context)

    if not obj:
        return

    add_component_operator = layout.operator(
        "wm.add_swivelmeta_component",
        text="Add Component",
        icon="ADD"
    )
    add_component_operator.panel_type = panel.bl_context

    for component_item in obj.swivelmeta_component_list.items:
        row = layout.row()
        draw_component(panel, context, obj, row, component_item)

    layout.separator()


class SwivelMetaObjectPanel(bpy.types.Panel):
    bl_label = "SwivelMeta"
    bl_idname = "OBJECT_PT_swivelmeta"
    bl_space_type = 'PROPERTIES'
    bl_region_type = 'WINDOW'
    bl_context = "object"

    def draw(self, context):
        draw_components_list(self, context)


class SwivelMetaScenePanel(bpy.types.Panel):
    bl_label = 'SwivelMeta'
    bl_idname = "SCENE_PT_swivelmeta"
    bl_space_type = 'PROPERTIES'
    bl_region_type = 'WINDOW'
    bl_context = 'scene'

    def draw(self, context):
        draw_component_global(self, context)
        layout = self.layout
        layout.separator()
        draw_components_list(self, context)


class SwivelMetaMaterialPanel(bpy.types.Panel):
    bl_label = 'SwivelMeta'
    bl_idname = "MATERIAL_PT_swivelmeta"
    bl_space_type = 'PROPERTIES'
    bl_region_type = 'WINDOW'
    bl_context = 'material'

    def draw(self, context):
        draw_components_list(self, context)


class SwivelMetaBonePanel(bpy.types.Panel):
    bl_label = "SwivelMeta"
    bl_idname = "BONE_PT_swivelmeta"
    bl_space_type = 'PROPERTIES'
    bl_region_type = 'WINDOW'
    bl_context = "bone"

    def draw(self, context):
        draw_components_list(self, context)


def register():
    bpy.utils.register_class(SwivelMetaObjectPanel)
    bpy.utils.register_class(SwivelMetaScenePanel)
    bpy.utils.register_class(SwivelMetaMaterialPanel)
    bpy.utils.register_class(SwivelMetaBonePanel)


def unregister():
    bpy.utils.unregister_class(SwivelMetaObjectPanel)
    bpy.utils.unregister_class(SwivelMetaScenePanel)
    bpy.utils.unregister_class(SwivelMetaMaterialPanel)
    bpy.utils.unregister_class(SwivelMetaBonePanel)
