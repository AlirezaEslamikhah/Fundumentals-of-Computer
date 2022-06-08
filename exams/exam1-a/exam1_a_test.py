import exam1_a

def test_q7_get_new_fib_array():
    nums = exam1.q7_get_new_fib_array(2, 3, 4)
    assert nums == [2, 3, 2*3-2, 3*4-2]

    nums = exam1.q7_get_new_fib_array(3, 4, 6)
    assert nums == [3, 4, 12-2, 4*10-2, 10*38-2, 38*378-2]

# def test_q8_get_phone_numbers():
#     queries = ["Ali", "Zohre"]
#     phone_numbers = exam1.q8_get_phone_numbers("phonebook1.txt", queries)
#     assert len(phone_numbers) == 2
#     assert phone_numbers[0] == "09122331415"
#     assert phone_numbers[1] == "03113421541"

#     queries = ["Zhila", "zhila", "Mojdeh"]
#     phone_numbers = exam1.q8_get_phone_numbers("phonebook1.txt", queries)
#     assert len(phone_numbers) == 3
#     assert phone_numbers[0] == "09153332231"
#     assert phone_numbers[1] == "09153332231"
#     assert phone_numbers[2] == "na"

#     queries = ["Francesco Pera", "Tomi Minasian", "Theodore Ty"]
#     phone_numbers = exam1.q8_get_phone_numbers("phonebook2.txt", queries)
#     assert phone_numbers == ["076019 168 24-53", "0049 6316259", "07814 352-7 85"] 