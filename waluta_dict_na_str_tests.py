import main

assert main.waluta_dict_na_str( {'galeon': 0, 'sykl': 0, 'knut': 50}) == '2 sykl 8 knut'
assert main.waluta_dict_na_str( {'galeon': 0, 'sykl': 0, 'knut': 13}) == '13 knut'
assert main.waluta_dict_na_str({'galeon': 5, 'sykl': 0, 'knut': 13}) == '5 galeon 13 knut'
assert main.waluta_dict_na_str({'galeon': 0, 'sykl': 5, 'knut': 0}) == '5 sykl'