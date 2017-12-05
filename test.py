import uuid
from md5 import md5

print md5(str(uuid.uuid4())).hexdigest()

import uuid
print str(uuid.uuid4()).split('-')[0]
