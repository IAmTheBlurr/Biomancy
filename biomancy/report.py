""" Module to represent a PBIP directory containing PowerBI pages and their visuals """
import json
import os

from typing import Optional, Union

from biomancy.components import Page, Pages, VisualGroup, VisualShape, VisualType


class Report(object):
    """ Class to represent a PBIP directory containing PowerBI pages """
    def __init__(self, directory_path: str, ignored_pages: Optional[list[str]] = None):
        self.directory_path = directory_path
        self.ignored_pages: list[str] = ignored_pages if ignored_pages else []
        self.ordered_pages = []
        self.pages: Pages = Pages()

        if not os.path.exists(directory_path):
            raise FileNotFoundError(f"Expected Structure Error || Target directory {directory_path} not found")

        self.__get_page_order()

        for page_hash in self.ordered_pages:
            if not os.path.isdir(os.path.join(self.directory_path, page_hash)):
                raise FileNotFoundError(f"Expected Structure Error || Page directory {page_hash} not found")

            page = Page(os.path.join(self.directory_path, page_hash))

            if self.ignored_pages and self.is_ignored(page.display_name):
                continue

            self.pages.add(page)

    def __len__(self):
        return len(self.pages)

    def __repr__(self):
        return f'Report({len(self.pages)})'

    def __get_page_order(self):
        """
        Grabs the order of the pages from the pages.json file

        Returns:
            None

        """
        with open(os.path.join(self.directory_path, 'pages.json')) as pages_json:
            data = json.load(pages_json)
            self.ordered_pages = data['pageOrder']

    def get_all_visuals_of_type(self, visual_type: str) -> list[Union[VisualGroup, VisualShape, VisualType]]:
        """
        Returns the data for all visuals of the specified type

        Args:
            visual_type: The type of visual to search for

        Returns:
            A list of instantiated Visual objects

        """
        visuals_data = []
        for page in self.pages:
            for visual in page.visuals:
                if visual == visual_type:
                    visuals_data.append(visual)

        return visuals_data

    def get_page_json(self, display_name: str) -> dict:
        """
        Get the raw data for a page by its display name

        Args:
            display_name: The display name of the page

        Returns:
            dict: The raw data for the page

        """
        return self.pages[display_name].raw_data

    def get_all_pages_json(self) -> list[dict]:
        """
        Get the raw data for all pages

        Returns:
            list[dict]: A list of raw data for all pages

        """
        return [page.raw_data for page in self.pages]

    def is_ignored(self, display_name: str) -> bool:
        """
        Check if the page is in the ignored pages list

        Args:
            display_name:

        Returns:
            bool: True if the page is in the ignored pages list, False otherwise

        """
        return display_name in self.ignored_pages

    def get_all_relevant_visuals(self) -> dict[str, list[VisualType]]:
        """
        Get all visuals that are not shapes or groups

        Returns:
            dict[str, list[VisualType]]: A list of VisualType objects

        """
        relevant_types = {}
        for page in self.pages:
            for visual in page.visuals:
                if visual.type != 'shape' and visual.type != 'visualGroup':
                    if visual.type not in relevant_types:
                        relevant_types[visual.type] = [visual]
                    else:
                        relevant_types[visual.type].append(visual)

        return relevant_types
