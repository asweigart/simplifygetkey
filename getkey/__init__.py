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


class Platform(object):
    def getkey(self, blocking=True):
        buffer = ''
        for c in self.getchars(blocking):
            buffer += c.decode(encoding=locale.getpreferredencoding())
            if buffer not in self.keys.escapes:
                break

        keycode = self.keys.canon(buffer)
        if keycode in self.interrupts:
            interrupt = self.interrupts[keycode]
            if isinstance(interrupt, BaseException) or \
                issubclass(interrupt, BaseException):
                raise interrupt
            else:
                raise NotImplementedError('Unimplemented interrupt: {!r}'
                                          .format(interrupt))
        return keycode

    def bang(self):
        while True:
            code = self.getkey(True)
            name = self.keys.name(code) or '???'
            print('{} = {!r}'.format(name, code))

    # You MUST override at least one of the following
    def getchars(self, blocking=True):
        char = self.getchar(blocking)
        while char:
            yield char
            char = self.getchar(False)

    def getchar(self, blocking=True):
        for char in self.getchars(blocking):
            return char
        else:
            return None


class PlatformUnix(Platform):
    KEYS = 'unix'
    INTERRUPTS = {'CTRL_C': KeyboardInterrupt}

    def __init__(self, keys=None, interrupts=None,
                 stdin=None, select=None, tty=None, termios=None):
        """Make Unix Platform object.

        Arguments:
            keys (Keys): Keys object to use for escapes & names.
            interrupts (dict): Map of keys to interrupt actions
                (Ctrl-C -> KeyboardInterrupt by default)
            stdin (file descriptor): file object to use (stdin by default)
            select (callable): select function (select.select by default)
            tty (module): tty module
            termios (module): termios module
        """
        keys = keys or self.KEYS

        if isinstance(keys, str):
            keys = PLATFORM_KEYS[keys]
        self.key = self.keys = keys
        if interrupts is None:
            interrupts = self.INTERRUPTS
        self.interrupts = {
            self.keys.code(name): action
            for name, action in interrupts.items()
        }

        self.stdin = stdin or sys.stdin
        if not select:
            from select import select
        if not tty:
            import tty
        if not termios:
            import termios
        self.select = select
        self.tty = tty
        self.termios = termios

        try:
            self.__decoded_stream = OSReadWrapper(self.stdin)
        except Exception as err:
            raise GetKeyException('Cannot use unix platform on non-file-like stream')

    def fileno(self):
        return self.__decoded_stream.fileno()

    @contextmanager
    def context(self):
        fd = self.fileno()
        old_settings = self.termios.tcgetattr(fd)
        self.tty.setcbreak(fd)
        try:
            yield
        finally:
            self.termios.tcsetattr(
                fd, self.termios.TCSADRAIN, old_settings
            )

    def getchars(self, blocking=True):
        """Get characters on Unix."""
        with self.context():
            if blocking:
                yield self.__decoded_stream.read(1)
            while self.select([self.fileno()], [], [], 0)[0]:
                yield self.__decoded_stream.read(1)


class OSReadWrapper(object):
    """Wrap os.read binary input with encoding in standard stream interface.

    We need this since os.read works more consistently on unix, but only
    returns byte strings.  Since the user might be typing on an international
    keyboard or pasting unicode, we need to decode that.  Fortunately
    python's stdin has the fileno & encoding attached to it, so we can
    just use that.
    """
    def __init__(self, stream, encoding=None):
        """Construct os.read wrapper.

        Arguments:
            stream (file object): File object to read.
            encoding (str): Encoding to use (gets from stream by default)
        """
        self.__stream = stream
        self.__fd = stream.fileno()
        self.encoding = encoding or stream.encoding
        self.__decoder = codecs.getincrementaldecoder(self.encoding)()

    def fileno(self):
        return self.__fd

    @property
    def buffer(self):
        return self.__stream.buffer

    def read(self, chars):
        buffer = ''
        while len(buffer) < chars:
            buffer += self.__decoder.decode(os.read(self.__fd, 1))
        return buffer


class PlatformWindows(Platform):
    KEYS = 'windows'
    INTERRUPTS = {'CTRL_C': KeyboardInterrupt}

    def __init__(self, keys=None, interrupts=None, msvcrt=None):
        keys = keys or self.KEYS

        if isinstance(keys, str):
            keys = PLATFORM_KEYS[keys]
        self.key = self.keys = keys
        if interrupts is None:
            interrupts = self.INTERRUPTS
        self.interrupts = {
            self.keys.code(name): action
            for name, action in interrupts.items()
        }

        if msvcrt is None:
            import msvcrt
        self.msvcrt = msvcrt

    def getchars(self, blocking=True):
        """Get characters on Windows."""

        if blocking:
            yield self.msvcrt.getch()
        while self.msvcrt.kbhit():
            yield self.msvcrt.getch()


def windows_or_unix(*args, **kwargs):
    try:
        import msvcrt
    except ImportError:
        return PlatformUnix(*args, **kwargs)
    else:
        return PlatformWindows(*args, **kwargs)



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


