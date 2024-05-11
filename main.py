import math

def waluta_dict_na_str(waluta_dict: dict) -> str:
    knut = waluta_dict["knut"] % 17
    sykl_raw = waluta_dict["sykl"] + math.floor(waluta_dict["knut"]/17)
    sykl = sykl_raw % 21
    galeon = waluta_dict["galeon"]+math.floor(sykl_raw/21)
    response_list = []
    if galeon != 0:
        response_list.append(f"{galeon} galeon")
    if sykl !=0:
        response_list.append(f"{sykl} sykl")
    if knut != 0:
        response_list.append(f"{knut} knut")
    response = ' '.join(response_list)

    return response

