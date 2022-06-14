from cgi import print_form
import unittest
from snail_print import snail_print, RLL

from io import StringIO
import sys


class Capturing(list):
    def __enter__(self):
        self._stdout = sys.stdout
        sys.stdout = self._stringio = StringIO()
        return self

    def __exit__(self, *args):
        self.extend(self._stringio.getvalue().splitlines())
        del self._stringio  # free up some memory
        sys.stdout = self._stdout


def example_input_to_one_string(example_input, sep):
    if type(example_input) is tuple:
        return sep.join([str(i) for i in example_input])
    return str(example_input)


def expected_output(example_input, sep=" "):
    string_input = example_input_to_one_string(example_input, sep)
    return [string_input[0 : i + 1] for i in range(len(string_input))]


# TO DO: Fix this function and make it not use set()
def back_slash_n_expected_output(example_input):
    example_input = example_input.split("\n")
    list_ = []
    for j in range(len(example_input)):
        for k in range(len(example_input[0 : j + 1])):
            word = example_input[k]
            if k == j:
                for i in range(len(word)):
                    list_.append(word[0 : i + 1])
                list_.append("")
            else:
                list_.append(word)
    return list_


def captured_output(example_input, sep=" ", end="\n"):
    with Capturing() as output:
        if type(example_input) is tuple:
            snail_print(*example_input, sep=sep, end=end)
        else:
            snail_print(example_input, sep=sep, end=end)
    output = [i.strip(RLL) for i in output]
    return output


class ValidationTests(unittest.TestCase):
    def test_simple_case(self):
        example_input = "hola"

        output_1 = expected_output(example_input)
        output_2 = captured_output(example_input)

        self.assertEqual(output_1, output_2)

    def test_mutiple_objects(self):
        example_input = "hola", "mundo"

        output_1 = expected_output(example_input)
        output_2 = captured_output(example_input)

        self.assertEqual(output_1, output_2)

    def test_special_characters(self):
        example_input = "¿cómo están?"

        output_1 = expected_output(example_input)
        output_2 = captured_output(example_input)

        self.assertEqual(output_1, output_2)

    def test_mutiple_objects_and_special_characters(self):
        example_input = "bien", "y tú"

        output_1 = expected_output(example_input)
        output_2 = captured_output(example_input)

        self.assertEqual(output_1, output_2)

    def test_numbers(self):
        example_input = 34567

        output_1 = expected_output(example_input)
        output_2 = captured_output(example_input)

        self.assertEqual(output_1, output_2)

    def test_mutiple_objects_and_numbers(self):
        example_input = 3, "+", 4, "=", 7

        output_1 = expected_output(example_input)
        output_2 = captured_output(example_input)

        self.assertEqual(output_1, output_2)

    def test_class_str(self):
        class Class_1:
            def __init__(self, name):
                self.name = name

            def __str__(self):
                return self.name

        example_input = Class_1("Sophia")

        output_1 = expected_output(example_input)
        output_2 = captured_output(example_input)

        self.assertEqual(output_1, output_2)

    def test_class_repr(self):
        class Class_2:
            def __init__(self, name):
                self.name = name

            def __repr__(self):
                return self.name

        example_input = Class_2("Sophia"), Class_2("Tony"), Class_2("Jack")

        output_1 = expected_output(example_input)
        output_2 = captured_output(example_input)

        self.assertEqual(output_1, output_2)

    def test_sep(self):
        example_input = "hola", "mundo"
        sep = "+"

        output_1 = expected_output(example_input, sep=sep)
        output_2 = captured_output(example_input, sep=sep)

        self.assertEqual(output_1, output_2)

    def test_large_case(self):
        example_input = "h" * 50

        output_1 = expected_output(example_input)
        output_2 = captured_output(example_input)

        self.assertEqual(output_1, output_2)

    def test_end_1(self):
        example_input = "hola"
        end = ""

        output_1 = expected_output(example_input)
        output_2 = captured_output(example_input, end=end)

        self.assertEqual(output_1, output_2)

    def test_end_2(self):
        example_input_1 = "hola"
        end = ""
        example_input_2 = "chao"

        example_input = example_input_1 + end + example_input_2[0]
        output_X = expected_output(example_input)
        output_X.pop(len(output_X) - 2)

        example_input = example_input_2[1::]
        output_Y = expected_output(example_input)
        output_Y = ["c" + s for s in output_Y]

        output_1 = output_X + output_Y

        with Capturing() as output_2:
            snail_print(example_input_1, end=end)
            snail_print(example_input_2)
        output_2 = [i.strip(RLL) for i in output_2]

        self.assertEqual(output_1, output_2)

    def test_end_3(self):
        example_input_1 = "hola"
        end = ""
        example_input_2 = "chao"

        example_input = example_input_2[1::]
        output_1 = expected_output(example_input)
        output_1 = ["c" + s for s in output_1]
        output_1.insert(0, example_input_1 + example_input_2[0])

        with Capturing() as output_2:
            print(example_input_1, end=end)
            snail_print(example_input_2)
        output_2 = [i.strip(RLL) for i in output_2]

        self.assertEqual(output_1, output_2)

    def test_1_back_slash_n(self):
        example_input = "Hola\nComo"

        output_1 = set(back_slash_n_expected_output(example_input))
        output_2 = set(captured_output(example_input))

        self.assertEqual(output_1, output_2)

    def test_multiple_back_slash_n(self):
        example_input = "Hola\nComo\nEstas"

        output_1 = set(back_slash_n_expected_output(example_input))
        output_2 = set(captured_output(example_input))

        self.assertEqual(output_1, output_2)

    def test_delay_type(self):
        with Capturing() as _:
            snail_print("hola", delay=0.1)
            snail_print("hola", delay=1)

        test_ended = True

        self.assertTrue(test_ended)

    def test_validation(self):
        with self.assertRaises(TypeError):
            snail_print("hola", delay="random_string")
            snail_print("hola", delay=1234)
            snail_print("hola", end=1234)
            snail_print("hola", flush=1234)


if __name__ == "__main__":
    unittest.main()
