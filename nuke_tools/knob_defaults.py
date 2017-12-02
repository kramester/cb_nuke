"""Defines knob defaults
"""

import nuke


def install():

    # Root defaults
    nuke.knobDefault("Root.format", "hd")
    # nuke.knobDefault("Root.OCIO_config", "spi-vfx")

    # Random Node Defaults
    nuke.knobDefault("EXPTool.mode", "0")
    nuke.knobDefault("Project3D.crop", "false")
    nuke.knobDefault("Grain2.maskgrain", "false")
    nuke.knobDefault("Viewer.frame_increment", "8")
    nuke.knobDefault("Transform.shutteroffset", "centered")
    nuke.knobDefault("Tracker4.shutteroffset", "centered")
    nuke.knobDefault("CornerPin2D.shutteroffset", "centered")
    nuke.knobDefault("Tracker4.cornerPinOptions", "Transform (match-move)")
    nuke.knobDefault("Reformat.resize", "none")
    nuke.knobDefault("Reformat.pbb", "true")

    # Because lots of nodes in nuke default to ALL channels
    nuke.knobDefault("Blur.channels", "rgba")
    nuke.knobDefault("Defocus.channels", "rgba")
    nuke.knobDefault("ZDefocus.channels", "rgba")
    nuke.knobDefault("Sharpen.channels", "rgba")

    # Keylight defaults
    nuke.knobDefault("Keylight.screenReplaceMethod", "Source")
    nuke.knobDefault("Keylight.insideReplaceMethod", "Source")
    nuke.knobDefault("Keylight.insideComponent", "Alpha")
    nuke.knobDefault("Keylight.outsideComponent", "Inverted Alpha")

    # Write defaults
    nuke.knobDefault("Write.channels", "rgba")
