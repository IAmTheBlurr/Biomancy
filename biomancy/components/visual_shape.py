from typing import Optional

from .visual_base import VisualBase


class VisualShape(VisualBase):
    """ Class to represent a visualType on a PowerBI report page """
    def __init__(self, data: dict, directory_path: Optional[str] = None):
        super().__init__(data, directory_path=directory_path)
        self.visual_data: dict = self.raw_data['visual'] if 'visual' in self.raw_data else None
        self.type: str = self.raw_data['visual']['visualType']
        self.objects: Optional[dict[str: dict]] = self.visual_data['objects'] if 'objects' in self.visual_data else None
        self.drill_filter_other_visuals: bool = self.visual_data['drillFilterOtherVisuals'] if 'drillFilterOtherVisuals' in self.visual_data else None
        self.parent_group_name: Optional[str] = self.raw_data['parentGroupName'] if 'parentGroupName' in self.raw_data else None
        self.how_created: str = self.raw_data['howCreated'] if 'howCreated' in self.raw_data else None

    def __repr__(self):
        return f"VisualShape({self.type})"
