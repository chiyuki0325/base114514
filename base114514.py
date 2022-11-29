#! /usr/bin/env python3

"""Base114514 data encodings"""

from base64 import b64decode, b64encode
from locale import getdefaultlocale
from binascii import Error as BinASCIIError
from re import fullmatch
import sys

__all__ = ['b114514encode', 'b114514decode', 'encoding_dict', 'decoding_dict']

encoding_dict = {65: b'1145', 66: b'1154', 67: b'1514', 68: b'1415', 69: b'1541', 70: b'1451', 71: b'5114', 72: b'4115',
                 73: b'5141', 74: b'4151', 75: b'4511', 76: b'5411', 77: b'5541', 78: b'5514', 79: b'5154', 80: b'5451',
                 81: b'5145', 82: b'5415', 83: b'1554', 84: b'4551', 85: b'4515', 86: b'1545', 87: b'1455', 88: b'4155',
                 89: b'4415', 90: b'4451', 97: b'4541', 98: b'4145', 99: b'4154', 100: b'4514', 101: b'1445',
                 102: b'5441', 103: b'1454', 104: b'5414', 105: b'5144', 106: b'1544', 107: b'1114', 108: b'1115',
                 109: b'5551', 110: b'5554', 111: b'4441', 112: b'4445', 113: b'1151', 114: b'1141', 115: b'5515',
                 116: b'5545', 117: b'4454', 118: b'4414', 119: b'1511', 120: b'1411', 121: b'4544', 122: b'4144',
                 48: b'5455', 49: b'5155', 50: b'1111', 51: b'4444', 52: b'5555', 53: b'1155', 54: b'1144', 55: b'5511',
                 56: b'5544', 57: b'4455', 43: b'4411', 47: b'5115', 61: b'4114'}
decoding_dict = {b'1145': b'A', b'1154': b'B', b'1514': b'C', b'1415': b'D', b'1541': b'E', b'1451': b'F',
                 b'5114': b'G', b'4115': b'H', b'5141': b'I', b'4151': b'J', b'4511': b'K', b'5411': b'L',
                 b'5541': b'M', b'5514': b'N', b'5154': b'O', b'5451': b'P', b'5145': b'Q', b'5415': b'R',
                 b'1554': b'S', b'4551': b'T', b'4515': b'U', b'1545': b'V', b'1455': b'W', b'4155': b'X',
                 b'4415': b'Y', b'4451': b'Z', b'4541': b'a', b'4145': b'b', b'4154': b'c', b'4514': b'd',
                 b'1445': b'e', b'5441': b'f', b'1454': b'g', b'5414': b'h', b'5144': b'i', b'1544': b'j',
                 b'1114': b'k', b'1115': b'l', b'5551': b'm', b'5554': b'n', b'4441': b'o', b'4445': b'p',
                 b'1151': b'q', b'1141': b'r', b'5515': b's', b'5545': b't', b'4454': b'u', b'4414': b'v',
                 b'1511': b'w', b'1411': b'x', b'4544': b'y', b'4144': b'z', b'5455': b'0', b'5155': b'1',
                 b'1111': b'2', b'4444': b'3', b'5555': b'4', b'1155': b'5', b'1144': b'6', b'5511': b'7',
                 b'5544': b'8', b'4455': b'9', b'4411': b'+', b'5115': b'/', b'4114': b'='}


