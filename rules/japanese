class Rule:
  digit_grouping = 4
  negative_phrase = 'mainasu'
  separator = ' '
  ordering = 'hst'
  
  unit_names = ['zero', 'ichi', 'ni', 'san', 'yon',
                'go', 'roku', 'nana', 'hachi', 'kyū']
  suffixes = {
    1: 'jū',
    2: 'hyaku',
    3: 'sen',
    4: 'man',
    8: 'oku',
    12: 'chō',
    16: 'kei',
    20: 'gai',
  }
  
  @classmethod
  def non_regular(cls, digit, head, tail):
    head_names = dict()
    head_separator = ''
    suffix = None
    
    if digit < 5:
      head_names[1] = ''

    if digit == 3:
      head_names[6] = 'rop'
      head_names[8] = 'hap'
      suffix = 'pyaku' if head in (6, 8) else 'byaku' if head == 3 else None

    if digit == 4:
      head_names[8] = 'has'
      suffix = 'zen' if head == 3 else None

    return {k: v for k, v in {
      'head_names': head_names,
      'head_separator': head_separator,
      'suffix': suffix,
    }.items() if v is not None}
