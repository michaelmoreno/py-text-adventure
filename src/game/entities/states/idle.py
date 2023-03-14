class Idle(State):
    def __init__(self, entity: Entity):
        self.entity = entity

    def execute(self) -> None:
        if self.entity.location.