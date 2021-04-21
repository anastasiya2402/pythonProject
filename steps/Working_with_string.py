import unittest


class MyTestCase(unittest.TestCase):
    def test_string(self):
        my_string = "ewqpru32094u230ewhjr0349rhwe09r3490wsdfpj3409t30f3409f"
        string_char = list(my_string)
        print(string_char)
        ['e', 'w', 'q', 'p', 'r', 'u', '3', '2', '0', '9', '4', 'u', '2', '3', '0', 'e', 'w', 'h', 'j', 'r', '0', '3',
         '4', '9', 'r', 'h', 'w', 'e', '0', '9', 'r', '3', '4', '9', '0', 'w', 's', 'd', 'f', 'p', 'j', '3', '4', '0',
         '9', 't', '3', '0', 'f', '3', '4', '0', '9', 'f']

        print(len(string_char))
        54

        string_numbers=[]
        for i in range(6,11):
            string_numbers.append(string_char[i])

        for i in range(12,15):
            string_numbers.append(string_char[i])

        for i in range(20,24):
            string_numbers.append(string_char[i])

        for i in range(28,30):
            string_numbers.extend(string_char[i])

        for i in range(31,35):
            string_numbers.extend(string_char[i])

        for i in range(41,45):
            string_numbers.extend(string_char[i])

        for i in range(46,48):
            string_numbers.extend(string_char[i])

        for i in range(49,53):
            string_numbers.extend(string_char[i])
        print(string_numbers)


