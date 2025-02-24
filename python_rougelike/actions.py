from abc import  ABC

class Action(ABC):
    pass

class QuitAction(Action):
    pass

class MoveAction(Action):

    @property
    def dx(self) -> int:
        return self._dx

    @property
    def dy(self) -> int:
        return self._dy

    def __init__(self, dx: int, dy: int):
        super(MoveAction, self).__init__()
        self._dx = dx
        self._dy = dy