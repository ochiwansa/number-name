base_number = 10
digit_grouping = 3
negative_word = 'minus'
default_separator = ''
default_ordering = 'hst'

unit_names = [
    'null',
    'eins',
    'zwei',
    'drei',
    'vier',
    'fünf',
    'sechs',
    'sieben',
    'acht',
    'neun',
]

suffixes = [
    ['zig', 'hundert'],
    'tausend',
    'Million',
    'Milliarde',
    'Billion',
    'Billiarde',
    'Trillion',
    'Trilliarde',
    'Quadrillion',
    'Quadrilliarde',
    'Quintillion',
    'Quintilliarde',
    'Sextillion',
    'Sextilliarde',
    'Septillion',
    'Septilliarde',
    'Octillion',
    'Octilliarde',
    'Nonillion',
    'Nonilliarde',
    'Decillion',
    'Decilliarde',
]

irregulars = {
    11: 'elf',
    12: 'zwölf',
}

semi_regulars = [
    {
        # sech... & sieb...
        # e.g. sechzehn (16)
        # e.g. siebzig (70)
        'digit': 2,
        'rules': {
            'head_names': {
                6: 'sech',
                7: 'sieb',
            }
        },
    },
    {
        # zehn & ...zehn
        # e.g. zehn (10)
        # e.g. neunzehn (19)
        'min': 10,
        'before': 20,
        'rules': {
            'morph': lambda head, tail, suffix: (
                tail, 0, 'zehn'),
            'head_names': {
                0: '',
            }
        },
    },
    {
        # ...zig & ...und...zig
        # e.g. zwanzig (20)
        # e.g. einundfünfzig (51)
        # e.g. neunundneunzig (99)
        'min': 20,
        'before': 100,
        'rules': {
            'head_names': {
                2: 'zwan',
            },
            'tail_names': {
                1: 'ein',
            },
            'ordering': 'ths',
            'tail_separator': 'und',
        },
    },
    {
        # dreißig & ...unddreißig
        # e.g. dreißig (30)
        # e.g. neununddreißig (39)
        'min': 30,
        'before': 40,
        'rules': {
            'morph': lambda head, tail, suffix: (
                head, tail, 'ßig'),
        },
    },
    {
        # hundert... & tausend...
        # e.g. hundert (100)
        # e.g. hundertsechzig (160)
        # e.g. tausend (1_000)
        # e.g. tausendneunhundertneunundnenunzig (1_999)
        'min': 100,
        'before': 2_000,
        'rules': {
            'head_names': {
                1: '',
            },
        },
    },
    {
        # eine ...
        # e.g. eine Million (1_000_000)
        # e.g. eine Milliarde tausendzwölf (1_000_001_012)
        'min': 1_000_000,
        'rules': {
            'head_names': {
                1: 'eine',
            },
            'head_separator': ' ',
            'tail_separator': ' ',
        },
    },
    {
        # ... Millionen, ... Milliarden, etc.
        # e.g. zwei Millionen (2_000_000)
        # e.g. neun Trilliarden (9_000_000_000_000_000)
        'head': lambda x: x > 1,
        'min': 2_000_000,
        'rules': {
            'morph': lambda head, tail, suffix: (
                head, tail, suffix + ('en' if suffix[-1] != 'e' else 'n')),
        },
    },
]

message_out_of_range = 'Die Nummer ist außerhalb des zulässigen Bereichs'
