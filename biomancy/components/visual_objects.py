""" Module to represent the internal properties of a visual on a PowerBI report page """


class VisualObjects(object):
    """ Class to represent the internal properties of a visual on a PowerBI report page """
    def __init__(self, data: dict):
        self.raw_data: dict = data

        self.shadow_custom = None
        self.category_axis = None
        self.zoom = None
        self.image_scaling = None
        self.y1_axis_reference_line = None
        self.ribbon_bands = None
        self.selection = None
        self.spacing = None
        self.data = None
        self.error = None
        self.labels = None
        self.column_width = None
        self.icon = None
        self.label = None
        self.outline = None
        self.value = None
        self.legend = None
        self.map_controls = None
        self.column_formatting = None
        self.data_point = None
        self.column_headers = None
        self.bubble_layer = None
        self.y2_axis = None
        self.value_axis = None
        self.shape_custom_rectangle = None
        self.line_styles = None
        self.image = None
        self.padding = None
        self.reference_line = None
        self.items = None
        self.indicator = None
        self.selection_icon = None
        self.header = None
        self.markers = None
        self.analysis = None
        self.series_labels = None
        self.tree = None
        self.layout = None
        self.general = None
        self.fill_custom = None
