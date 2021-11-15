# number-name
An attempt to create a universal "number name" library in Python

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
