class Rule:
  digit_grouping = 3
  negative_phrase = 'negatif'
  separator = ' '
  ordering = 'hst'
  
  unit_names = ['nol', 'satu', 'dua', 'tiga', 'empat', 'lima',
                'enam', 'tujuh', 'delapan', 'sembilan']
  suffixes = {
    1: 'puluh',
    2: 'ratus',
    3: 'ribu',
    6: 'juta',
    9: 'milyar',
    12: 'triliun',
    15: 'kuadriliun',
    18: 'kuantiliun',
    21: 'sekstiliun',
    24: 'septiliun',
    27: 'oktiliun',
    30: 'noniliun',
    33: 'desiliun',
    36: 'undesiliun',
    39: 'duodesiliun',
    42: 'tredesiliun',
  }
  
  @classmethod
  def non_regular(cls, digit, head, tail):
    head_names = dict()
    head_separator = None
    suffix = None
    
    if digit == 2:
      if head == 1 and tail:
        suffix = 'belas'
        head = tail
        tail = 0

    if digit < 4:
      head_names[1] = 'se'
      if head == 1:
        head_separator = ''
    
    return {k: v for k, v in {
      'head': head,
      'tail': tail,
      'head_names': head_names,
      'head_separator': head_separator,
      'suffix': suffix,
    }.items() if v is not None}
