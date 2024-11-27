from .Attribute import Attribute

class Entity:
    def __init__(self, name: str, *args: Attribute):
        self.name: str = name
        self.attributes: list[Attribute] = list(args)

    def add_attribute(self, attribute: Attribute):
        self.attributes.append(attribute)