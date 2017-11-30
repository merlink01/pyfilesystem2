from fs.errors import *

from functools import wraps
def convert_fs_errors(func):
    """Function wrapper to convert FSError instances into OSError."""
    @wraps(func)
    def wrapper(*args,**kwds):
        try:
            # ~ print(func,args,kwds)
            return func(*args,**kwds)
        except (ResourceNotFound, e):
            raise OSError(errno.ENOENT,str(e))
        except (ParentDirectoryMissing, e):
            if sys.platform == "win32":
                raise OSError(errno.ESRCH,str(e))
            else:
                raise OSError(errno.ENOENT,str(e))
        except (ResourceInvalid, e):
            raise OSError(errno.EINVAL,str(e))
        except (PermissionDenied, e):
            raise OSError(errno.EACCES,str(e))
        except (ResourceLocked, e):
            if sys.platform == "win32":
                raise WindowsError(32,str(e))
            else:
                raise OSError(errno.EACCES,str(e))
        except (DirectoryNotEmpty, e):
            raise OSError(errno.ENOTEMPTY,str(e))
        except (DestinationExists, e):
            raise OSError(errno.EEXIST,str(e))
        except (StorageSpace, e):
            raise OSError(errno.ENOSPC,str(e))
        except (RemoteConnection, e):
            raise OSError(errno.ENETDOWN,str(e))
        except (Unsupported, e):
            raise OSError(errno.ENOSYS,str(e))
        except (FSError, e):
            raise OSError(errno.EFAULT,str(e))
    return wrapper
