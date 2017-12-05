import os
import re
import nuke


# def library_from_path(path):
#     path = os.path.abspath(path)
#     glibrary = []
#     for root, dirs, files in os.walk(path):
#         if files:
#             gdict = {}
#             r = re.compile(r'.+\.gizmo$')
#             gfiles = filter(r.match, files)
#             gdict['files'] = sorted(gfiles)
#             gdict['plugin_path'] = root
#             gdict['folder'] = os.path.relpath(root, path)
#             glibrary.append(gdict)
#         else:
#             pass
#     return glibrary
#
#
# def load_library(glibrary):
#     for gdict in glibrary:
#         nuke.pluginAddPath(gdict['plugin_path'])
#
#
# def add_libary_to_menu(glibrary, root_menu):
#     for gdict in glibrary:
#         for gfile in gdict['files']:
#             fname, fext = os.path.splitext(gfile)
#             root_menu.addCommand('{}/{}'.format(gdict['folder'], fname), 'nuke.createNode(\'{}\')'.format(gfile), icon='{}.png'.format(fname))


class GizmoLibrary:
    def __init__(self, plugin_paths, gizmo_menu_items):
        # default contructor
        if isinstance(plugin_paths, list):
            self.plugin_paths = plugin_paths
        else:
            self.plugin_paths = [plugin_paths]

        if isinstance(gizmo_menu_items, list):
            self.gizmo_menu_items = gizmo_menu_items
        else:
            self.gizmo_menu_items = [gizmo_menu_items]
        for item in self.gizmo_menu_items:
            if not isinstance(item, GizmoMenuItem):
                raise ValueError('gizmo_menu_items must be a list of GizmoMenuItem objects')

    @classmethod
    def library_from_path(cls, path):
        # alternative constructor for gizmo libaray
        path = os.path.abspath(path)
        plugin_paths = []
        gizmo_menu_items = []
        for root, dirs, files in os.walk(path):
            if files:
                # if there are files in the path, store the plugin_path for loading
                plugin_paths.append(root)
                # filter out only .gizmo files for the menu
                r = re.compile(r'.+\.gizmo$')
                gfiles = filter(r.match, files)
                # group versioned gizmos together into 1 menu entry
                gdict = cls.group_versions(sorted(gfiles))
                # get the realtive path for submenu creation
                submenu = os.path.relpath(root, path)
                for name, versions in gdict.iteritems():
                    # store the matching icon if file exists
                    icon = os.path.join(root, '{}.png'.format(name))
                    if not os.path.exists(icon):
                        icon = None
                    gizmo_item = GizmoMenuItem(name, versions, submenu, icon=icon)
                    gizmo_menu_items.append(gizmo_item)
            # if there are no files, go to next path in walk
            else:
                pass
        return cls(plugin_paths, gizmo_menu_items)

    @classmethod
    def group_versions(self, versions):
        # groups versioned filenames by basename
        group = {}
        r = re.compile(r"(_v\d+)?(\..*)")
        for f in versions:
            group.setdefault(r.sub("", f), []).append(f)
        return group

    def load_library(self):
        # load all the plugin paths into nuke, can use this in init.py to load without building menus
        for path in self.plugin_paths:
            nuke.pluginAddPath(path)

    def add_library_to_menu(self, root_menu, default_icon=None):
        # adds the gizmo libaray to the menu
        for gizmo in self.gizmo_menu_items:
            if isinstance(gizmo, GizmoMenuItem):
                fullname = os.path.join(gizmo.submenu, gizmo.name)
                # for windows, replace backslashes with forwardslashes
                # fullname.replace('\\\\', '/').replace('\\', '/')
                if not gizmo.icon:
                    gizmo.icon = default_icon
                # if theres only 1 version, just use that one
                if len(gizmo.versions) == 1:
                    version = gizmo.versions[0]
                else:
                    # if version set to latest, use last gizmo in version list
                    if gizmo.use_version == 'latest':
                        version = gizmo.versions[-1]
                    # if a specific version is specified, try to get that one
                    else:
                        r = re.compile(r".*(_v(\d+))\..*")
                        for v in gizmo.versions:
                            match = r.match(v)
                            if int(match.group(2)) == int(gizmo.use_version):
                                version = v
                                break
                # finally, add the gizmo to the specified nuke menu
                root_menu.addCommand(fullname, 'nuke.createNode(\'{}\')'.format(version), icon=gizmo.icon, shortcut=gizmo.shortcut, tooltip=gizmo.tooltip)

    def find_gizmo_item(self, name):
        # returns the gizmo item from the library
        for gizmo in self.gizmo_menu_items:
            if gizmo.name == name:
                return gizmo


class GizmoMenuItem:
    def __init__(self, name, versions, submenu, use_version='latest', shortcut=None, icon=None, tooltip=''):
        self.name = name
        self.submenu = submenu
        self.versions = versions
        self.use_version = use_version
        self.shortcut = shortcut
        self.icon = icon
        self.tooltip = tooltip

    def set_name(self, name):
        self.name = str(name)

    def set_icon(self, icon):
        self.icon = str(icon)

    def set_tooltip(self, tooltip):
        self.tooltip = str(tooltip)

    def set_version(self, version):
        self.use_version = version

    def set_shortcut(self, shortcut):
        self.shortcut = str(shortcut)

    def set_submenu(self, submenu):
        self.submenu = str(submenu)
