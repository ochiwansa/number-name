class Rule:
  digit_grouping = 3
  negative_phrase = 'minus'
  separator = ' '
  ordering = 'hst'
  
  unit_names = ['zero', 'one', 'two', 'three', 'four',
                'five', 'six', 'seven', 'eight', 'nine']
  suffixes = {
    1: 'ty',
    2: 'hundred',
    3: 'thousand',
    6: 'million',
    9: 'billion',
    12: 'trillion',
    15: 'quadrillion',
    18: 'quintillion',
    21: 'sextillion',
    24: 'septillion',
    27: 'octillion',
    30: 'nonillion',
    33: 'decillion',
    36: 'undecillion',
    39: 'duodecillion',
    42: 'tredecillion',
  }
  
  @classmethod
  def non_regular(cls, digit, head, tail):
    head_names = dict()
    head_separator = None
    tail_separator = None
    suffix = None
    
    if digit == 2:
      head_separator = ''
      tail_separator = '-'
      head_names[3] = 'thir'
      head_names[5] = 'fif'
      head_names[8] = 'eigh'
      if head == 1:
        suffix = 'teen' if tail > 2 else ''
        head = tail
        tail = 0
        head_names[0] = 'ten'
        head_names[1] = 'eleven'
        head_names[2] = 'twelve'
      else:
        head_names[2] = 'twen'
        head_names[4] = 'for'
    else:
      tail_separator = ' and ' if tail < 100 else ', '
    
    return {k: v for k, v in {
      'head': head,
      'tail': tail,
      'head_names': head_names,
      'head_separator': head_separator,
      'tail_separator': tail_separator,
      'suffix': suffix,
    }.items() if v is not None}
