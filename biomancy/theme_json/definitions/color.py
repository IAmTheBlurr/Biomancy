""" Module to define the Color class. """
import re


class Color(object):
    """ Class to represent a color """
    PATTERN: str = "^#[0-9a-fA-F]{8}$|^#(?:[0-9a-fA-F]{3}){1,2}$"

    def __init__(self, value: str):
        self.__validate(value)
        self.__value = value

    def __call__(self):
        return self.__value

    def __eq__(self, other):
        if isinstance(other, Color):
            return self.__value == other.__value
        return str(self) == other

    def __get__(self, instance, owner):
        return self.__value

    def __repr__(self):
        return f"Color('{self.__value}')"

    def __str__(self):
        return self.__value

    def __validate(self, color: str):
        if not re.match(self.PATTERN, color):
            raise ValueError(f"Invalid color format: {color}")

    def set(self, value) -> None:
        """
        Set the color value.

        Args:
            value (str): The color value.

        Returns:
            None

        """
        self.__validate(value)
        self.__value = value

    def to_json(self) -> dict:
        """
        Returns the color as a JSON object.

        Returns:
            dict: The color as a JSON object.

        """
        return {"color": self.__value}