def _(s: str) -> str:
    cn_strings = {
        'string argument should contain only ASCII characters': '字符串参数应仅包含 ASCII 字符',
        'Non-base114514 digit found': '发现非 base114514 字符',
        'Usage: base114514 [OPTION]... [FILE]': '用法：base114514 [选项]... [文件]',
        'Base114514 encode or decode FILE, or standard input, to standard output.\n': 'Base114514 编码或解码 <文件> 或标准输入，并输出到标准输出。\n',
        'With no FILE, or when FILE is -, read standard input.\n': '如果没有指定 <文件>，或者 <文件> 为 "-"，则从标准输入读取。\n',
        'Mandatory arguments to long options are mandatory for short options too.': '长选项的必选参数对于短选项也是必选的。',
        'decode data': '解码数据',
        'when decoding, ignore non-numeric characters': '解码时忽略非数字字符',
        'COLS': '列数',
        'wrap encoded lines after COLS character (default 76).': '在指定的 <列数> 后自动换行（默认为 76）。',
        'Use 0 to disable line wrapping': '0 为禁用自动换行',
        'output version information and exit': '显示版本信息并退出',
        'The data are encoded as described for the base114514 alphabet by YidaozhanYa.': '数据以 YidaozhanYa 规定的 base114514 数字表的格式进行编码。',
        'When decoding, the input may contain newlines in addition to the bytes of': '解码时，输入数据除了包含正式的 base114514 数字表的字节以外，还可能包含一些',
        'the formal base114514 alphabet.  Use --ignore-garbage to attempt to recover': '换行符。使用 --ignore-garbage 来使程序在已编码的流中遇到数字表以外的',
        'from any other non-numeric bytes in the encoded stream.': '字节后尝试恢复执行。',
        'Huh, huh, huh, ah ah ah ah ah ah ah ah ah ah ah ah ah ah ah ah ah ah ah ah ah': '哼, 哼, 哼, 啊啊啊啊啊啊啊啊啊啊啊啊啊',
        'unrecognized option': '不适用的选项',
        'Try \'base114514 --help\' for more information.': '请尝试执行 "base114514 --help" 来获取更多信息。',
        'extra operand': '多余的操作对象'
    }
    if getdefaultlocale()[0].startswith('zh'):
        return cn_strings[s]
    else:
        return s


# from standard base64 module
bytes_types = (bytes, bytearray)  # Types acceptable as binary data


def _bytes_from_decode_data(s):
    if isinstance(s, str):
        try:
            return s.encode('ascii')
        except UnicodeEncodeError:
            raise ValueError(_('string argument should contain only ASCII characters'))
    if isinstance(s, bytes_types):
        return s
    try:
        return memoryview(s).tobytes()
    except TypeError:
        raise TypeError("argument should be a bytes-like object or ASCII "
                        "string, not %r" % s.__class__.__name__) from None


# Base114514 encoding/decoding uses standard base64 module

def b114514encode(bytes_to_encode: bytes) -> bytes:
    """
    Encode the bytes-like object s using Base114514 and return a bytes object.
    """
    encoded: bytes = bytes()
    base64_encoded: bytes = b64encode(bytes_to_encode)
    for i in range(len(base64_encoded)):
        encoded += encoding_dict[base64_encoded[i]]
    return encoded


