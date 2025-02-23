from __future__ import annotations

import tcod.context
from tcod.tileset import Tileset

class Game:

    def __init__(self) -> None:
        self._vsync = False
        self._title = None
        self._tileset = None
        self._height = None
        self._width = None

    def run(self) -> None:

        if self._title is None: raise Exception("Title must be set.")
        if self._tileset is None: raise Exception("Tileset must be set.")
        if self._height is None: raise Exception("Height must be set.")
        if self._width is None: raise Exception("Width must be set.")

        with tcod.context.new_terminal(
            self._width,
            self._height,
            tileset=self._tileset,
            title=self._title,
            vsync=self._vsync
        ) as context:
            root_console = tcod.console.Console(self._width, self._height, order="F")
            while True:
                root_console.print(x=1, y=1, string="@")
                context.present(root_console)

                for event in tcod.event.wait():
                    if event.type == "QUIT":
                        self.stop()
                        return

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
        return  self




