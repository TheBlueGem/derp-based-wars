from typing import Tuple


def check_if_tuple_in_list(tup: Tuple[int, int], li) -> bool:
    for elem in li:
        if elem == tup:
            return True
    return False


def get_el_in_both_lists(li1, li2):
    for el in li1:
        if el in li2:
            return el

