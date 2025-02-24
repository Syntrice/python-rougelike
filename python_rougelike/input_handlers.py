from tcod import tcod

from python_rougelike.actions import Action, MoveAction, QuitAction
from python_rougelike.settings import Settings

class EventHandler(tcod.event.EventDispatch[Action]):

    def __init__(self, settings: Settings):
        self._settings = settings

    def ev_quit(self, event: tcod.event.Quit) -> Action | None:
        raise SystemExit()

    def ev_keydown(self, event: tcod.event.KeyDown) -> Action | None:
        action: Action | None = None

        key = event.sym

        if key in self._settings.keymap["MOVE_UP"]:
            action = MoveAction(dx=0, dy=-1)
        elif key in self._settings.keymap["MOVE_DOWN"]:
            action = MoveAction(dx=0, dy=1)
        elif key in self._settings.keymap["MOVE_LEFT"]:
            action = MoveAction(dx=-1, dy=0)
        elif key in self._settings.keymap["MOVE_RIGHT"]:
            action = MoveAction(dx=1, dy=0)
        elif key in self._settings.keymap["QUIT"]:
            action = QuitAction()

        # No valid key was pressed
        return action