""" Module to represent the base class for all PowerBI visual constructs """
from typing import Optional

from .visual_position import VisualPosition


class VisualBase(object):
    """ Base class for PowerBI visual objects """
    def __init__(self, data: dict, directory_path: Optional[str] = None):
        """
        Initialize the VisualBase object

        Args:
            data (dict): The raw data from the PowerBI JSON file.
            directory_path (Optional[str]): The directory path to the PowerBI JSON file.

        """
        self.validate_required_fields(data)
        self.raw_data: dict = data
        self.directory_path: Optional[str] = directory_path

        self.name: str = data['name']
        self.schema: str = data['$schema']
        self.position: VisualPosition = VisualPosition(data['position'])

    def __repr__(self):
        return f"{self.__class__.__name__}({self.name})"

    @property
    def height(self) -> Optional[int]:
        """
        Get the height of the visual

        Returns:
            Optional[int]: The height of the visual

        """
        if not self.position:
            return None

        return self.position.height

    @property
    def width(self) -> Optional[int]:
        """
        Get the width of the visual

        Returns:
            Optional[int]: The width of the visual

        """
        if not self.position:
            return None

        return self.position.width

    @property
    def x(self) -> Optional[int]:
        """
        Get the x-coordinate of the visual

        Returns:
            Optional[int]: The x-coordinate of the visual

        """
        if not self.position:
            return None

        return self.position.x

    @property
    def y(self) -> Optional[int]:
        """
        Get the y-coordinate of the visual

        Returns:
            Optional[int]: The y-coordinate of the visual

        """
        if not self.position:
            return None

        return self.position.y

    @property
    def z(self) -> Optional[int]:
        """
        Get the z-index of the visual

        Returns:
            Optional[int]: The z-index of the visual

        """
        return self.position.z

    @property
    def tab_order(self) -> Optional[int]:
        """
        Get the tab order of the visual

        Returns:
            Optional[int]: The tab order of the visual

        """
        return self.position.tab_order

    @property
    def angle(self) -> Optional[int]:
        """
        Get the angle of the visual

        Returns:
            Optional[int]: The angle of the visual

        """
        return self.position.angle

    @staticmethod
    def validate_required_fields(data: dict) -> None:
        """
        Validate the required property fields of the incoming data

        Args:
            data (dict): The raw data from the PowerBI JSON file

        Returns:
            None

        """
        if not data['name']:
            raise ValueError("Expected Structural Error || `name` expected in the PowerBI JSON file")

        if not data['position']:
            raise ValueError("Expected Structural Error || `position` expected in the PowerBI JSON file")

        if not data['$schema']:
            raise ValueError("Expected Structural Error || `$schema` expected in the PowerBI JSON file")
