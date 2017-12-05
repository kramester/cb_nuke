"""Adds custom nodes, plugins, and tools to the menus.
"""
import nuke
import viewer_util
import node_util
import settings
from gizmo_util import GizmoLibrary

# default menu icon for all non-vanilla nuke menu items
nuke.pluginAddPath('./icons')
DEFAULT_MENU_ICON = 'cb_icon.png'

# define menu locations
nuke_menu = nuke.menu('Nuke')
node_menu = nuke.menu('Nodes')
toolsets_menu = node_menu.findItem('ToolSets')
cb_menu = nuke_menu.addMenu('ChickenBone')

# checks nuke version because they changed the name of recent files in menu
if nuke.NUKE_VERSION_MAJOR < 9:
    recent_menu_item = "_&Recent Files"
else:
    recent_menu_item = "Open Recent Comp"


def install():
    """Adds custom menu items"""

    # Appends more recent files to recent file menu. By deafult nuke only shows last 6 files
    for i in range(7, 10):
        nuke_menu.addCommand("File/{}/@recent_file{}".format(recent_menu_item, i),
                             "nuke.scriptOpen(nuke.recentFile({}))".format(i), "#+{}".format(i))
    for i in range(10, 21):
        nuke_menu.addCommand("File/{}/@recent_file{}".format(recent_menu_item, i),
                             "nuke.scriptOpen(nuke.recentFile({}))".format(i))

    # Viewer menu items
    nuke_menu.findItem('Viewer').addSeparator()
    nuke_menu.addCommand('Viewer/Stop Up', viewer_util.viewer_stop_up, '^Up', icon=DEFAULT_MENU_ICON)
    nuke_menu.addCommand('Viewer/Stop Down', viewer_util.viewer_stop_down, '^Down', icon=DEFAULT_MENU_ICON)
    nuke_menu.addCommand('Viewer/Reset', viewer_util.viewer_stop_reset, '^Home', icon=DEFAULT_MENU_ICON)
    nuke_menu.findItem('Viewer').addSeparator()
    nuke_menu.addCommand('Viewer/Cycle Viewer LUTs', viewer_util.toggle_viewer_lut, '+v', icon=DEFAULT_MENU_ICON)
    nuke_menu.addCommand('Viewer/VIEWER_INPUT/Cycle Masks', node_util.cycle_viewer_input_masks, '^m', icon=DEFAULT_MENU_ICON)

    # Edit menu items
    nuke_menu.addCommand('Edit/Paste', node_util.paste_to_selected, '^v', index=12, icon=DEFAULT_MENU_ICON)
    nuke_menu.findItem('Edit/Node').addSeparator()
    nuke_menu.addCommand('Edit/Node/Label Selected Nodes...', node_util.label_dialog, '^l', icon=DEFAULT_MENU_ICON)
    nuke_menu.addCommand('Edit/Node/GUI Disable\/Enable...', node_util.gui_disable, '^d', icon=DEFAULT_MENU_ICON)

    # Node Menu
    node_menu.addCommand('Transform/Transform', "nuke_tools.node_util.context_aware_create_node('Transform', 'TransformGeo', 'DeepTransform')", 't', icon="2D.png")
    node_menu.addCommand('Merge/Merge', "nuke_tools.node_util.context_aware_create_node('Merge2', 'Scene', 'DeepMerge')", 'm', icon="Merge.png")
    node_menu.addCommand('Color/ColorCorrect', "nuke_tools.node_util.context_aware_create_node('ColorCorrect', None, 'DeepColorCorrect')", 'c', icon="ColorCorrect.png")
    node_menu.addCommand('Image/Write', "nuke_tools.node_util.context_aware_create_node('Write', None, 'DeepWrite')", 'w', icon="Write.png")
    node_menu.addCommand('Time/FrameHold', "nuke.createNode('FrameHold')['first_frame'].setValue( nuke.frame() )", icon='FrameHold.png')

    # Gizmos
    studio_gizmos = GizmoLibrary.library_from_path(settings.STUDIO_GIZMO_PATH)
    # these get loaded in the init.py so we dont need to load them here
    # studio_gizmos.load_library()
    studio_gizmos.add_library_to_menu(node_menu, default_icon=DEFAULT_MENU_ICON)
    studio_gizmos.add_library_to_menu(cb_menu, default_icon=DEFAULT_MENU_ICON)
