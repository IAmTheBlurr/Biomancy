

class Fill(object):
    def __init__(self, color: str):
        self.color = color

    def to_json(self):
        return {"fill": self.color}