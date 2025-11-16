from calculator import calculator 

def test_add_first():
    calc = calculator()
    assert calc.add(1, 1) == 2
