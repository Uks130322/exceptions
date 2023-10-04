def equation(a=input("A = "), b=input("B = ")) -> str:
    """
    Find the root of equation (A^2 - 1) * x = B
    """

    try:
        a, b = float(a), float(b)
        return str(b / (a ** 2 - 1))

    except ZeroDivisionError:
        if b == 0:
            return "x is any number"
        else:
            return "x does not exist"

    except:
        return "Something wrong with numbers"

print(equation())

TEST_CASES = [
    {"a": 2, "b": 6, "result": "2.0"},
    {"a": 3, "b": 2.7, "result": "0.3375"},
    {"a": "5", "b": 6, "result": "0.25"},
    {"a": "a", "b": 5, "result": "Something wrong with numbers"},
    {"a": -7, "b": 0, "result": "0.0"},
    {"a": 1, "b": 0, "result": "x is any number"},
    {"a": -1, "b": 3.2, "result": "x does not exist"}
    ]
    

def test_equation():
    for case in TEST_CASES:
        assert equation(case["a"], case["b"]) == case["result"]
        print(f"Equation ({case['a']}^2 - 1) * x = {case['b']} PASS")

test_equation()        
