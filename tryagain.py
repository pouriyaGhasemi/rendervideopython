from datetime import datetime, timedelta
from os import remove, path, makedirs, chdir
import sys
dir_path = path.dirname(path.realpath(__file__))
chdir(dir_path)
from models import WhatToDo

jobs = WhatToDo.filter(done=0,IsRendering=1,TryToRender=1).order_by(WhatToDo.insertDateTime)
count = jobs.count()
print("app starting. {} jobs to left".format(count))
for job in jobs:
    job.IsRendering = 0
    job.TryToRender=2
    job.done=2
    job.save()

jobs = WhatToDo.filter(done=0,IsRendering=1,TryToRender=0).order_by(WhatToDo.insertDateTime)
count = jobs.count()
print("app starting. {} jobs to left".format(count))
for job in jobs:
    job.IsRendering = 0
    job.TryToRender=1
    job.save()
