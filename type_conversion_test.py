# Type Conversion Reality Check

tests = [
    ("int → float", lambda: float(5)),
    ("int → str", lambda: str(5)),
    ("int → bool", lambda: bool(5)),
    ("int → list", lambda: list(5)),
    ("int → tuple", lambda: tuple(5)),

    ("float → int", lambda: int(3.7)),
    ("float → str", lambda: str(3.7)),
    ("float → bool", lambda: bool(2.5)),
    ("float → list", lambda: list(3.7)),
    ("float → tuple", lambda: tuple(3.7)),

    ("str → int", lambda: int("123")),
    ("str → float", lambda: float("3.14")),
    ("str → bool", lambda: bool("False")),
    ("str → list", lambda: list("abc")),
    ("str → tuple", lambda: tuple("abc")),

    ("bool → int", lambda: int(True)),
    ("bool → float", lambda: float(True)),
    ("bool → str", lambda: str(True)),
    ("bool → list", lambda: list(True)),
    ("bool → tuple", lambda: tuple(False)),

    ("list → tuple", lambda: tuple([1, 2])),
    ("list → str", lambda: str([1, 2])),
    ("list → int", lambda: int([1, 2])),
    ("list → float", lambda: float([1, 2])),
    ("list → bool", lambda: bool([])),

    ("tuple → list", lambda: list((1, 2))),
    ("tuple → str", lambda: str((1, 2))),
    ("tuple → int", lambda: int((1, 2))),
    ("tuple → float", lambda: float((1, 2))),
    ("tuple → bool", lambda: bool(())),
]

for label, test in tests:
    try:
        result = test()
        print(f"{label:<15}: SUCCESS → {result}")
    except Exception as e:
        print(f"{label:<15}: ERROR → {type(e).__name__}")