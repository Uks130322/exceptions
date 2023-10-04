def diapason(first=input("Please enter first number: "),
             second=input("Please enter second number: ")) -> str:

    """
    Read two values. Return integer numbers from minimum
    to maximum number. If was entered not int or float
    return error message.
    """

    
    try:
        
        first, second = float(first), float(second)
        first, second = min(first, second), max(first, second)
        first = int(first) + bool(first - int(first)) * (first > 0)
        second = int(second) + 1
        
        return " ".join([str(number) for number in range(first, second)])

    except:
        
        return "Something wrong with numbers"


print(diapason())


TEST_CASES = [
    {"first": 1, "second": 1, "result": "1"},
    {"first": 1, "second": 5, "result": "1 2 3 4 5"},
    {"first": -3, "second": 2, "result": "-3 -2 -1 0 1 2"},
    {"first": 1.2, "second": 5.3, "result": "2 3 4 5"},
    {"first": -3.1, "second": 1, "result": "-3 -2 -1 0 1"},
    {"first": 1, "second": -4.3, "result": "-4 -3 -2 -1 0 1"},
    {"first": 1, "second": "a", "result": "Something wrong with numbers"}
    ]
    


def test_diapason():
    for case in TEST_CASES:
        assert diapason(case["first"], case["second"]) == case["result"]
        print("pass")

test_diapason()
