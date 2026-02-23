
def add(a: int, b: int) -> int:
    return a + b

def substract(a: int, b: int) -> int:
    return a - b

def multiplay(a: int, b: int) -> int:
    return a * b

def divide(a: int, b: int) -> int:
    return a // b


# ----------------------------------------------------

# Test

def test_add() -> None:
    assert add(1, 2) == 3

def test_substract() -> None:
    assert substract(1, 2) == -1

def test_multyplay() -> None:
    assert multiplay(10, 2) == 20

def test_divide() -> None:
    assert divide(10, 2) == 5



