""" Module to represent the position of a visual on a PowerBI report page """
from typing import Optional


class VisualPosition(object):
    """ Class to represent the position of a visual on a PowerBI report page """
    def __init__(self, data: dict):
        self.validate_required_fields(data)

        self.height: int = data['height']
        self.width: int = data['width']
        self.x: int = data['x']
        self.y: int = data['y']

        self.z: Optional[int] = data['z'] if 'z' in data else None
        self.tab_order: Optional[int] = data['tabOrder'] if 'tabOrder' in data else None
        self.angle: Optional[int] = data['angle'] if 'angle' in data else None

    @staticmethod
    def validate_required_fields(data: dict) -> None:
        """
        Validate the required property fields of the incoming data

        Args:
            data (dict): The raw data from the PowerBI JSON file.

        Returns:
            None

        """
        if 'height' not in data:
            raise KeyError("Expected Structural Error || Key `height` expected in data when constructing a VisualPosition object.")

        if 'width' not in data:
            raise KeyError("Expected Structural Error || Key `width` expected in data when constructing a VisualPosition object.")

        if 'x' not in data:
            raise KeyError("Expected Structural Error || Key `x` expected in data when constructing a VisualPosition object.")

        if 'y' not in data:
            raise KeyError("Expected Structural Error || Key `y` expected in data when constructing a VisualPosition object.")


