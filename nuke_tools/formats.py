"""Sets up a default list of formats
"""

import nuke
import collections

NUKE_FORMATS = {
    'hd': '1920 1080 1',
    'hhd': '960 540 1',
    'uhd': '3840 2160 1',
    '3qhd': '1280 720 1',
    '2khd': '2048 1152 1',
    '2k21': '2048 1024 1',
    '2kws': '2048 956 1',
    '2kfa': '2048 1556 1',
    '2kam': '2048 1556 2',
    '1kfa': '1024 778 1',
    '1kam': '1024 778 2',
    '2kdci': '2048 1080 1',
    '4kdci': '4096 2160 1',
    '2kac': '2048 1536 1',
    '2kpan': '2048 856 1'
}

# put them in order by format name
NUKE_FORMATS = collections.OrderedDict(sorted(NUKE_FORMATS.items()))


def install():
    for k, v in NUKE_FORMATS.iteritems():
        nuke.addFormat('{0} {1}'.format(v, k))
