import nuke
import nuke_tools.formats

# add paths so nuke loads gizmos and icons
nuke.pluginAddPath('./gizmos')
nuke.pluginAddPath('./icons')

# install customizations
nuke_tools.formats.install()

print("Loaded CB init.py")
