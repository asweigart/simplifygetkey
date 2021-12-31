# Which key(s) were pressed
# What chars to print (if any)
# Keycode(s) generating event
import string

class UnicodeAsciiKeys(object):
    NULL = '\x00'
    START_OF_HEADING = '\x01'
    START_OF_TEXT = '\x02'
    END_OF_TEXT = '\x03'
    END_OF_TRANSMISSION = '\x04'
    ENQUIRY = '\x05'
    ACKNOWLEDGE = '\x06'
    BELL = '\x07'
    BACKSPACE = '\x08'
    CHARACTER_TABULATION = '\t'
    HORIZONTAL_TABULATION = '\t'
    TAB = '\t'
    LINE_FEED = '\n'
    NEW_LINE = '\n'
    END_OF_LINE = '\n'
    LINE_TABULATION = '\x0b'
    VERTICAL_TABULATION = '\x0b'
    FORM_FEED = '\x0c'
    CARRIAGE_RETURN = '\r'
    SHIFT_OUT = '\x0e'
    SHIFT_IN = '\x0f'
    DATA_LINK_ESCAPE = '\x10'
    DEVICE_CONTROL_ONE = '\x11'
    DEVICE_CONTROL_TWO = '\x12'
    DEVICE_CONTROL_THREE = '\x13'
    DEVICE_CONTROL_FOUR = '\x14'
    NEGATIVE_ACKNOWLEDGE = '\x15'
    SYNCHRONOUS_IDLE = '\x16'
    END_OF_TRANSMISSION_BLOCK = '\x17'
    CANCEL = '\x18'
    END_OF_MEDIUM = '\x19'
    SUBSTITUTE = '\x1a'
    ESCAPE = '\x1b'
    INFORMATION_SEPARATOR_FOUR = '\x1c'
    FILE_SEPARATOR = '\x1c'
    INFORMATION_SEPARATOR_THREE = '\x1d'
    GROUP_SEPARATOR = '\x1d'
    INFORMATION_SEPARATOR_TWO = '\x1e'
    RECORD_SEPARATOR = '\x1e'
    INFORMATION_SEPARATOR_ONE = '\x1f'
    UNIT_SEPARATOR = '\x1f'
    SPACE = ' '
    EXCLAMATION_MARK = '!'
    FACTORIAL = '!'
    BANG = '!'
    QUOTATION_MARK = '"'
    NUMBER_SIGN = '#'
    POUND_SIGN = '#'
    HASH = '#'
    CROSSHATCH = '#'
    OCTOTHORPE = '#'
    DOLLAR_SIGN = '$'
    ESCUDO = '$'
    PERCENT_SIGN = '%'
    AMPERSAND = '&'
    APOSTROPHE = "'"
    APOSTROPHE_QUOTE = "'"
    APL_QUOTE = "'"
    LEFT_PARENTHESIS = '('
    OPENING_PARENTHESIS = '('
    RIGHT_PARENTHESIS = ')'
    CLOSING_PARENTHESIS = ')'
    ASTERISK = '*'
    STAR = '*'
    PLUS_SIGN = '+'
    COMMA = ','
    DECIMAL_SEPARATOR = ','
    HYPHEN_MINUS = '-'
    HYPHEN_OR_MINUS_SIGN = '-'
    FULL_STOP = '.'
    PERIOD = '.'
    DOT = '.'
    DECIMAL_POINT = '.'
    SOLIDUS = '/'
    SLASH = '/'
    VIRGULE = '/'
    DIGIT_ZERO = '0'
    DIGIT_ONE = '1'
    DIGIT_TWO = '2'
    DIGIT_THREE = '3'
    DIGIT_FOUR = '4'
    DIGIT_FIVE = '5'
    DIGIT_SIX = '6'
    DIGIT_SEVEN = '7'
    DIGIT_EIGHT = '8'
    DIGIT_NINE = '9'
    COLON = ':'
    SEMICOLON = ';'
    LESS_THAN_SIGN = '<'
    EQUALS_SIGN = '='
    GREATER_THAN_SIGN = '>'
    QUESTION_MARK = '?'
    COMMERCIAL_AT = '@'
    AT_SIGN = '@'
    LATIN_CAPITAL_LETTER_A = 'A'
    LATIN_CAPITAL_LETTER_B = 'B'
    LATIN_CAPITAL_LETTER_C = 'C'
    LATIN_CAPITAL_LETTER_D = 'D'
    LATIN_CAPITAL_LETTER_E = 'E'
    LATIN_CAPITAL_LETTER_F = 'F'
    LATIN_CAPITAL_LETTER_G = 'G'
    LATIN_CAPITAL_LETTER_H = 'H'
    LATIN_CAPITAL_LETTER_I = 'I'
    LATIN_CAPITAL_LETTER_J = 'J'
    LATIN_CAPITAL_LETTER_K = 'K'
    LATIN_CAPITAL_LETTER_L = 'L'
    LATIN_CAPITAL_LETTER_M = 'M'
    LATIN_CAPITAL_LETTER_N = 'N'
    LATIN_CAPITAL_LETTER_O = 'O'
    LATIN_CAPITAL_LETTER_P = 'P'
    LATIN_CAPITAL_LETTER_Q = 'Q'
    LATIN_CAPITAL_LETTER_R = 'R'
    LATIN_CAPITAL_LETTER_S = 'S'
    LATIN_CAPITAL_LETTER_T = 'T'
    LATIN_CAPITAL_LETTER_U = 'U'
    LATIN_CAPITAL_LETTER_V = 'V'
    LATIN_CAPITAL_LETTER_W = 'W'
    LATIN_CAPITAL_LETTER_X = 'X'
    LATIN_CAPITAL_LETTER_Y = 'Y'
    LATIN_CAPITAL_LETTER_Z = 'Z'
    LEFT_SQUARE_BRACKET = '['
    OPENING_SQUARE_BRACKET = '['
    REVERSE_SOLIDUS = '\\'
    BACKSLASH = '\\'
    RIGHT_SQUARE_BRACKET = ']'
    CLOSING_SQUARE_BRACKET = ']'
    CIRCUMFLEX_ACCENT = '^'
    LOW_LINE = '_'
    SPACING_UNDERSCORE = '_'
    GRAVE_ACCENT = '`'
    LATIN_SMALL_LETTER_A = 'a'
    LATIN_SMALL_LETTER_B = 'b'
    LATIN_SMALL_LETTER_C = 'c'
    LATIN_SMALL_LETTER_D = 'd'
    LATIN_SMALL_LETTER_E = 'e'
    LATIN_SMALL_LETTER_F = 'f'
    LATIN_SMALL_LETTER_G = 'g'
    LATIN_SMALL_LETTER_H = 'h'
    LATIN_SMALL_LETTER_I = 'i'
    LATIN_SMALL_LETTER_J = 'j'
    LATIN_SMALL_LETTER_K = 'k'
    LATIN_SMALL_LETTER_L = 'l'
    LATIN_SMALL_LETTER_M = 'm'
    LATIN_SMALL_LETTER_N = 'n'
    LATIN_SMALL_LETTER_O = 'o'
    LATIN_SMALL_LETTER_P = 'p'
    LATIN_SMALL_LETTER_Q = 'q'
    LATIN_SMALL_LETTER_R = 'r'
    LATIN_SMALL_LETTER_S = 's'
    LATIN_SMALL_LETTER_T = 't'
    LATIN_SMALL_LETTER_U = 'u'
    LATIN_SMALL_LETTER_V = 'v'
    LATIN_SMALL_LETTER_W = 'w'
    LATIN_SMALL_LETTER_X = 'x'
    LATIN_SMALL_LETTER_Y = 'y'
    LATIN_SMALL_LETTER_Z = 'z'
    LEFT_CURLY_BRACKET = '{'
    OPENING_CURLY_BRACKET = '{'
    LEFT_BRACE = '{'
    VERTICAL_LINE = '|'
    VERTICAL_BAR = '|'
    RIGHT_CURLY_BRACKET = '}'
    CLOSING_CURLY_BRACKET = '}'
    RIGHT_BRACE = '}'
    TILDE = '~'
    DELETE = '\x7f'

