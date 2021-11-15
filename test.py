import locale
locale.setlocale(locale.LC_ALL, '')

import sys
from os.path import dirname, join
sys.path.append(join(dirname(__file__), 'src'))

from number_name import number_name, lang

value = int(sys.argv[1])
language = sys.argv[2]
print('number:', f'{value:n}')
print('name:', number_name(value, eval(f'lang.{language}')))