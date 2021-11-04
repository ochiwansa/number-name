class Rule:
  digit_grouping = 3
  negative_phrase = 'minus'
  separator = ''
  ordering = 'hst'
  
  unit_names = ['null', 'eins', 'zwei', 'drei', 'vier',
                'fünf', 'sechs', 'sieben', 'acht', 'neun']
  suffixes = {
    1: 'zig',
    2: 'hundert',
    3: 'tausend',
    6: 'million',
    9: 'milliarde',
    12: 'billion',
    15: 'billiarde',
    18: 'trillion',
    21: 'trilliarde',
    24: 'quadrillion',
    27: 'quadrilliarde',
    30: 'quintillion',
    33: 'quintilliarde',
    36: 'sextillion',
    39: 'sextilliarde',
    42: 'septillion',
    45: 'septilliarde',
  }
  
  @classmethod
  def non_regular(cls, digit, head, tail):
    head_names = dict()
    tail_names = dict()
    suffix = None
    ordering = None
    head_separator = None
    tail_separator = None
    
    if digit == 2:
      head_names[6] = 'sech'
      head_names[7] = 'sieb'
      if head == 1:
        suffix = '' if tail in (1, 2) else 'zehn'
        head = tail
        tail = 0
        head_names[0] = ''
        head_names[1] = 'elf'
        head_names[2] = 'zwölf'
      else:
        suffix = 'ßig' if head == 3 else None
        head_names[2] = 'zwan'
        tail_names[1] = 'ein'
        ordering = 'ths'
        tail_separator = 'und'
    elif digit < 7:
      head_names[1] = ''
    else:
      head_names[1] = 'eine'
      head_separator = ' '
      tail_separator = ' '

    return {k: v for k, v in {
      'head': head,
      'tail': tail,
      'head_names': head_names,
      'tail_names': tail_names,
      'suffix': suffix,
      'ordering': ordering,
      'head_separator': head_separator,
      'tail_separator': tail_separator,
    }.items() if v is not None}
