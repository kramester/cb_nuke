import re

file_list = [
    "ThisFile_v01.ext",
    "ThisFile_v02.ext",
    "ThatFile_v01.ext",
    "ThatFile_v02.ext",
    "NonVersionedFile.ext",
    "Non_VersionedFile.ext",
]


r = re.compile(r".*(_v(\d+))\..*")
for f in file_list:
    match = r.match(f)
    print int(match.group(2))
    print(f)
    # if int(match.group(2)) == int(gizmo.use_version):


def group_versions(lst):
    group = {}
    r = re.compile(r"(_v\d+)?(\..*)")
    for f in file_list:
        # match = reg.match(f)
        res.setdefault(r.sub("", f), []).append(f)
    return res


# group_items(file_list)
