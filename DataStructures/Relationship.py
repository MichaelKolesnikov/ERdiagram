from .Attribute import Attribute
from .Cardinality import Cardinality

class Relationship:
    def __init__(self, name: str, cardinalities: list[Cardinality], *attributes: Attribute):
        self.name: str = name
        self.cardinalities = cardinalities
        self.attributes: list[Attribute] = list(attributes)

    def add_attribute(self, attribute: Attribute):
        self.attributes.append(attribute)

    def add_cardinality(self, cardinality: Cardinality):
        self.cardinalities.append(cardinality)