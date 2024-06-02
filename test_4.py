print("hello")
from main import wybierz_sowe_zwroc_koszt
from main import wybierz_sowe_zwroc_koszt
from main import wybierz_sowe_zwroc_koszt
from main import licz_sume
import main

def test_wybierz_sowe_zwroc_koszt():
    test_cases = [
        ((False, "lokalna", "list"), {"galeon": 0, "sykl": 0, "knut": 2}),
        ((False, "lokalna", "paczka"), {"galeon": 0, "sykl": 0, "knut": 7}),
        ((False, "krajowa", "list"), {"galeon": 0, "sykl": 1, "knut": 2}),
        ((False, "krajowa", "paczka"), {"galeon": 0, "sykl": 2, "knut": 1}),
        ((False, "dalekobiezna", "list"), {"galeon": 0, "sykl": 2, "knut": 0}),
        ((False, "dalekobiezna", "paczka"), {"galeon": 0, "sykl": 4, "knut": 0}),
        ((True, "lokalna", "list"), {"galeon": 0, "sykl": 0, "knut": 9}),
        ((False, "lokalna", "list", "wyjec"), {"galeon": 0, "sykl": 0, "knut": 6})
    ]

    for input_args, expected_output in test_cases:
        output = wybierz_sowe_zwroc_koszt(*input_args)
        assert output == expected_output, f"For {input_args}, expected {expected_output} but got {output}"

    print("All tests passed!")

test_wybierz_sowe_zwroc_koszt()


