import time
from fs.memoryfs import MemoryFS
from fs.expose import fuse
fs = MemoryFS()

mp = fuse.mount(fs, '/home/merlink/fusemount/'.encode())
print (mp.path)

try:
    while 1:
        time.sleep(1)
except:

    mp.unmount()
mp.unmount()
