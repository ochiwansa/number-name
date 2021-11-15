base_number = 10
digit_grouping = 3
negative_word = 'moins'
default_separator = ' '
default_ordering = 'hst'

unit_names = [
    'zéro',
    'un',
    'deux',
    'trois',
    'quatre',
    'cinq',
    'six',
    'sept',
    'huit',
    'neuf',
]

suffixes = [
    ['nte', 'cent'],
    'mille',
    'million',
    'milliard',
    'billion',
    'billiard',
    'trillion',
    'trilliard',
    'quadrillion',
    'quadrilliard',
    'quintillion',
    'quintilliard',
    'sextillion',
    'sextilliard',
    'septillion',
    'septilliard',
    'octillion',
    'octilliard',
    'nonillion',
    'nonilliard',
    'decillion',
    'decilliard',
]

irregulars = None

semi_regulars = [
    {
        # ...-...
        # e.g. dix-sept (17)
        # e.g. soixante-neuf (69)
        'digit': 2,
        'rules': {
            'head_separator': '',
            'tail_separator': '-',
        },
    },
    {
        # dix & dix-...
        # e.g. dix (10)
        # e.g. dix-neuf (19)
        'number': [10, 17, 18, 19],
        'rules': {
            'morph': lambda head, tail, suffix: (
                head, tail, 'dix'),
            'head_names': {
                1: '',
            },
        },
    },
    {
        # ...ze
        # e.g. onze (11)
        # e.g. seize (16)
        'min': 11,
        'max': 16,
        'rules': {
            'morph': lambda head, tail, suffix: (
                0, tail, 'ze'),
            'tail_names': {
                1: 'on',
                2: 'dou',
                3: 'trei',
                4: 'quator',
                5: 'quin',
                6: 'sei',
            },
            'tail_separator': '',
            'ordering': 'tsh',
        },
    },
    {
        # ...nte & ...nte...
        # e.g. trente (30)
        # e.g. quarante (40)
        # e.g. soixante-huit (68)
        # e.g. soixante-dix-neuf (79)
        'digit': 2,
        'head': lambda x: x > 2 and x < 8,
        'rules': {
            'morph': lambda head, tail, suffix: (
                head if head < 7 else 6,
                tail if head < 7 else tail + 10,
                suffix),
            'head_names': {
                3: 'tre',
                4: 'quara',
                5: 'cinqua',
                6: 'soixa',
            },
        },
    },
    {
        # vingt, vingt-..., quatre-vingts & quatre-vingt-...
        # e.g. vingt (20)
        # e.g. vingt-cinq (25)
        # e.g. quatre-vingts (80)
        # e.g. quatre-vingt-un (81)
        # e.g. quatre-vingt-dix-neuf (99)
        'digit': 2,
        'head': [2, 8, 9],
        'rules': {
            'morph': lambda head, tail, suffix: (
                head if head == 2 else 4,
                tail + 10 if head == 9 else tail,
                'vingt'),
            'head_names': {
                2: '',
            },
            'head_separator': '-',
        },
    },
    {
        # ... et un & ... et onze
        # e.g. vingt et un (21)
        # e.g. soixante et onze (71)
        'min': 20,
        'max': 80,
        'tail': [1, 11],
        'rules': {
            'tail_separator': ' et ',
        },
    },
    {
        # quatre-vingts, ... cents, ... millions, etc.
        # ... mille, quatre-vingt mille, quatre-vingts millions, etc.
        # ... cent mille, ... cents millions, etc.
        # e.g. quatre-vingts (80)
        # e.g. huit cents (800)
        # e.g. huit mille (8_000)
        # e.g. quatre-vingt mille (80_000)
        # e.g. huit cent mille (800_000)
        # e.g. huit millions (8_000_000)
        # e.g. quatre-vingts millions (80_000_000)
        # e.g. huit cents millions (800_000_000)
        'min': 80,
        'head': lambda x: x > 1,
        'tail': lambda x: not x,
        'scale': lambda x: x < 3 or x >= 6,
        'rules': {
            'morph': lambda head, tail, suffix: (
                head, tail, suffix + ('s' if suffix != 'mille' else '')),
        },
    },
    {
        # cent & mille
        # e.g. cent (100)
        # e.g. mille (1_000)
        'min': 100,
        'max': 2000,
        'rules': {
            'head_names': {
                1: '',
            },
        },
    },
]