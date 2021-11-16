def number_name(n, lang, scale=0):
  if n < 0:
    return lang.negative_word + ' ' + number_name(-n, lang)
  
  if n < lang.base_number:
    return lang.unit_names[n]
  
  if lang.irregulars:
    if n in lang.irregulars:
      return lang.irregulars[n]

  max_digit = len(lang.suffixes) * lang.digit_grouping
  digit = len(str(n // lang.base_number)) + 1
  
  if digit > max_digit:
    raise ValueError(lang.message_out_of_range
      if hasattr(lang, 'message_out_of_range')
      else 'The number is out of range')
  
  power = digit - 1
  if power > lang.digit_grouping:
    power //= lang.digit_grouping
    power *= lang.digit_grouping
  divisor = pow(lang.base_number, power)
  
  head = n // divisor
  tail = n % divisor
  
  suffix = lang.suffixes[power // lang.digit_grouping] \
    if power >= lang.digit_grouping \
      else lang.suffixes[0][power - 1]

  head_names = [name for name in lang.unit_names]
  tail_names = [name for name in lang.unit_names]

  head_separator = lang.default_separator
  tail_separator = lang.default_separator

  ordering = lang.default_ordering

  spell_zero_head = False
  spell_zero_tail = False

  if lang.semi_regulars:
    def check_value(val, check):
      return (check(val) if callable(check)
        else val in check if type(check) == list
        else val == check)

    filters = {
      'number': lambda x: check_value(n, x),
      'digit': lambda x: check_value(digit, x),
      'head': lambda x: check_value(head, x),
      'tail': lambda x: check_value(tail, x),
      'suffix': lambda x: check_value(suffix, x),
      'scale': lambda x: check_value(scale, x),
      'min': lambda x: n >= x,
      'max': lambda x: n <= x,
      'after': lambda x: n > x,
      'before': lambda x: n < x,
    }

    for sr in lang.semi_regulars:
      condition = True
      for filter in filters:
        if filter in sr:
          condition = condition and filters[filter](sr[filter])
          if not condition:
            break
      
      if condition and 'rules' in sr:
        rules = sr['rules']
        
        if 'morph' in rules:
          head, tail, suffix = rules['morph'](head, tail, suffix)
        
        if 'head_names' in rules:
          for i in rules['head_names']:
            head_names[i] = rules['head_names'][i]
        if 'tail_names' in rules:
          for i in rules['tail_names']:
            tail_names[i] = rules['tail_names'][i]
        
        head_separator = rules.get('head_separator', head_separator)
        tail_separator = rules.get('tail_separator', tail_separator)
        
        ordering = rules.get('ordering', ordering)

        spell_zero_head = rules.get('spell_zero_head', spell_zero_head)
        spell_zero_tail = rules.get('spell_zero_tail', spell_zero_tail)
  
  head_phrase = number_name(head, lang, power) if head >= lang.base_number \
                else head_names[head] if head or spell_zero_head \
                else ''
  tail_phrase = number_name(tail, lang) if tail >= lang.base_number \
                else tail_names[tail] if tail or spell_zero_tail \
                else ''
  head_separator = head_separator if head_phrase else ''
  tail_separator = tail_separator if tail_phrase else ''
  
  hp, hs = head_phrase, head_separator
  tp, ts = tail_phrase, tail_separator

  return str.join(
    r'', (hp, hs, tp, ts, suffix) if ordering == 'hts'
    else (suffix, hs, hp, ts, tp) if ordering == 'sht'
    else (tp, ts, suffix, hs, hp) if ordering == 'tsh'
    else (tp, ts, hp, hs, suffix) if ordering == 'ths'
    else (suffix, ts, tp, hs, hp) if ordering == 'sth'
    else (hp, hs, suffix, ts, tp)) # ordering == 'hst'
