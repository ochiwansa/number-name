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
        'after': 10,
        'before': 20,
        'rules': {
            'morph': lambda head, tail, suffix: (
                tail, 0, 'belas'),
        },
    },
    {
        # se...
        # e.g. sepuluh (10)
        # e.g. seribu seratus sebelas (1_111)
        'head': 1,
        'before': 2_000,
        'rules': {
            'head_names': {
                1: 'se',
            },
            'head_separator': '',
        },
    },
]

message_out_of_range = 'Bilangan di luar jangkauan'
