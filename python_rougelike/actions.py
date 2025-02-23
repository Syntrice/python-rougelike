from abc import  ABC

class Action:
    pass

class QuitAction(Action):
    pass

class MoveAction(Action):

    @property
    def dx(self) -> int:
        return self._dx

    @dx.setter
    def dx(self, value: object) -> None:
        self._dx = value

    @property
    def dy(self) -> int:
        return self._dy

    @dy.setter
    def dy(self, value: object) -> None:
        self._dy = value

    def __init__(self, dx: int, dy: int):
        super(MoveAction, self).__init__()
        self._dx = dx
        self._dy = dy