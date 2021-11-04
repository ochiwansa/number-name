from math import floor, log10

def number_name(n, rule):
  if n < 0:
    return rule.negative_phrase + ' ' + number_name(-n, rule)
  
  if n < 10:
    return rule.unit_names[n]
  
  max_digit = max([*rule.suffixes]) + rule.digit_grouping
  digit = floor(log10(n)) + 1
  
  if digit > max_digit:
    raise ValueError
  
  power = digit - 1
  if power > rule.digit_grouping:
    power //= rule.digit_grouping
    power *= rule.digit_grouping
  divisor = pow(10, power)
  
  head = n // divisor
  tail = n % divisor
  
  nr = rule.non_regular(digit, head, tail)
  head = nr.get('head', head)
  tail = nr.get('tail', tail)
  
  suffix = nr.get('suffix', rule.suffixes[power])
  
  default_separator = rule.separator if hasattr(rule, 'separator') else ' '
  head_separator = nr.get('head_separator', default_separator)
  tail_separator = nr.get('tail_separator', default_separator)
  
  head_names = nr.get('head_names', dict())
  head_names = [head_names.get(n, name)
                for n, name in enumerate(rule.unit_names)]
  tail_names = nr.get('tail_names', dict())
  tail_names = [tail_names.get(n, name)
                for n, name in enumerate(rule.unit_names)]
  
  default_ordering = rule.ordering if hasattr(rule, 'ordering') else 'hst'
  ordering = nr.get('ordering', default_ordering)
  
  spell_zero_tail = nr.get('spell_zero_tail', False)
  
  head_phrase = number_name(head, rule) if head >= 10 \
                else head_names[head]
  tail_phrase = number_name(tail, rule) if tail >= 10 \
                else tail_names[tail] if tail or spell_zero_tail \
                else ''
  head_separator = head_separator if head_phrase else ''
  tail_separator = tail_separator if tail_phrase else ''
  
  return tail_phrase + tail_separator + suffix + head_separator + head_phrase \
      if ordering == 'tsh' \
    else head_phrase + head_separator + tail_phrase + tail_separator + suffix \
      if ordering == 'hts' \
    else tail_phrase + tail_separator + head_phrase + head_separator + suffix \
      if ordering == 'ths' \
    else suffix + head_separator + head_phrase + tail_separator + tail_phrase \
      if ordering == 'sht' \
    else suffix + tail_separator + tail_phrase + head_separator + head_phrase \
      if ordering == 'sth' \
    else head_phrase + head_separator + suffix + tail_separator + tail_phrase
      #  ordering == 'hst' (default)
