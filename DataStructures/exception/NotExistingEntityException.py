from DataStructures.Entity import Entity
from exception import ERDiagramException


class NotExistingEntityException(ERDiagramException):
    def __init__(self, entity: Entity):
        super().__init__(f"Entity {entity.name} doesn't exist")
