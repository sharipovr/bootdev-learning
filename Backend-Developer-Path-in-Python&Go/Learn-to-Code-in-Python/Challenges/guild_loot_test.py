from guild_loot import *

# Run cases (happy paths)
run_cases_tally = [
    (["Gold", "gold", "Potion", "GOLD"], {"gold": 3, "potion": 1}),
    (["Arrow", "arrow", "arrow", "Bow"], {"arrow": 3, "bow": 1}),
]

run_cases_merge = [
    ({"gold": 3, "potion": 1}, {"potion": 4, "elixir": 2}, {"gold": 3, "potion": 5, "elixir": 2}),
    ({"arrow": 2}, {"bow": 1}, {"arrow": 2, "bow": 1}),
]

# Submit cases (include edges, end on big happy path)
submit_cases_tally = run_cases_tally + [
    ([], {}),
    (["Elixir", "ELIXIR", "elixir", "eLiXiR"], {"elixir": 4}),
]

submit_cases_merge = run_cases_merge + [
    ({}, {}, {}),
    ({"coin": 10}, {}, {"coin": 10}),
    ({}, {"gem": 5}, {"gem": 5}),
    (
        {"gold": 7, "potion": 2, "arrow": 10},
        {"potion": 3, "elixir": 4, "arrow": 1},
        {"gold": 7, "potion": 5, "elixir": 4, "arrow": 11},
    ),
]


def test_tally(input_items, expected_output):
    print("---------------------------------")
    print(f"Input items: {input_items}")
    result = tally_loot(input_items)
    print(f"Expected: {expected_output}")
    print(f"Actual:   {result}")
    if result == expected_output:
        print("Pass")
        return True
    print("Fail")
    return False


def test_merge(a, b, expected_output):
    print("---------------------------------")
    print("Input:")
    print(f"  Left:  {a}")
    print(f"  Right: {b}")
    result = merge_counts(a, b)
    print(f"Expected: {expected_output}")
    print(f"Actual:   {result}")
    if result == expected_output:
        print("Pass")
        return True
    print("Fail")
    return False


def main():
    tally_cases = submit_cases_tally
    merge_cases = submit_cases_merge

    if "__RUN__" in globals():
        tally_cases = run_cases_tally
        merge_cases = run_cases_merge

    passed = 0
    failed = 0

    print("Testing tally_loot...")
    for case in tally_cases:
        if test_tally(*case):
            passed += 1
        else:
            failed += 1
    print("")

    print("Testing merge_counts...")
    for case in merge_cases:
        if test_merge(*case):
            passed += 1
        else:
            failed += 1

    if failed == 0:
        print("============= PASS ==============")
    else:
        print("============= FAIL ==============")

    total = len(tally_cases) + len(merge_cases)
    skipped = (len(submit_cases_tally) + len(submit_cases_merge)) - total
    if skipped > 0:
        print(f"{passed} passed, {failed} failed, {skipped} skipped")
    else:
        print(f"{passed} passed, {failed} failed")


main()
