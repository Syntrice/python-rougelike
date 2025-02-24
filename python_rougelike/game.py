from __future__ import annotations

import tcod.context
from tcod.tileset import Tileset

from python_rougelike.actions import MoveAction, QuitAction
from python_rougelike.input_handlers import EventHandler
from python_rougelike.settings import Settings


class Game:

    def __init__(self) -> None:
        self._vsync: bool = False
        self._title: str = None
        self._tileset: Tileset = None
        self._height: int = None
        self._width: int = None
        self._settings: Settings = None
        self._event_handler: EventHandler = None

    def _configure_services(self) -> None:
        if self._title is None: raise Exception("Title must be set.")
        if self._tileset is None: raise Exception("Tileset must be set.")
        if self._height is None: raise Exception("Height must be set.")
        if self._width is None: raise Exception("Width must be set.")
        if self._settings is None: raise Exception("Settings must be set.")

        self._event_handler = EventHandler(self._settings)

    def run(self) -> None:

        self._configure_services()

        player_x = int(self._width / 2)
        player_y = int(self._height / 2)

        with tcod.context.new_terminal(
                self._width,
                self._height,
                tileset=self._tileset,
                title=self._title,
                vsync=self._vsync
        ) as context:
            root_console = tcod.console.Console(self._width, self._height, order="F")
            while True:
                root_console.print(x=player_x, y=player_y, string="@")
                context.present(root_console)

                root_console.clear()

                for event in tcod.event.wait():
                    action = self._event_handler.dispatch(event)

                    if action is None:
                        continue

                    if isinstance(action, MoveAction):
                        player_x += action.dx
                        player_y += action.dy

                    elif isinstance(action, QuitAction):
                        raise SystemExit()

    def stop(self) -> None:
        raise SystemExit

    def set_screen_size(self, width: int, height: int) -> Game:
        self._width = width
        self._height = height
        return self

    def set_tileset(self, tileset: Tileset) -> Game:
        self._tileset = tileset
        return self

    def set_title(self, title: str) -> Game:
        self._title = title
        return self

    def use_vsync(self) -> Game:
        self._vsync = True
        return self

    def load_settings(self, path: str) -> Game:
        self._settings = Settings(path)
        return self
