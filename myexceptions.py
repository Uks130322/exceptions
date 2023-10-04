def summa(*args) -> int:
    """
    Calculate sum of integer objects in args
    """
    
    class IntError(Exception):
        pass
    
    final = 0
    
    for item in args:
        try:
            if isinstance(item, float):
                raise IntError
            final += item

        except:
            pass

    return final

print(summa(1, 2.5, "me", 8, [14, 15], "one", "6"))


TEST_CASES = [
    {"lst": [], "result": 0},
    {"lst": ["a", "b"], "result": 0},
    {"lst": [3.5, 1.7], "result": 0},
    {"lst": [3, 1], "result": 4},
    {"lst": [3.5, 1.7, "a", [16], 24, 0, "b"], "result": 24}
    ]


###TEST###

def test_summa():
    for case in TEST_CASES:
        assert case["result"] == summa(*case["lst"])
        print("pass")

test_summa()
