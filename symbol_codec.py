# Symbol-to-binary dictionary
symbol_to_binary = {
    # Greek Alphabet
    'α': '0',      'β': '10',    'γ': '110',   'δ': '1110',
    'Ω': '11110',  'Σ': '111110','Π': '1111110','Λ': '11111110',

    # Mathematical Symbols
    '∞': '111111110', '∂': '1111111110', '∇': '11111111110', '√': '111111111110',
    '∑': '1111111111110', '±': '11111111111110', '≠': '111111111111110', '×': '1111111111111110',

    # Runes (Ancient Norse)
    'ᚠ': '00', 'ᚢ': '010', 'ᛗ': '0110', 'ᛇ': '01110',
    'ᛝ': '011110', 'ᛞ': '0111110', 'ᚦ': '01111110', 'ᚬ': '011111110',

    # Hebrew Letters
    'א': '100', 'ב': '1010', 'ג': '10110', 'ד': '101110',
    'צ': '1011110', 'ק': '10111110', 'ת': '101111110', 'ח': '1011111110',

    # Japanese Kana (Katakana)
    'カ': '1100', 'シ': '11010', 'ツ': '110110', 'ソ': '1101110',
    'ク': '11011110', 'コ': '110111110', 'サ': '1101111110', 'セ': '11011111110',

    # Tibetan or Sanskrit
    'ཨ': '11100', 'ॐ': '111010', 'ऌ': '1110110', 'ऋ': '11101110',
    'ष': '111011110', 'क्ष': '1110111110', 'त्र': '11101111110', 'ज्ञ': '111011111110',

    # Cyrillic Alphabet
    'Б': '111100', 'Д': '1111010', 'Г': '11110110', 'Ф': '111101110',
    'Я': '1111011110', 'Ж': '11110111110', 'Ч': '111101111110', 'Ш': '1111011111110'
}

# Encoding function
def encode(data, symbol_to_binary):
    binary_string = ''
    for char in data:
        binary_string += symbol_to_binary.get(char, '')  # Default to empty string if not found
    return binary_string

# Decoding function
def decode(binary_string, symbol_to_binary):
    binary_to_symbol = {v: k for k, v in symbol_to_binary.items()}  # Reverse dictionary
    decoded_string = ''
    temp = ''
    for bit in binary_string:
        temp += bit
        if temp in binary_to_symbol:
            decoded_string += binary_to_symbol[temp]
            temp = ''
    return decoded_string
