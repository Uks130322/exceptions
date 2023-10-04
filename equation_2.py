from math import sin

def equation_2(a=input("A = ")) -> str:
    """
    Find the root of equation A * (A - 1) * x = sin(A)
    """

    try:
        a = float(a)
        return str(sin(a) / (a * (a - 1)))

    except ZeroDivisionError:
        if a == 0:
            return "-1.0"
        else:
            return "x does not exist"

    except:
        return "Something wrong with numbers"

print(equation_2())

TEST_CASES = [
    {"a": 3, "result": "0.0235200013433112"},
    {"a": "0","result": "-1.0"},
    {"a": "a", "b": 5, "result": "Something wrong with numbers"},
    {"a": 1, "result": "x does not exist"}
    ]
    

def test_equation_2():
    for case in TEST_CASES:
        assert equation_2(case["a"]) == case["result"]
        print(f"Equation {case['a']} * ({case['a']} - 1) * x = sin({case['a']}) PASS")

test_equation_2()        
