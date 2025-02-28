""" Module to represent a collection of PowerBI pages """
from typing import Optional, Union

from .page import Page
from .visual_group import VisualGroup
from .visual_shape import VisualShape
from .visual_type import VisualType


class Pages(object):
    """ Class to represent a collection of PowerBI pages """
    def __init__(self):
        self.__pages: list[Page] = []
        self.display_names: list[str] = []
        self.hashes: list[str] = []

    def __getitem__(self, item: Union[int, str]) -> Optional[Page]:
        if isinstance(item, int):
            return self.__pages[item]

        if item in self.hashes:
            return self.__pages[self.hashes.index(item)]

        if item in self.display_names:
            return self.__pages[self.display_names.index(item)]

        return None

    def __iter__(self):
        return iter(self.__pages)

    def __len__(self):
        return len(self.__pages)

    def __repr__(self):
        return f'Pages({len(self.__pages)})'

    def __list__(self):
        return self.__pages

    def add(self, page: Page):
        """ Add a page to the list of pages """
        self.__pages.append(page)
        self.display_names.append(page.display_name)
        self.hashes.append(page.hash)

    def get_all_visuals(self) -> list[Union[VisualGroup, VisualShape, VisualType]]:
        """ Get all visuals from all pages """
        return [visual for page in self.__pages for visual in page.visuals]

    def get_all_visuals_by_type(self, visual_type: str) -> list[Union[VisualGroup, VisualShape, VisualType]]:
        """ Get all visuals of a specific type from all pages """
        return [visual for page in self.__pages for visual in page.visuals if visual.type == visual_type]

    def visual_occurrences_count(self) -> dict[str, int]:
        """
        Count the number of occurrences of each visual in all pages

        Returns:
            A dictionary containing the count of occurrences of each visual

        """
        visual_occurrences = {}
        for page in self.__pages:
            for visual in page.visuals:
                if visual.visual_type not in visual_occurrences:
                    visual_occurrences[visual.visual_type] = 1
                else:
                    visual_occurrences[visual.visual_type] += 1

        return visual_occurrences

    def unique_visuals_per_page_count(self) -> dict[str, int]:
        """
        Count the number of unique visuals in each page

        Returns:
            A dictionary containing the count of unique visuals in each page

        """
        return {page.display_name: len(page.visuals.get_unique_types()) for page in self.__pages}
