def count_vowels(text):
    vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
    counter = 0
    unique_vowels = set()

    for c in text:
        if c in vowels:
            counter += 1
            unique_vowels.add(c)

    return counter, unique_vowels