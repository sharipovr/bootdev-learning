from settings_fileparser import load_settings

run_cases = [
    (
        """# Game settings
player_name =   Aria  
max_health=120

  # graphics options
fullscreen = true
resolution = 1920x1080
""",
        {
            "player_name": "Aria",
            "max_health": "120",
            "fullscreen": "true",
            "resolution": "1920x1080",
        },
    ),
    (
        """# simple single line
name = DungeonCrawler
""",
        {"name": "DungeonCrawler"},
    ),
]

submit_cases = run_cases + [
    (
        """# duplicate keys
volume = 50
volume = 75
""",
        {"volume": "75"},
    ),
    (
        """# mixed spacing and comments
  # comment line
 music_enabled= true  

music_volume =   80
sound_effects =off
""",
        {
            "music_enabled": "true",
            "music_volume": "80",
            "sound_effects": "off",
        },
    ),
    (
        """# lines without equals should be ignored
broken_line
another:broken
key = value
""",
        {"key": "value"},
    ),
]


def test(file_text, expected_output):
    print("---------------------------------")
    print("Input file text:\n")
    print(file_text)
    result = load_settings(file_text)
    print("\nExpected:")
    print(expected_output)
    print("Actual:")
    print(result)
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
