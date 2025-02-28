""" Module to represent a visualGroup on a PowerBI report page """
from typing import Optional, Union

from .visual_base import VisualBase
from .visual_shape import VisualShape
from .visual_type import VisualType


class VisualGroup(VisualBase):
    """ Class to represent a visualGroup on a PowerBI report page """
    def __init__(self, data: dict, directory_path: Optional[str] = None):
        super().__init__(data, directory_path=directory_path)
        self.display_name: str = ''
        self.group_mode: str = ''
        self.children: dict = {}
        self.objects: dict = {}
        self.type: str = 'visualGroup'
        self.parent_group_name: None = None

        self.__populate_properties()

    def __repr__(self):
        return f'VisualGroup({self.display_name})'

    def __populate_properties(self) -> None:
        """
        Validate and populate instance properties from the fields expected to be present in the raw data

        Returns:
            None

        """
        if 'visualGroup' not in self.raw_data:
            raise KeyError("Expected Structural Error || Key `visualGroup` expected in data when constructing a VisualGroup object.")

        visual_group = self.raw_data['visualGroup']

        if 'displayName' not in visual_group:
            raise KeyError("Expected Structural Error || Key `displayName` expected in data when constructing a VisualGroup object.")

        if 'groupMode' not in visual_group:
            raise KeyError("Expected Structural Error || Key `groupMode` expected in data when constructing a VisualGroup object.")

        self.display_name = visual_group['displayName']
        self.group_mode = visual_group['groupMode']

        if 'objects' in visual_group:
            self.objects = visual_group['objects']

    def add(self, visual: Union[VisualShape, VisualType]) -> None:
        """
        Add a PowerBI Visual to the visual group

        Args:
            visual (Union[VisualShape, VisualType]): PowerBI Visual being added to the visual group

        Returns:
            None

        """
        self.children[visual.name] = visual
