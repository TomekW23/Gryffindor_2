from main import wyslij_sowe
from unittest.mock import patch

class MockInput:
    def __init__(self, inputs):
        self.inputs = inputs
    
    def __call__(self, prompt):
        return next(self.inputs)

def generate_test_data():
    while True:
        yield ["Harry", "Podejdź tu"]

dane_testowe = generate_test_data()
sukcesy = 0
niepowodzenia = 0

with patch('builtins.input', MockInput(dane_testowe)):
    for _ in range(100):
        adresat, tresc = next(dane_testowe)
        wysylam_list = wyslij_sowe(adresat, tresc)
        if wysylam_list:
            sukcesy += 1
        else:
            niepowodzenia += 1

expected_weights = (90, 10)  # Oczekiwane wagi

actual_ratio = niepowodzenia / sukcesy
expected_ratio = expected_weights[1] / expected_weights[0]


if abs(actual_ratio - expected_ratio) < 0.1:  
    print("Stosunek niepowodzeń do sukcesów jest zgodny z oczekiwaniami.")
else:
    print("Stosunek niepowodzeń do sukcesów nie jest zgodny z oczekiwaniami.")