# These are used for the names of ctrl keys, etc.
ASCII_NAMES = {
    '\t': 'tab',

    ' ': 'space',          # 0x20
    '!': 'exclamation',    # 0x21
    '"': 'double quote',   # 0x22
    '#': 'hash',           # 0x23
    '$': 'dollar',         # 0x24
    '%': 'percent',        # 0x25
    '&': 'ampersand',      # 0x26
    '\'': 'single quote',  # 0x27
    '(': 'open paren',     # 0x28
    ')': 'close paren',    # 0x29
    '*': 'asterisk',       # 0x2a
    '+': 'plus',           # 0x2b
    ',': 'comma',          # 0x2c
    '-': 'minus',          # 0x2d
    '.': 'period',         # 0x2e
    '/': 'slash',          # 0x2f

    ':': 'colon',          # 0x3a
    ';': 'semicolon',      # 0x3b
    '<': 'less than',      # 0x3c
    '=': 'equals',         # 0x3d
    '>': 'greater than',   # 0x3e
    '?': 'question',       # 0x3f
    '@': 'at',             # 0x40

    '[': 'left bracket',   # 0x5b
    '\\': 'backslash',     # 0x5c
    ']': 'right bracket',  # 0x5d
    '^': 'caret',          # 0x5e
    '_': 'underscore',     # 0x5f
    '`': 'backtick',       # 0x60

    '{': 'left brace',     # 0x7b
    '|': 'pipe',           # 0x7c
    '}': 'right brace',    # 0x7d
    '~': 'tilde',          # 0x7e
}


