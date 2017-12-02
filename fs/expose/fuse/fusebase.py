import os
from fs.base import *
__all__ = ['flags_to_mode']
def flags_to_mode(flags, binary=True):
    """Convert an os.O_* flag bitmask into an FS mode string."""
    if flags & os.O_WRONLY:
        if flags & os.O_TRUNC:
            mode = "w"
        elif flags & os.O_APPEND:
            mode = "a"
        else:
            mode = "r+"
    elif flags & os.O_RDWR:
        if flags & os.O_TRUNC:
            mode = "w+"
        elif flags & os.O_APPEND:
            mode = "a+"
        else:
            mode = "r+"
    else:
        mode = "r"
    if flags & os.O_EXCL:
        mode += "x"
    if binary:
        mode += 'b'
    else:
        mode += 't'
    return mode
