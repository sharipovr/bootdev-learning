def tally_loot(items):
  result = {}

  for  i in range(0,len(items)):
    item = items[i].lower()
    if item in result:
      index = result[item]
      result[item] = index + 1
    else:
      result[item] = 1
  return result


def merge_counts(a, b):
  result = {}

  for item in a:
    result[item] = a[item]
    
  for item in b:
    if item in result:
      result[item] += b[item]
    else:
      result[item] = b[item]

  return result

