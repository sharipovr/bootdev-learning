def compute_totals(lines):
    totals = {}
    skipped = 0

    for line in lines:
        line = str.strip(line)
        if line == "" or line[0] == "#":
            continue
        parts = line.split(",")
        if len(parts) != 3:
            skipped += 1
            continue
        item = str.strip(parts[0])
        if item == '':
            skipped += 1
            continue

        try:
          qty = int(str.strip(parts[1]))
          price = int(parts[2]) if len(parts) > 2 else 0
          total = qty * price
        except ValueError:
          skipped += 1
          continue
      
        if item in totals:
            totals[item] = totals[item] + total
        else:
            totals[item] = total

    return (totals, skipped)