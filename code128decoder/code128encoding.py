"""Encoding data tables for code128 barcode encoder"""

__revision__ = "$Rev: 1$"

charset_a = \
{
    ' ' :   0,        '!' :   1,        '"' :   2,        '#' :   3,
    '$' :   4,        '%' :   5,        '&' :   6,       '\'' :   7,
    '(' :   8,        ')' :   9,        '*' :  10,        '+' :  11,
    ',' :  12,        '-' :  13,        '.' :  14,        '/' :  15,
    '0' :  16,        '1' :  17,        '2' :  18,        '3' :  19,
    '4' :  20,        '5' :  21,        '6' :  22,        '7' :  23,
    '8' :  24,        '9' :  25,        ':' :  26,        ';' :  27,
    '<' :  28,        '=' :  29,        '>' :  30,        '?' :  31,
    '@' :  32,        'A' :  33,        'B' :  34,        'C' :  35,
    'D' :  36,        'E' :  37,        'F' :  38,        'G' :  39,
    'H' :  40,        'I' :  41,        'J' :  42,        'K' :  43,
    'L' :  44,        'M' :  45,        'N' :  46,        'O' :  47,
    'P' :  48,        'Q' :  49,        'R' :  50,        'S' :  51,
    'T' :  52,        'U' :  53,        'V' :  54,        'W' :  55,
    'X' :  56,        'Y' :  57,        'Z' :  58,        '[' :  59,
   '\\' :  60,        ']' :  61,        '^' :  62,        '_' :  63,
 '\x00' :  64,     '\x01' :  65,     '\x02' :  66,     '\x03' :  67,
 '\x04' :  68,     '\x05' :  69,     '\x06' :  70,     '\x07' :  71,
 '\x08' :  72,     '\x09' :  73,     '\x0a' :  74,     '\x0b' :  75,
 '\x0c' :  76,     '\x0d' :  77,     '\x0e' :  78,     '\x0f' :  79,
 '\x10' :  80,     '\x11' :  81,     '\x12' :  82,     '\x13' :  83,
 '\x14' :  84,     '\x15' :  85,     '\x16' :  86,     '\x17' :  87,
 '\x18' :  88,     '\x19' :  89,     '\x1a' :  90,     '\x1b' :  91,
 '\x1c' :  92,     '\x1d' :  93,     '\x1e' :  94,     '\x1f' :  95,
 '\xf3' :  96,     '\xf2' :  97,    'SHIFT' :  98,     'TO_C' :  99,
 'TO_B' : 100,     '\xf4' : 101,     '\xf1' : 102
}

charset_a_rev = dict([(x[1], x[0]) for x in charset_a.items()])

charset_b = \
{
    ' ' :   0,        '!' :   1,        '"' :   2,        '#' :   3,
    '$' :   4,        '%' :   5,        '&' :   6,       '\'' :   7,
    '(' :   8,        ')' :   9,        '*' :  10,        '+' :  11,
    ',' :  12,        '-' :  13,        '.' :  14,        '/' :  15,
    '0' :  16,        '1' :  17,        '2' :  18,        '3' :  19,
    '4' :  20,        '5' :  21,        '6' :  22,        '7' :  23,
    '8' :  24,        '9' :  25,        ':' :  26,        ';' :  27,
    '<' :  28,        '=' :  29,        '>' :  30,        '?' :  31,
    '@' :  32,        'A' :  33,        'B' :  34,        'C' :  35,
    'D' :  36,        'E' :  37,        'F' :  38,        'G' :  39,
    'H' :  40,        'I' :  41,        'J' :  42,        'K' :  43,
    'L' :  44,        'M' :  45,        'N' :  46,        'O' :  47,
    'P' :  48,        'Q' :  49,        'R' :  50,        'S' :  51,
    'T' :  52,        'U' :  53,        'V' :  54,        'W' :  55,
    'X' :  56,        'Y' :  57,        'Z' :  58,        '[' :  59,
   '\\' :  60,        ']' :  61,        '^' :  62,        '_' :  63,
    '`' :  64,        'a' :  65,        'b' :  66,        'c' :  67,
    'd' :  68,        'e' :  69,        'f' :  70,        'g' :  71,
    'h' :  72,        'i' :  73,        'j' :  74,        'k' :  75,
    'l' :  76,        'm' :  77,        'n' :  78,        'o' :  79,
    'p' :  80,        'q' :  81,        'r' :  82,        's' :  83,
    't' :  84,        'u' :  85,        'v' :  86,        'w' :  87,
    'x' :  88,        'y' :  89,        'z' :  90,        '{' :  91,
    '|' :  92,        '}' :  93,        '~' :  94,     '\x7f' :  95,
 '\xf3' :  96,     '\xf2' :  97,    'SHIFT' :  98,     'TO_C' :  99,
 '\xf4' : 100,     'TO_A' : 101,     '\xf1' : 102
}

