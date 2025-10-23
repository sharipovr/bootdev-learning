def join_strings(strings):
    result = ""

    for i in range(0, len(strings)):
        result += strings[i]
        if i != len(strings)-1:
          result += ","            

    return result