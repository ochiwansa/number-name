# ochiwansa/number-name
An attempt to create a universal "number name" library in Python, with declarative-style rule definition.

Sample language rule definition (lang/indonesian.py):

```python
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
        # e.g. sebelas (11)
        # e.g. seribu (1000)
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
```

Sample usage:

    >>> from number_name import number_name, lang
    >>> number_name(132_576_849_015, lang.english)
    'one hundred and thirty-two billion, five hundred and seventy-six million, eight hundred and forty-nine thousand, fifteen'
    >>> number_name(132_576_849_015, lang.indonesian)
    'seratus tiga puluh dua milyar lima ratus tujuh puluh enam juta delapan ratus empat puluh sembilan ribu lima belas'
    >>> number_name(132_576_849_015, lang.french)
    'cent trente-deux milliard cinq cent soixante-seize million huit cent quarante-neuf mille quinze'
    >>> number_name(132_576_849_015, lang.german)
    'hundertzweiunddreißig Milliarden fünfhundertsechsundsiebzig Millionen achthundertneunundvierzigtausendfünfzehn'
    >>> number_name(132_576_849_015, lang.japanese)
    'sen sanbyaku nijū-gooku nanasen roppyaku hachijū-yonman kyūsen jū-go'
