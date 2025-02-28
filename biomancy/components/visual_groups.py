""" Module to represent a collection of PowerBI visual groups """
from .visual_group import VisualGroup


class VisualGroups(object):
    """ Class to represent a collection of PowerBI visual groups """
    def __init__(self):
        self.__groups: dict[str, VisualGroup] = {}
        self.hash_names: list[str] = []
        self.display_names: list[str] = []

    def __getitem__(self, item):
        if isinstance(item, int):
            return self.__groups[self.hash_names[item]]

        if item in self.hash_names:
            return self.__groups[item]

        if item in self.display_names:
            return self.__groups[self.hash_names[self.display_names.index(item)]]

        return self.__groups[item]

    def __iter__(self) -> iter:
        return iter(self.__groups)

    def __len__(self):
        return len(self.__groups)

    def __repr__(self):
        return f'VisualGroups({len(self.__groups)})'

    def add(self, group: VisualGroup):
        """ Add a visual group to the list of visual groups """
        self.__groups[group.name] = group
        self.display_names.append(group.display_name)
        self.hash_names.append(group.name)