class UnicodeKeys(object):
    # Names from ftp://ftp.unicode.org/Public/UNIDATA/NamesList.txt
    NULL = chr(0x00)
    START_OF_HEADING = chr(0x01)


class VT100StandardModeKeys(object):
    # http://www.braun-home.net/michael/mbedit/info/misc/VT100_commands.htm
    # http://www.ccs.neu.edu/research/gpc/MSim/vona/terminal/VT100_Escape_Codes.html
    F1 = '\x1bOP'
    F2 = '\x1bOQ'
    F3 = '\x1bOR'
    F4 = '\x1bOS'

    UP = '\x1b[A'
    DOWN = '\x1b[B'
    RIGHT = '\x1b[C'
    LEFT = '\x1b[D'


class VT100ApplicationsModeKeys(object):
    F1 = '\x1bOP'
    F2 = '\x1bOQ'
    F3 = '\x1bOR'
    F4 = '\x1bOS'

    UP = '\x1bOA'
    DOWN = '\x1bOB'
    RIGHT = '\x1bOC'
    LEFT = '\x1bOD'

    KEYPAD_0 = '\x1bOp'
    KEYPAD_1 = '\x1bOq'
    KEYPAD_2 = '\x1bOr'
    KEYPAD_3 = '\x1bOs'
    KEYPAD_4 = '\x1bOt'
    KEYPAD_5 = '\x1bOu'
    KEYPAD_6 = '\x1bOv'
    KEYPAD_7 = '\x1bOw'
    KEYPAD_8 = '\x1bOx'
    KEYPAD_9 = '\x1bOy'
    KEYPAD_MINUS = '\x1bOm'
    KEYPAD_COMMA = '\x1bOl'
    KEYPAD_PERIOD = '\x1bOn'
    KEYPAD_ENTER = '\x1bOM'


class VT220Keys(object):
    # F1-F5 didn't exist historically, but were added by later emulators
    F1 = '\x1b[11~'
    F2 = '\x1b[12~'
    F3 = '\x1b[13~'
    F4 = '\x1b[14~'
    F5 = '\x1b[15~'

    # Historical keys
    F6 = '\x1b[17~'
    F7 = '\x1b[18~'
    F8 = '\x1b[19~'
    F9 = '\x1b[20~'
    F10 = '\x1b[21~'
    F11 = '\x1b[23~'
    F12 = '\x1b[24~'

    # F13+ and key combinations to enter them are of limited usefulness today


class UnixKeys(object):
    # Keys found experimentally, of unknown provenance
    ESC = '\x1b'

    HOME = '\x1b[H'
    END = '\x1b[F'
    PAGE_UP = '\x1b[5'
    PAGE_DOWN = '\x1b[6'

    ENTER = '\n'
    CR = '\r'
    BACKSPACE = '\x7f'

    SPACE = ' '

    INSERT = '\x1b[2~'
    DELETE = '\x1b[3~'


class AlternativeUnixFunctionKeys(object):
    # Unsure origin: alternate V220 mode?
    F1 = '\x1bO11~'
    F2 = '\x1bO12~'
    F3 = '\x1bO13~'
    F4 = '\x1bO14~'
    F5 = '\x1bO15~'
    F6 = '\x1bO17~'
    F7 = '\x1bO18~'
    F8 = '\x1bO19~'
    F9 = '\x1bO20~'
    F10 = '\x1bO21~'
    F11 = '\x1bO23~'
    F12 = '\x1bO24~'


