import os

GIZMO_FOLDER = "/Users/anthony/code_projects/cb_nuke/gizmos"

for root, dirs, files in os.walk(GIZMO_FOLDER):
    print(root)
    print(dirs)
    print(files)


class GizmoItem():
    def __init__(self):
        pass
