from typing import Union


def calculate_fizz_buzz(list_to_fizzbuzz: list[int]) -> list[Union[str, int]]:
    """
    This method returns a copy of the original list but replaces inside this copy:
    numbers that can be divided by 3 and 5 by "fizzbuzz"
    numbers that can be divided by 3 by "fizz"
    number that can be divided by 5 by "buzz"
    :param list_to_fizzbuzz: list of int
    :return: modified copy
    """
    fizz_buzzed_list = []
    for number in list_to_fizzbuzz:
        div_mod_of_3 = divmod(number, 3)
        div_mod_of_5 = divmod(number, 5)
        if div_mod_of_5[1] == 0 and div_mod_of_3[1] == 0:
            fizz_buzzed_list.append("fizzbuzz")
        elif div_mod_of_5[1] == 0:
            fizz_buzzed_list.append("buzz")
        elif div_mod_of_3[1] == 0:
            fizz_buzzed_list.append("fizz")
        else:
            fizz_buzzed_list.append(number)
    return fizz_buzzed_list
