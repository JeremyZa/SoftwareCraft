from fizzbuzz.sources.api import calculate_fizz_buzz


def test_basic_case():
    list_for_test = [i for i in range(100)]
    fizz_buzzed_result = calculate_fizz_buzz(list_for_test)

    for i in list_for_test:
        div_mod_of_3 = divmod(i, 3)
        div_mod_of_5 = divmod(i, 5)
        if div_mod_of_3[1] == 0 and div_mod_of_5[1] == 0:
            assert fizz_buzzed_result[i] == "fizzbuzz"
        elif div_mod_of_3[1] == 0:
            assert fizz_buzzed_result[i] == "fizz"
        elif div_mod_of_5[1] == 0:
            assert fizz_buzzed_result[i] == "buzz"
        else:
            assert fizz_buzzed_result[i] == i
