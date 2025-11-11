from fix_purchaselog_parser import compute_totals

run_cases = [
    (
        [
            "apple,2,3",
            "banana,1,5",
            "apple,1,3",
        ],
        ({"apple": 9, "banana": 5}, 0),
    ),
    (
        [
            "# cart",
            "  apple , 2 , 4 ",
            "",
            "banana,3,2",
            " #ignored",
            "banana, 1 , 2 ",
        ],
        ({"apple": 8, "banana": 8}, 0),
    ),
]

submit_cases = run_cases + [
    (
        [
            "orange, two, 3",
            "grape,1",
            "melon,2,4,extra",
            ",1,2",
            "peach,5,1",
            "peach, x ,1",
            "#end",
        ],
        ({"peach": 5}, 5),
    ),
    (
        ["#", "", "bad,line", "ok,1,notint"],
        ({}, 2),
    ),
    (
        [
            "bread,2,3",
            "milk,1,4",
            "bread,3,3",
            "eggs,12,1",
            "#discount day",
            "milk,2,4",
        ],
        ({"bread": 15, "milk": 12, "eggs": 12}, 0),
    ),
]


def show_input(lines):
    print("Input lines:")
    for idx, line in enumerate(lines):
        print(f"  {idx}: {repr(line)}")


def test(lines, expected_output):
    print("---------------------------------")
    show_input(lines)
    print("")
    result = compute_totals(lines)
    print(f"Expected: {expected_output}")
    print(f"Actual:   {result}")
    if result == expected_output:
        return True
    return False


def main():
    passed = 0
    failed = 0
    skipped = len(submit_cases) - len(test_cases)
    for test_case in test_cases:
        correct = test(*test_case)
        if correct:
            passed += 1
            print("Pass")
        else:
            failed += 1
            print("Fail")
    if failed == 0:
        print("============= PASS ==============")
    else:
        print("============= FAIL ==============")
    if skipped > 0:
        print(f"{passed} passed, {failed} failed, {skipped} skipped")
    else:
        print(f"{passed} passed, {failed} failed")


test_cases = submit_cases
if "__RUN__" in globals():
    test_cases = run_cases

main()
