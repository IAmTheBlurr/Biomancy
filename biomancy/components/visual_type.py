""" Module to represent a visualType on a PowerBI report page """
from typing import Optional

from .visual_base import VisualBase
from .visual_container_objects import VisualContainerObjects


class VisualType(VisualBase):
    """ Class to represent a visualType on a PowerBI report page """
    def __init__(self, data: dict, directory_path: Optional[str] = None):
        super().__init__(data, directory_path=directory_path)
        self.drill_filter_other_visuals: bool = data['visual']['drillFilterOtherVisuals'] if 'drillFilterOtherVisuals' in data['visual'] else None
        self.filterConfig: dict = self.raw_data['filterConfig'] if 'filterConfig' in self.raw_data else None
        self.objects: Optional[dict[str: dict]] = data['visual']['objects'] if 'objects' in data['visual'] else None
        self.parent_group_name: Optional[str] = self.raw_data['parentGroupName'] if 'parentGroupName' in self.raw_data else None
        self.query: dict = data['visual']['query'] if 'query' in data['visual'] else None
        self.type: str = data['visual']['visualType']
        self.visual_container_objects: VisualContainerObjects = VisualContainerObjects(data['visual']['visualContainerObjects']) if 'visualContainerObjects' in data['visual'] else None

        self.next_object_properties = [
            'shadowCustom', 'categoryAxis', 'zoom', 'imageScaling', 'y1AxisReferenceLine',
            'ribbonBands', 'selection', 'spacing', 'data', 'error', 'labels', 'columnWidth', 'icon',
            'label', 'outline', 'value', 'legend', 'mapControls', 'columnFormatting', 'dataPoint',
            'columnHeaders', 'bubbleLayer', 'y2Axis', 'valueAxis', 'shapeCustomRectangle',
            'lineStyles', 'image', 'padding', 'referenceLine', 'items', 'indicator', 'selectionIcon',
            'header', 'markers', 'analysis', 'seriesLabels', 'tree', 'layout', 'general',
            'fillCustom'
        ]

    def __contains__(self, item):
        return item in self.__dict__()

    def __dict__(self) -> dict:
        return dict(
            drill_filter_other_visuals=self.drill_filter_other_visuals,
            filterConfig=self.filterConfig,
            objects=self.objects,
            parent_group_name=self.parent_group_name,
            query=self.query,
            type=self.type,
            visual_container_objects=self.visual_container_objects
        )

    def __repr__(self):
        return f"VisualType({self.type})"
