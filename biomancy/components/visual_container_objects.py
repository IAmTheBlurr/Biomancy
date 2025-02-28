""" Module to represent the properties of a visual container """
from ..tools import to_bool


class VisualContainerObjects(object):
    """ Class to represent the properties of a visual container """
    def __init__(self, data: dict):
        self.raw_data: dict = data

        self.background: dict = {}
        self.border: dict = {}
        self.drop_shadow: dict = {}
        self.padding: dict[str, int] = {}
        self.style_preset: dict = {}
        self.title: dict = {}
        self.visual_header: dict = {}
        self.visual_link: dict = {}
        self.visual_tooltip: dict = {}

        self.__populate_from_data(data)

    def __contains__(self, item):
        return item in self.__dict__()

    def __dict__(self) -> dict:
        return dict(
            background=self.background,
            border=self.border,
            drop_shadow=self.drop_shadow,
            padding=self.padding,
            style_preset=self.style_preset,
            title=self.title,
            visual_header=self.visual_header,
            visual_link=self.visual_link,
            visual_tooltip=self.visual_tooltip
        )

    def __getitem__(self, item: str):
        return getattr(self, item)

    def __iter__(self):
        return iter(dict(self).items())

    def __repr__(self):
        return f"VisualContainerProperties({self.raw_data})"

    def __populate_from_data(self, data):
        background = data['background'] if 'background' in data else None
        border = data['border'] if 'border' in data else None
        drop_shadow = data['dropShadow'] if 'dropShadow' in data else None
        padding = data['padding'] if 'padding' in data else None
        title = data['title'] if 'title' in data else None
        visual_header = data['visualHeader'] if 'visualHeader' in data else None
        visual_link = data['visualLink'] if 'visualLink' in data else None
        visual_tooltip = data['visualTooltip'] if 'visualTooltip' in data else None

        self.__set_background(background)
        self.__set_border(border)
        self.__set_drop_shadow(drop_shadow)
        self.__set_padding(padding)
        self.__set_title(title)
        self.__set_visual_header(visual_header)
        self.__set_visual_link(visual_link)
        self.__set_visual_tooltip(visual_tooltip)

    def __set_background(self, data):
        if data:
            properties = data[0]['properties']
            if 'show' in properties:
                self.background['show'] = (properties['show']['expr']['Literal']['Value'])
            if 'transparency' in properties:
                self.background['transparency'] = int(properties['transparency']['expr']['Literal']['Value'][:-1])

    def __set_border(self, data):
        if data:
            properties = data[0]['properties']
            if 'color' in properties:
                self.border['color'] = properties['color']['expr']['Literal']['Value']
            if 'radius' in properties:
                self.border['radius'] = int(properties['radius']['expr']['Literal']['Value'][:-1])
            if 'show' in properties:
                self.border['show'] = to_bool(properties['show']['expr']['Literal']['Value'])
            if 'width' in properties:
                self.border['width'] = int(properties['width']['expr']['Literal']['Value'][:-1])

    def __set_drop_shadow(self, data):
        if data:
            properties = data[0]['properties']
            if 'angle' in properties:
                self.drop_shadow['angle'] = int(properties['angle']['expr']['Literal']['Value'][:-1])
            if 'color' in properties:
                self.drop_shadow['color'] = properties['color']['expr']['Literal']['Value']
            if 'position' in properties:
                self.drop_shadow['position'] = properties['position']['expr']['Literal']['Value']
            if 'preset' in properties:
                self.drop_shadow['preset'] = properties['preset']['expr']['Literal']['Value'].replace("'", "")
            if 'shadowBlur' in properties:
                self.drop_shadow['shadowBlur'] = int(properties['shadowBlur']['expr']['Literal']['Value'][:-1])
            if 'shadowDistance' in properties:
                self.drop_shadow['shadowDistance'] = int(properties['shadowDistance']['expr']['Literal']['Value'][:-1])
            if 'shadowSpread' in properties:
                self.drop_shadow['shadowSpread'] = int(properties['shadowSpread']['expr']['Literal']['Value'][:-1])
            if 'show' in properties:
                self.drop_shadow['show'] = to_bool(properties['show']['expr']['Literal']['Value'])
            if 'transparency' in properties:
                self.drop_shadow['transparency'] = int(properties['transparency']['expr']['Literal']['Value'][:-1])

    def __set_padding(self, data):
        if data:
            properties = data[0]['properties']
            if 'top' in properties:
                self.padding['top'] = int(properties['top']['expr']['Literal']['Value'][:-1])
            if 'right' in properties:
                self.padding['right'] = int(properties['right']['expr']['Literal']['Value'][:-1])
            if 'bottom' in properties:
                self.padding['bottom'] = int(properties['bottom']['expr']['Literal']['Value'][:-1])
            if 'left' in properties:
                self.padding['left'] = int(properties['left']['expr']['Literal']['Value'][:-1])

    def __set_title(self, data):
        if data:
            properties = data[0]['properties']
            if 'text' in properties:
                self.title['text'] = properties['text']['expr']['Literal']['Value'].replace("'", "")
            if 'show' in properties:
                self.title['show'] = to_bool(properties['show']['expr']['Literal']['Value'])
            if 'italic' in properties:
                self.title['italic'] = properties['italic']['expr']['Literal']['Value']
            if 'alignment' in properties:
                self.title['alignment'] = properties['alignment']['expr']['Literal']['Value'].replace("'", "")

    def __set_visual_header(self, data):
        if data:
            properties = data[0]['properties']
            if 'show' in properties:
                self.visual_header['show'] = to_bool(properties['show']['expr']['Literal']['Value'])
            if 'showSmartNarrativeButton' in properties:
                self.visual_header['showSmartNarrativeButton'] = properties['showSmartNarrativeButton']['expr']['Literal']['Value']

    def __set_visual_link(self, data):
        if data:
            properties = data[0]['properties']
            if 'show' in properties:
                self.visual_link['show'] = to_bool(properties['show']['expr']['Literal']['Value'])
            if 'type' in properties:
                self.visual_link['type'] = properties['type']['expr']['Literal']['Value'].replace("'", "")

    def __set_visual_tooltip(self, data):
        if data:
            properties = data[0]['properties']
            if 'show' in properties:
                self.visual_tooltip['show'] = to_bool(properties['show']['expr']['Literal']['Value'])
            if 'type' in properties:
                self.visual_tooltip['type'] = properties['type']['expr']['Literal']['Value'].replace("'", "")

    def keys(self):
        """ Return the keys of the properties """
        return self.__dict__().keys()