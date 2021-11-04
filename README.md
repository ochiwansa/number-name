# number-name
An attempt to create a universal "number name" library in Python

Sample usage:

    >>> from number_name import number_name
    >>> from rules import english, indonesian, german, japanese
    >>> number_name(132_576_849_015, english.Rule)
    'one hundred and thirty-two billion five hundred and seventy-six million eight hundred and forty-nine thousand and fifteen'
