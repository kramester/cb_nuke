import os
import re
try:
    import nuke
except:
    pass


def library_from_path(path):
    path = os.path.abspath(path)
    glibrary = []
    for root, dirs, files in os.walk(path):
        if files:
            gdict = {}
            r = re.compile(r'.+\.gizmo$')
            gfiles = filter(r.match, files)
            gdict['files'] = sorted(gfiles)
            gdict['plugin_path'] = root
            gdict['folder'] = os.path.relpath(root, path)
            glibrary.append(gdict)
        else:
            pass
    return glibrary


def load_library(glibrary):
    for gdict in glibrary:
        nuke.pluginAddPath(gdict['plugin_path'])


def add_libary_to_menu(glibrary, root_menu):
    for gdict in glibrary:
        for gfile in gdict['files']:
            fname, fext = os.path.splitext(gfile)
            root_menu.addCommand('{}/{}'.format(gdict['folder'], fname), 'nuke.createNode(\'{}\')'.format(gfile), icon=None)


class GizmoVersioned():
    def __init__(self):
        pass
