base_number = 10
digit_grouping = 3
negative_word = 'minus'
default_separator = ' '
default_ordering = 'hst'

unit_names = [
    'zero',
    'one',
    'two',
    'three',
    'four',
    'five',
    'six',
    'seven',
    'eight',
    'nine',
]

suffixes = [
    ['ty', 'hundred'],
    'thousand',
    'million',
    'billion',
    'trillion',
    'quadrillion',
    'quintillion',
    'sextillion',
    'septillion',
    'octillion',
    'nonillion',
    'decillion',
    'undecillion',
    'duodecillion',
    'tredecillion',
    'quattuordecillion',
    'quindecillion',
    'sexdecillion',
    'septendecillion',
    'octodecillion',
    'novemdecillion',
    'vigintillion',
]

irregulars = {
    10: 'ten',
    11: 'eleven',
    12: 'twelve',
}

semi_regulars = [
    {
        # ...ty, ...ty... & ...teen
        # e.g. twenty (20)
        # e.g. ninety-nine (99)
        # e.g. fifteen (15)
        'digit': 2,
        'rules': {
            'head_names': {
                2: 'twen',
                3: 'thir',
                5: 'fif',
                8: 'eigh',
            },
            'head_separator': '',
            'tail_separator': '-',
        },
    },
    {
        # ...teen
        # e.g. thirteen (13)
        # e.g. nineteen (19)
        'min': 13,
        'before': 20,
        'rules': {
            'morph': lambda head, tail, suffix: (
                tail, 0, 'teen'),
        },
    },
    {
        # forty & forty-...
        # e.g. forty (40)
        # e.g. forty-nine (49)
        'min': 40,
        'before': 50,
        'rules': {
            'head_names': {
                4: 'for',
            },
        },
    },
    {
        # ... group_suffix, ...
        # e.g. one million, two thousand, three hundred (1_002_300)
        'digit': lambda x: x > digit_grouping,
        'rules': {
            'tail_separator': ', ',
        },
    },
    {
        # ... hundred and ...
        # e.g. two hundred and twelve (212)
        # e.g. nine hundred and ninety-nine (999)
        'digit': digit_grouping,
        'rules': {
            'tail_separator': ' and ',
        },
    },
]

message_out_of_range = 'The number is out of range'
