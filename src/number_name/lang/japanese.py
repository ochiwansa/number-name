base_number = 10
digit_grouping = 4
negative_word = 'mainasu'
default_separator = ' '
default_ordering = 'hst'

unit_names = [
    'rei',
    'ichi',
    'ni',
    'san',
    'yon',
    'go',
    'roku',
    'nana',
    'hachi',
    'kyū',
]

suffixes = [
    ['jū', 'hyaku', 'sen'],
    'man',
    'oku',
    'chō',
    'kei',
    'gai',
    'jo',
    'jō',
    'kō',
    'kan',
    'sei',
    'sai',
    'goku',
    'gōgasha',
    'asōgi',
    'nayuta',
    'fukashigi',
    'muryōtaisū'
]

irregulars = None

semi_regulars = [
    {
        # ...-...
        # jū-ichi (11)
        # kyūjū-kyū (99)
        'digit': 2,
        'rules': {
            'tail_separator': '-',
        },
    },
    {
        # ...jū, ...hyaku, ...sen, ...man, ...oku, etc.
        # e.g. nijū (20)
        # e.g. goman (5_0000)
        # e.g. kyūchō (9_0000_0000_0000)
        'min': 10,
        'rules': {
            'head_separator': '',
        },
    },
    {
        # jū, hyaku & sen
        # e.g. jū (10)
        # e.g. sen (1_000)
        'before': 1_0000,
        'rules': {
            'head_names': {
                1: '',
            },
        },
    },
    {
        # sanbyaku, roppyaku, happyaku
        # e.g. sanbyaku (300)
        # e.g. happyaku (800)
        'digit': 3,
        'rules': {
            'head_names': {
                6: 'rop',
                8: 'hap',
            },
            'morph': lambda head, tail, suffix: (
                head, tail, 'pyaku' if head in (6, 8)
                else 'byaku' if head == 3 else suffix),
        },
    },
    {
        # sanzen & hassen
        # e.g. sanzen (3000)
        # e.g. hassen (8000)
        'digit': 4,
        'rules': {
            'head_names': {
                8: 'has',
            },
            'morph': lambda head, tail, suffix: (
                head, tail, 'zen' if head == 3 else suffix),
        },
    },
]

message_out_of_range = 'Kazu ga han\'i-gaidesu'
