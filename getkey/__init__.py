# -*- coding: utf-8 -*-
# Initially taken from:
# http://code.activestate.com/recipes/134892/
# Thanks to Danny Yoo

from __future__ import absolute_import, print_function
import sys
from contextlib import contextmanager
import codecs
import locale
import os
import sys
from .keynames import PLATFORM_KEYS


__version__ = '0.6.5'


class GetKeyException(Exception):
    """Raised by the code in this getkey module. If getkey ever raises
    an exception that isn't GetKeyException, you can assume it's caused
    by a bug in the getkey module."""
    pass


class PlatformUnix(object):
    def __init__(self):
        self.keys = PLATFORM_KEYS['unix']

        try:
            self.__decoded_stream = OSReadWrapper()
        except Exception as err:
            raise GetKeyException('Cannot use unix platform on non-file-like stream')

    def getkey(self, blocking=True):
        buffer = ''
        for c in self.getchars(blocking):
            buffer += c
            if buffer not in self.keys.escapes:
                break

        keycode = self.keys.canon(buffer)
        if keycode == '\x03':
            raise KeyboardInterrupt
        return keycode

    def fileno(self):
        return self.__decoded_stream.fileno()

    @contextmanager
    def context(self):
        fd = self.fileno()
        old_settings = termios.tcgetattr(fd)
        tty.setcbreak(fd)
        try:
            yield
        finally:
            termios.tcsetattr(
                fd, termios.TCSADRAIN, old_settings
            )

    def getchars(self, blocking=True):
        """Get characters on Unix."""
        with self.context():
            if blocking:
                yield self.__decoded_stream.read(1)
            while select.select([self.fileno()], [], [], 0)[0]:
                yield self.__decoded_stream.read(1)


class OSReadWrapper(object):
    """Wrap os.read binary input with encoding in standard stream interface.

    We need this since os.read works more consistently on unix, but only
    returns byte strings.  Since the user might be typing on an international
    keyboard or pasting unicode, we need to decode that.  Fortunately
    python's stdin has the fileno & encoding attached to it, so we can
    just use that.
    """
    def __init__(self):
        self.__decoder = codecs.getincrementaldecoder(sys.stdin.encoding)()

    def fileno(self):
        return sys.stdin.fileno()

    @property
    def buffer(self):
        return sys.stdin.buffer

    def read(self, chars):
        buffer = ''
        while len(buffer) < chars:
            buffer += self.__decoder.decode(os.read(sys.stdin.fileno(), 1))
        return buffer


class PlatformWindows(object):
    def __init__(self):
        self.keys = PLATFORM_KEYS['windows']

    def getkey(self, blocking=True):
        buffer = ''
        for c in self.getchars(blocking):
            buffer += c.decode(encoding=locale.getpreferredencoding())
            if buffer not in self.keys.escapes:
                break

        keycode = self.keys.canon(buffer)
        if keycode == '\x03':
            raise KeyboardInterrupt
        return keycode

    def getchars(self, blocking=True):
        """Get characters on Windows."""

        if blocking:
            yield msvcrt.getch()
        while msvcrt.kbhit():
            yield msvcrt.getch()


if sys.platform.startswith('linux') or sys.platform.startswith('darwin'):
    import select
    import tty
    import termios
    __platform = PlatformUnix()
elif sys.platform.startswith('win32'):
    import msvcrt
    __platform = PlatformWindows()
elif sys.platform.startswith('cygwin'):
    try:
        import msvcrt
    except ImportError:
        __platform = PlatformUnix(*args, **kwargs)
    else:
        __platform = PlatformWindows(*args, **kwargs)
else:
    raise GetKeyException('Unknown platform {!r}'.format(sys.platform))

getkey = __platform.getkey
keys = __platform.keys



