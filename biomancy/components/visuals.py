""" Module to represent a collection of PowerBI visuals """
import json
import os

from typing import Union

from .visual_group import VisualGroup
from .visual_shape import VisualShape
from .visual_type import VisualType


class Visuals(object):
    """ Class to represent a collection of PowerBI visuals """
    def __init__(self):
        self.ordered_visuals: list[Union[VisualType, VisualShape, VisualGroup]] = []
        self.hashes: list[str] = []

    def __getitem__(self, item):
        return self.ordered_visuals[item]

    def __iter__(self) -> iter:
        return iter(self.ordered_visuals)

    def __len__(self):
        return len(self.ordered_visuals)

    def __repr__(self):
        return f"Visuals({len(self.ordered_visuals)})"

    @staticmethod
    def __init_visual_from_directory(directory_path: str) -> Union[VisualType, VisualShape, VisualGroup]:
        """
        Read the JSON file and populate the raw_data property

        Args:
            directory_path (str): the directory path which contains the PowerBI JSON file.

        Returns:
            None

        """
        file_path = os.path.join(directory_path, 'visual.json')

        if not os.path.exists(file_path):
            raise FileNotFoundError(
                f"Expected Structural Error || `visual.json` expected at {file_path}, not found")

        with open(file_path) as visual_json_file:
            data = json.load(visual_json_file)

            if 'visualGroup' in data:
                return VisualGroup(data, directory_path=directory_path)
            elif 'visual' in data:
                if data['visual']['visualType'] == 'shape':
                    return VisualShape(data, directory_path=directory_path)
                else:
                    return VisualType(data, directory_path=directory_path)
            else:
                raise ValueError(f'Expected Visual Type || `visual` or `visualGroup` not found when constructing *Visual Object, inspect raw data -- {data}.')

    def get_unique_types(self) -> list[str]:
        """ Get a list of unique visual types """
        return list(set(visual.type for visual in self.ordered_visuals))

    def add(self, visual_path: str) -> Union[VisualType, VisualShape, VisualGroup]:
        """ Add a visual to the list of visuals """
        visual = self.__init_visual_from_directory(visual_path)

        if not visual:
            raise ValueError(f"Expected Structural Error || Visual object not created for {visual_path}")

        self.ordered_visuals.append(visual)
        self.hashes.append(visual.name)

        return visual

    def get_by_hash(self, hash_value: str) -> Union[VisualType, VisualShape, VisualGroup]:
        """ Get a visual by its hash """
        if hash_value not in self.hashes:
            raise IndexError(f"Hash {hash_value} not found in the list of hashes")

        return self.ordered_visuals[self.hashes.index(hash_value)]