def b114514decode(bytes_to_decode: bytes, validate: bool = False) -> bytes:
    """Decode the Base114514 encoded bytes-like object or ASCII string s.

    The result is returned as a bytes object.  A binascii.Error is raised if
    s is incorrectly padded.

    If validate is False (the default), characters that are neither in the
    normal base-114514 alphabet nor the alternative alphabet are discarded prior
    to the padding check.  If validate is True, these non-alphabet characters
    in the input result in a binascii.Error.
    """
    bytes_to_decode = _bytes_from_decode_data(bytes_to_decode)
    decoded: bytes = bytes()
    if validate and not fullmatch(r'[145]*', bytes_to_decode.decode()):
        raise BinASCIIError(_('Non-base114514 digit found'))
    validated_bytes_to_decode = bytes()
    for i in range(len(bytes_to_decode)):
        match bytes_to_decode[i]:
            case 49:
                validated_bytes_to_decode += b'1'
            case 52:
                validated_bytes_to_decode += b'4'
            case 53:
                validated_bytes_to_decode += b'5'
    for i in range(len(validated_bytes_to_decode) // 4):
        decoded += decoding_dict[validated_bytes_to_decode[i * 4:i * 4 + 4]]
    return b64decode(decoded)


def wraps(string: str, every=76):
    return '\n'.join(string[i:i + every] for i in range(0, len(string), every))


def main():
    wrap: int = 76
    decode_mode: bool = False
    ignore_garbage_mode: bool = False
    file_name: str = ""
    sys.argv.pop(0)  # def main():
    wrap: int = 76
    decode_mode: bool = False
    ignore_garbage_mode: bool = False
    file_name: str = ""
    if sys.argv and sys.argv[0] == 'base114514':
        sys.argv.pop(0)  # remove base114514 itself

    for arg in sys.argv:

        if arg == '--help':
            print(_('Usage: base114514 [OPTION]... [FILE]'))
            print(_('Base114514 encode or decode FILE, or standard input, to standard output.\n'))
            print(_('With no FILE, or when FILE is -, read standard input.\n'))
            print(_('Mandatory arguments to long options are mandatory for short options too.'))
            print(f'  -d, --decode          {_("decode data")}')
            print(f'  -i, --ignore-garbage  {_("when decoding, ignore non-numeric characters")}')
            print(f'  -w, --wrap={_("COLS")}       {_("wrap encoded lines after COLS character (default 76).")}')
            print(f'                          {_("Use 0 to disable line wrapping")}')
            print(f'      --version     {_("output version information and exit")}\n')
            print(_('The data are encoded as described for the base114514 alphabet by YidaozhanYa.'))
            print(_('When decoding, the input may contain newlines in addition to the bytes of'))
            print(_('the formal base114514 alphabet.  Use --ignore-garbage to attempt to recover'))
            print(_('from any other non-numeric bytes in the encoded stream.'))
            exit()

        elif arg == '--version':
            print('base114514 (下北沢 coreutils) 114.5.1.4'
                  '           ▃▆█▇▄▖◣'
                  '         ▟◤ 　   ◥█▎'
                  '      ◢◤　   ▐　   ▐▉'
                  '    ▗◤　   ▂　▗▖   ▕█▎'
                  '    ◤　▗▅▖◥▄　▀◣    █▊'
                  '    ▐　▕▎◥▖◣◤　    ◢██'
                  '    █◣　◥▅█▀　   ▐██◤'
                  '    ◥██◣       ◢██◤'
                  '     ◥██◣     ◢▄◤'
                  '        ▀██▅▇▀'
                  ''
                  f'{_("Huh, huh, huh, ah ah ah ah ah ah ah ah ah ah ah ah ah ah ah ah ah ah ah ah ah")}!')
            exit()

        elif arg.startswith('-w') or arg.startswith('--wrap'):
            wrap = int(arg.replace('--wrap=', '').replace('-w', ''))

        elif arg == '-d' or arg == '--decode':
            decode_mode = True

        elif arg == '-i' or arg == '--ignore-garbage':
            ignore_garbage_mode = True

        elif arg.startswith('-'):
            print(f'base114514: {_("unrecognized option")} \'{arg}\'')
            print(_('Try \'base114514 --help\' for more information.'))
            exit()

        else:
            if file_name == "":
                file_name = arg
            else:
                print(f'base114514: {_("extra operand")} \'{arg}\'')
                print(_('Try \'base114514 --help\' for more information.'))
                exit()

    if not decode_mode:
        # encode
        if file_name == "":
            # stdin
            encoded_string = b114514encode(sys.stdin.buffer.read()).decode()
        else:
            # file
            opened_file = open(file_name)
            encoded_string = b114514encode(opened_file.buffer.read()).decode()
        if wrap == 0:
            print(encoded_string, end='')
        else:
            print(wraps(encoded_string, wrap), end='')
    else:
        # decode
        if file_name == "":
            # stdin
            decoded_string = b114514decode(sys.stdin.buffer.read().strip(b' \n\r'),
                                           not ignore_garbage_mode).decode()
        else:
            # file
            opened_file = open(file_name)
            decoded_string = b114514decode(opened_file.buffer.read().strip(b' \n\r'),
                                           not ignore_garbage_mode).decode()
        print(decoded_string, end='')


if __name__ == '__main__':
    main()
