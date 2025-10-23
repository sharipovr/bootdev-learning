from fizz_buzz_range_builder import fizzbuzz_range

run_cases = [
    (1, 10, "1 2 Fizz 4 Buzz Fizz 7 8 Fizz Buzz"),
    (3, 5, "Fizz 4 Buzz"),
    (15, 16, "FizzBuzz 16"),
]

submit_cases = run_cases + [
    (5, 3, ""),
    (15, 15, "FizzBuzz"),
    (-3, 3, "Fizz -2 -1 FizzBuzz 1 2 Fizz"),
]


def test(start, end, expected_output):
    print("---------------------------------")
    print(f"Input: start={start}, end={end}")
    result = fizzbuzz_range(start, end)
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
