import os
from os import listdir
from os.path import isfile, join
import random

path = os.path.dirname(os.path.abspath(__file__))
onlyfiles = [f for f in listdir(path) if isfile(join(path, f))]

audio = path + '/' + random.choice(onlyfiles)

from subprocess import call
call(['play', '-v', '5', audio])
