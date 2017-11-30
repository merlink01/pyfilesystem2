import time
from fs.memoryfs import MemoryFS
from fs.expose import dokan
fs = MemoryFS()

mp = dokan.mount(fs, 'Q:\\', fsname='TestFS', volname='TestDrive',)
print (mp.path)

try:
    while 1:
        time.sleep(1)
except:

    mp.unmount()
mp.unmount()