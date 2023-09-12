# Credit to ChatGPT


class Utils:
    @staticmethod
    def reverse_number(number):
        if isinstance(number, int):
            sign = -1 if number < 0 else 1
            reversed_number = int(str(abs(number))[::-1]) * sign
            return reversed_number
        else:
            raise ValueError("Input must be an integer")

    @staticmethod
    def format_number(number):
        if isinstance(number, int):
            binary_format = bin(number)
            octal_format = oct(number)
            return binary_format, octal_format
        else:
            raise ValueError("Input must be an integer")
