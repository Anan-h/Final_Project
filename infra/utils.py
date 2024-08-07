import string
import random
from enum import Enum


class Utils:

    @staticmethod
    def generate_random_string(length):
        """
        a function to generate a random string
        :param length: the amount of characters in the string
        :return: a string text
        """
        chars = string.ascii_letters
        return ''.join((random.choice(chars) for i in range(length)))

    @staticmethod
    def generate_random_value_of_enum(enum: Enum):
        """
        a function to generate a random value from enum object
        :param enum: the desired object
        :return: a random value from the object
        """
        return random.choice(list(enum)).value
