from __future__ import absolute_import, print_function
import sys
from .platforms import GetKeyException, PlatformUnix, PlatformWindows, windows_or_unix

def platform():
    if sys.platform.startswith('linux') or sys.platform.startswith('darwin'):
        return PlatformUnix()
    elif sys.platform.startswith('win32'):
        return PlatformWindows()
    elif sys.platform.startswith('cygwin'):
        return windows_or_unix()
    else:
        raise GetKeyException('Unknown platform {!r}'.format(sys.platform))


__platform = platform()

getkey = __platform.getkey
keys = __platform.keys
key = keys  # alias
bang = __platform.bang

__version__ = '0.6.5'
