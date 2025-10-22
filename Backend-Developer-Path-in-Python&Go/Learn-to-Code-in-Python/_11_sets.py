def remove_duplicates(spells):
    result = set()
    unique_spells = []
    for spell in spells:
        if spell not in result:
            result.add(spell)
            unique_spells.append(spell)

    return unique_spells