class WindowsKeys(object):
    ESC = '\x1b'

    LEFT = '\xe0K'
    RIGHT = '\xe0M'
    UP = '\xe0H'
    DOWN = '\xe0P'

    ENTER = '\r'
    BACKSPACE = '\x08'
    SPACE = ' '

    F1 = '\x00;'
    F2 = '\x00<'
    F3 = '\x00='
    F4 = '\x00>'
    F5 = '\x00?'
    F6 = '\x00@'
    F7 = '\x00A'
    F8 = '\x00B'
    F9 = '\x00C'
    F10 = '\x00D'
    F11 = '\xe0\x85'
    F12 = '\xe0\x86'

    INSERT = '\xe0R'
    DELETE = '\xe0S'
    PAGE_UP = '\xe0I'
    PAGE_DOWN = '\xe0Q'
    HOME = '\xe0G'
    END = '\xe0O'

    CTRL_F1 = '\x00^'
    CTRL_F2 = '\x00_'
    CTRL_F3 = '\x00`'
    CTRL_F4 = '\x00a'
    CTRL_F5 = '\x00b'
    CTRL_F6 = '\x00c'
    CTRL_F7 = '\x00d'  # Captured by something?
    CTRL_F8 = '\x00e'
    CTRL_F9 = '\x00f'
    CTRL_F10 = '\x00g'
    CTRL_F11 = '\xe0\x89'
    CTRL_F12 = '\xe0\x8a'

    CTRL_HOME = '\xe0w'
    CTRL_END = '\xe0u'
    CTRL_INSERT = '\xe0\x92'
    CTRL_DELETE = '\xe0\x93'
    CTRL_PAGE_DOWN = '\xe0v'

    CTRL_2 = '\x00\x03'
    CTRL_UP = '\xe0\x8d'
    CTRL_DOWN = '\xe0\x91'
    CTRL_LEFT = '\xe0s'
    CTRL_RIGHT = '\xe0t'

    CTRL_ALT_A = '\x00\x1e'
    CTRL_ALT_B = '\x000'
    CTRL_ALT_C = '\x00.'
    CTRL_ALT_D = '\x00 '
    CTRL_ALT_E = '\x00\x12'
    CTRL_ALT_F = '\x00!'
    CTRL_ALT_G = '\x00"'
    CTRL_ALT_H = '\x00#'
    CTRL_ALT_I = '\x00\x17'
    CTRL_ALT_J = '\x00$'
    CTRL_ALT_K = '\x00%'
    CTRL_ALT_L = '\x00&'
    CTRL_ALT_M = '\x002'
    CTRL_ALT_N = '\x001'
    CTRL_ALT_O = '\x00\x18'
    CTRL_ALT_P = '\x00\x19'
    CTRL_ALT_Q = '\x00\x10'
    CTRL_ALT_R = '\x00\x13'
    CTRL_ALT_S = '\x00\x1f'
    CTRL_ALT_T = '\x00\x14'
    CTRL_ALT_U = '\x00\x16'
    CTRL_ALT_V = '\x00/'
    CTRL_ALT_W = '\x00\x11'
    CTRL_ALT_X = '\x00-'
    CTRL_ALT_Y = '\x00\x15'
    CTRL_ALT_Z = '\x00,'
    CTRL_ALT_1 = '\x00x'
    CTRL_ALT_2 = '\x00y'
    CTRL_ALT_3 = '\x00z'
    CTRL_ALT_4 = '\x00{'
    CTRL_ALT_5 = '\x00|'
    CTRL_ALT_6 = '\x00}'
    CTRL_ALT_7 = '\x00~'
    CTRL_ALT_8 = '\x00\x7f'
    CTRL_ALT_9 = '\x00\x80'
    CTRL_ALT_0 = '\x00\x81'
    CTRL_ALT_MINUS = '\x00\x82'
    CTRL_ALT_EQUALS = '\x00x83'
    CTRL_ALT_BACKSPACE = '\x00\x0e'

    ALT_F1 = '\x00h'
    ALT_F2 = '\x00i'
    ALT_F3 = '\x00j'
    ALT_F4 = '\x00k'
    ALT_F5 = '\x00l'
    ALT_F6 = '\x00m'
    ALT_F7 = '\x00n'
    ALT_F8 = '\x00o'
    ALT_F9 = '\x00p'
    ALT_F10 = '\x00q'
    ALT_F11 = '\xe0\x8b'
    ALT_F12 = '\xe0\x8c'
    ALT_HOME = '\x00\x97'
    ALT_END = '\x00\x9f'
    ALT_INSERT = '\x00\xa2'
    ALT_DELETE = '\x00\xa3'
    ALT_PAGE_UP = '\x00\x99'
    ALT_PAGE_DOWN = '\x00\xa1'
    ALT_LEFT = '\x00\x9b'
    ALT_RIGHT = '\x00\x9d'
    ALT_UP = '\x00\x98'
    ALT_DOWN = '\x00\xa0'

    CTRL_ALT_LEFT_BRACKET = '\x00\x1a'
    CTRL_ALT_RIGHT_BRACKET = '\x00\x1b'
    CTRL_ALT_SEMICOLON = '\x00\''
    CTRL_ALT_SINGLE_QUOTE = '\x00('
    CTRL_ALT_ENTER = '\x00\x1c'
    CTRL_ALT_SLASH = '\x005'
    CTRL_ALT_PERIOD = '\x004'
    CTRL_ALT_COMMA = '\x003'


