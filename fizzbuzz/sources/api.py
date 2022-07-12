from typing import Union

FIZZ_MULTIPLIER = 3

BUZZ_MULTIPLIER = 5

FIZZ = "fizz"

BUZZ = "buzz"


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
        fizz_buzz_value = ""
        if is_multiple_of(number, FIZZ_MULTIPLIER):
            fizz_buzz_value += FIZZ
        if is_multiple_of(number, BUZZ_MULTIPLIER):
            fizz_buzz_value += BUZZ
        if fizz_buzz_value == "":
            fizz_buzzed_list.append(number)
        else:
            fizz_buzzed_list.append(fizz_buzz_value)
    return fizz_buzzed_list


def is_multiple_of(number_to_test: int, multiplier: int) -> bool:
    return divmod(number_to_test, multiplier)[1] == 0
