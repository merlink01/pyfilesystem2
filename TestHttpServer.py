import time
from fs.memoryfs import MemoryFS
from fs.osfs import OSFS
from fs.expose import httpserver
#~ fs = MemoryFS()
fs = OSFS('~/')

httpserver.run(fs)