charset_b_rev = dict([(x[1], x[0]) for x in charset_b.items()])

charset_c = \
{
    'TO_B' : 100,    'TO_A' : 101,    '\xf1' : 102
}

charset_c_rev = dict([(x[1], x[0]) for x in charset_c.items()])

encodings = \
{
     0: "11011001100",
     1: "11001101100",
     2: "11001100110",
     3: "10010011000",
     4: "10010001100",
     5: "10001001100",
     6: "10011001000",
     7: "10011000100",
     8: "10001100100",
     9: "11001001000",
    10: "11001000100",
    11: "11000100100",
    12: "10110011100",
    13: "10011011100",
    14: "10011001110",
    15: "10111001100",
    16: "10011101100",
    17: "10011100110",
    18: "11001110010",
    19: "11001011100",
    20: "11001001110",
    21: "11011100100",
    22: "11001110100",
    23: "11101101110",
    24: "11101001100",
    25: "11100101100",
    26: "11100100110",
    27: "11101100100",
    28: "11100110100",
    29: "11100110010",
    30: "11011011000",
    31: "11011000110",
    32: "11000110110",
    33: "10100011000",
    34: "10001011000",
    35: "10001000110",
    36: "10110001000",
    37: "10001101000",
    38: "10001100010",
    39: "11010001000",
    40: "11000101000",
    41: "11000100010",
    42: "10110111000",
    43: "10110001110",
    44: "10001101110",
    45: "10111011000",
    46: "10111000110",
    47: "10001110110",
    48: "11101110110",
    49: "11010001110",
    50: "11000101110",
    51: "11011101000",
    52: "11011100010",
    53: "11011101110",
    54: "11101011000",
    55: "11101000110",
    56: "11100010110",
    57: "11101101000",
    58: "11101100010",
    59: "11100011010",
    60: "11101111010",
    61: "11001000010",
    62: "11110001010",
    63: "10100110000",
    64: "10100001100",
    65: "10010110000",
    66: "10010000110",
    67: "10000101100",
    68: "10000100110",
    69: "10110010000",
    70: "10110000100",
    71: "10011010000",
    72: "10011000010",
    73: "10000110100",
    74: "10000110010",
    75: "11000010010",
    76: "11001010000",
    77: "11110111010",
    78: "11000010100",
    79: "10001111010",
    80: "10100111100",
    81: "10010111100",
    82: "10010011110",
    83: "10111100100",
    84: "10011110100",
    85: "10011110010",
    86: "11110100100",
    87: "11110010100",
    88: "11110010010",
    89: "11011011110",
    90: "11011110110",
    91: "11110110110",
    92: "10101111000",
    93: "10100011110",
    94: "10001011110",
    95: "10111101000",
    96: "10111100010",
    97: "11110101000",
    98: "11110100010",
    99: "10111011110",
    100: "10111101110",
    101: "11101011110",
    102: "11110101110",
    103: "11010000100",
    104: "11010010000",
    105: "11010011100",
}

encodings_rev = dict([(x[1], x[0]) for x in encodings.items()])

STOP = "11000111010"
