from __future__ import absolute_import, print_function
import sys
from .platforms import GetKeyException, PlatformUnix, PlatformWindows, windows_or_unix

if sys.platform.startswith('linux') or sys.platform.startswith('darwin'):
    __platform = PlatformUnix()
elif sys.platform.startswith('win32'):
    __platform = PlatformWindows()
elif sys.platform.startswith('cygwin'):
    __platform = windows_or_unix()
else:
    raise GetKeyException('Unknown platform {!r}'.format(sys.platform))

getkey = __platform.getkey
keys = __platform.keys
bang = __platform.bang

__version__ = '0.6.5'
