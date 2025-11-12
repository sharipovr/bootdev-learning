from bank_account import BankAccount


run_cases = [
    {
        "title": "Deposit and withdraw (happy path)",
        "accounts": [("alice", "Alice", 100)],
        "operations": [
            ("deposit", "alice", 50),
            ("withdraw", "alice", 30),
        ],
        "expected_balances": {"alice": 120},
        "expected_results": [True, True],
    },
    {
        "title": "Transfer funds (happy path)",
        "accounts": [("alice", "Alice", 200), ("bob", "Bob", 20)],
        "operations": [("transfer", "alice", "bob", 50)],
        "expected_balances": {"alice": 150, "bob": 70},
        "expected_results": [True],
    },
    {
        "title": "Withdraw overdraft (should fail)",
        "accounts": [("charlie", "Charlie", 10)],
        "operations": [("withdraw", "charlie", 20)],
        "expected_balances": {"charlie": 10},
        "expected_results": [False],
    },
]

submit_cases = run_cases + [
    {
        "title": "Deposit zero (invalid)",
        "accounts": [("dana", "Dana", 5)],
        "operations": [("deposit", "dana", 0)],
        "expected_balances": {"dana": 5},
        "expected_results": [False],
    },
    {
        "title": "Transfer exceeds balance (should fail)",
        "accounts": [("ed", "Ed", 30), ("fran", "Fran", 100)],
        "operations": [("transfer", "ed", "fran", 50)],
        "expected_balances": {"ed": 30, "fran": 100},
        "expected_results": [False],
    },
    {
        "title": "Multiple ops end state (happy path)",
        "accounts": [("gina", "Gina", 300), ("harry", "Harry", 0)],
        "operations": [
            ("withdraw", "gina", 40),    # 260
            ("transfer", "gina", "harry", 100),  # gina:160, harry:100
            ("deposit", "harry", 50),     # harry:150
            ("withdraw", "harry", 25),    # harry:125
        ],
        "expected_balances": {"gina": 160, "harry": 125},
        "expected_results": [True, True, True, True],
    },
]


def run_scenario(case):
    accounts = {}
    for key, owner, start in case["accounts"]:
        accounts[key] = BankAccount(owner, start)

    results = []
    for op in case["operations"]:
        if op[0] == "deposit":
            _, who, amt = op
            res = accounts[who].deposit(amt)
            results.append(res)
        elif op[0] == "withdraw":
            _, who, amt = op
            res = accounts[who].withdraw(amt)
            results.append(res)
        elif op[0] == "transfer":
            _, src, dst, amt = op
            res = accounts[src].transfer_to(accounts[dst], amt)
            results.append(res)

    balances = {}
    for key in accounts:
        balances[key] = accounts[key].get_balance()

    return results, balances


def print_case_io(case, results, balances):
    print("---------------------------------")
    print(case["title"])
    print("Input:")
    print("  Accounts:")
    for key, owner, start in case["accounts"]:
        print(f"    - {key} => owner: {owner}, starting_balance: {start}")
    print("  Operations:")
    for op in case["operations"]:
        if op[0] == "deposit":
            _, who, amt = op
            print(f"    - deposit({who}, {amt})")
        elif op[0] == "withdraw":
            _, who, amt = op
            print(f"    - withdraw({who}, {amt})")
        elif op[0] == "transfer":
            _, src, dst, amt = op
            print(f"    - transfer({src} -> {dst}, {amt})")
    print("")
    print(f"Expected results:  {case['expected_results']}")
    print(f"Actual results:    {results}")
    print(f"Expected balances: {case['expected_balances']}")
    print(f"Actual balances:   {balances}")


def test_case(case):
    results, balances = run_scenario(case)
    print_case_io(case, results, balances)
    ok = results == case["expected_results"] and balances == case["expected_balances"]
    if ok:
        print("Pass")
    else:
        print("Fail")
    return ok


def main():
    passed = 0
    failed = 0
    skipped = len(submit_cases) - len(test_cases)

    for case in test_cases:
        correct = test_case(case)
        if correct:
            passed += 1
        else:
            failed += 1

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
