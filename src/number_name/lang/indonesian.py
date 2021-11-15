base_number = 10
digit_grouping = 3
negative_word = 'minus'
default_separator = ' '
default_ordering = 'hst'

unit_names = [
    'nol',
    'satu',
    'dua',
    'tiga',
    'empat',
    'lima',
    'enam',
    'tujuh',
    'delapan',
    'sembilan',
]

suffixes = [
    ['puluh', 'ratus'],
    'ribu',
    'juta',
    'milyar',
    'triliun',
    'dwiyar',
    'kuintiliun',
    'sektiliun',
    'septiliun',
    'oktiliun',
    'noniliun',
    'desiliun',
    'undesiliun',
    'duodesiliun',
    'tredesiliun',
    'kuattodesiliun',
    'kuindesiliun',
    'sekdesiliun',
    'septemdesiliun',
    'oktodesiliun',
    'novemdesiliun',
    'vigintiliun',
]

irregulars = None

semi_regulars = [
    {
        # ...belas
        # e.g. sebelas (11)
        # e.g. sembilan belas (19)
        'min': 11,
        'max': 19,
        'rules': {
            'morph': lambda head, tail, suffix: (
                tail, 0, 'belas'),
        },
    },
    {
        # se...
        # e.g. sepuluh (10)
        # e.g. seribu seratus sebelas (1111)
        'head': 1,
        'max': 2000,
        'rules': {
            'head_names': {
                1: 'se',
            },
            'head_separator': '',
        },
    },
]

message_out_of_range = 'Bilangan di luar jangkauan yang ditangani'