class ControlKeys(object):
    CTRL_A = '\x01'
    CTRL_B = '\x02'
    CTRL_C = '\x03'
    CTRL_D = '\x04'
    CTRL_E = '\x05'
    CTRL_F = '\x06'
    CTRL_G = '\x07'
    CTRL_H = '\x08'
    CTRL_I = '\t'
    CTRL_J = '\n'
    CTRL_K = '\x0b'
    CTRL_L = '\x0c'
    CTRL_M = '\r'
    CTRL_N = '\x0e'
    CTRL_O = '\x0f'
    CTRL_P = '\x10'
    CTRL_Q = '\x11'
    CTRL_R = '\x12'
    CTRL_S = '\x13'
    CTRL_T = '\x14'
    CTRL_U = '\x15'
    CTRL_V = '\x16'
    CTRL_W = '\x17'
    CTRL_X = '\x18'
    CTRL_Y = '\x19'
    CTRL_Z = '\x1a'

    CTRL_AT = '\x00'
    CTRL_BACKSLASH = '\x1c'
    CTRL_CARET = '\x1e'
    CTRL_LEFT_BRACKET = '\x1b'
    CTRL_RIGHT_BRACKET = '\x1d'
    CTRL_UNDERSCORE = '\x1f'



class AsciiKeys(object):
    def __init__(
            self,
            lower_format='{}', upper_format='SHIFT_{}', digit_format='N{}',
            ascii_names=ASCII_NAMES,
    ):
        for letter in string.ascii_lowercase:
            name = lower_format.format(letter.upper())
            setattr(self, name, letter)
        for letter in string.ascii_uppercase:
            name = upper_format.format(letter.upper())
            setattr(self, name, letter)
        for digit in string.digits:
            name = digit_format.format(digit)
            setattr(self, name, digit)
        for char, name in ascii_names.items():
            name = name.upper().replace(' ', '_')
            setattr(self, name, char)


class Keys(object):
    def __init__(self, keyclasses):
        self.__names = dict()  # Map of codes -> names
        self.__codes = dict()  # Map of names -> codes

        self.__escapes = set()

        for keyclass in keyclasses:
            for name in dir(keyclass):
                if self._is_key_name(name):
                    code = getattr(keyclass, name)
                    self.register(name, code)

    def register(self, name, code):
        if name not in self.__codes:
            self.__codes[name] = code
        if code not in self.__names:
            self.__names[code] = name
        for i in range(len(code)):
            self.__escapes.add(code[:i])

        # Update towards canonicity
        while True:
            canon_code = self.canon(code)
            canon_canon_code = self.canon(canon_code)
            if canon_code != canon_canon_code:
                self.__codes[self.name(code)] = canon_canon_code
            else:
                break
        while True:
            canon_name = self.name(self.code(name))
            canon_canon_name = self.name(self.code(canon_name))
            if canon_name != canon_canon_name:
                self.__names[self.code(name)] = canon_canon_name
            else:
                break

    @property
    def escapes(self):
        return self.__escapes

    @property
    def names(self):
        return self.__codes.keys()

    def name(self, code):
        return self.__names.get(code)

    def code(self, name):
        return self.__codes.get(name)

    def canon(self, code):
        name = self.name(code)
        return self.code(name) if name else code

    def __getattr__(self, name):
        code = self.code(name)
        if code is not None:
            return code
        else:
            return self.__getattribute__(name)

    def _is_key_name(self, name):
        return name == name.upper() and not name.startswith('_')


def _make_escapes(codes):
    escapes = set()
    for code in codes:
        for i in range(len(code)):
            escapes.add(code[:i])
    return escapes


unix_keys = Keys([
    VT100StandardModeKeys(),
    VT100ApplicationsModeKeys(),
    VT220Keys(),
    UnixKeys(),
    AlternativeUnixFunctionKeys(),
    AsciiKeys(),
    ControlKeys(),
    UnicodeAsciiKeys(),
])
windows_keys = Keys([
    WindowsKeys(),
    AsciiKeys(),
    ControlKeys(),
    UnicodeAsciiKeys(),
])


PLATFORM_KEYS = {
    'unix': unix_keys,
    'windows': windows_keys,
}
