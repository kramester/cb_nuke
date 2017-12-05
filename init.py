import os
import nuke
import nuke_tools.formats
from nuke_tools.gizmo_util import GizmoLibrary

studio_gizmos = GizmoLibrary.library_from_path(os.getenv('NUKE_GIZMO_PATH'))
studio_gizmos.load_library()

# install customizations
nuke_tools.formats.install()

print("Loaded CB init.py")
