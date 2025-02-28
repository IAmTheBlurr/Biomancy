""" Class to represent a PowerBI page """
import json
import os

from .visual_type import VisualType
from .visual_group import VisualGroup
from .visual_groups import VisualGroups
from .visuals import Visuals


class Page(object):
    """ Class to represent a PowerBI page """
    def __init__(self, directory_path: str):
        self.raw_data = {}
        self.directory_path: str = directory_path
        self.display_name: str = ''
        self.file_path: str = os.path.join(directory_path, 'page.json')
        self.hash: str = os.path.basename(directory_path)
        self.visuals: Visuals = Visuals()
        self.visuals_directories: list[str] = []

        self.visual_groups: VisualGroups = VisualGroups()

        if not os.path.exists(directory_path):
            raise FileNotFoundError(f"Expected Structural Error || Target directory {directory_path} not found")

        with open(self.file_path) as page_json_file:
            self.raw_data = json.load(page_json_file)

        self.display_name = self.raw_data['displayName'] if 'displayName' in self.raw_data else ''
        self.objects = self.raw_data.get('objects', []) if 'objects' in self.raw_data else []

        self.__populate_visuals_data()
        self.__construct_groups()

    def __len__(self):
        return len(self.visuals)

    def __repr__(self):
        return f'Page({self.display_name})'

    def __get_visuals_directories(self):
        visuals_dir = os.path.join(self.directory_path, 'visuals')
        if not os.path.exists(visuals_dir):
            return

        self.visuals_directories = [
            directory for directory in os.listdir(visuals_dir) if os.path.isdir(os.path.join(visuals_dir, directory))
        ]

    def __populate_visuals_data(self):
        if not self.visuals_directories:
            self.__get_visuals_directories()

        for visual_dir in self.visuals_directories:
            visual_json_path = os.path.join(self.directory_path, 'visuals', visual_dir)

            if not os.path.exists(visual_json_path):
                continue

            created_visual = self.visuals.add(visual_json_path)

            if isinstance(created_visual, VisualGroup):
                self.visual_groups.add(created_visual)

    def __construct_groups(self):
        for visual in self.visuals:
            if not isinstance(visual, VisualGroup) and visual.parent_group_name and visual.parent_group_name in self.visual_groups:
                self.visual_groups[visual.parent_group_name].add(visual)

    def visuals_by_type(self, visual_type: str) -> list[VisualType]:
        """ Get all visuals of a specific type from all pages """
        return [visual for visual in self.visuals if visual.type == visual_type]
