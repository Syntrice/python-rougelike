from __future__ import annotations

import tcod.context
from tcod.tileset import Tileset
from python_rougelike.engine import Engine
from python_rougelike.input_handlers import EventHandler
from python_rougelike.settings import Settings
from python_rougelike.world import World

class Game:

    def __init__(
            self,
            title: str,
            tileset: Tileset,
            rows: int,
            cols: int,
            settings: Settings,
            vsync: bool = False
    ) -> None:
        """
        Manages a game instance, including setting up tcod and resolving dependencies
        Args:
            title: the game title
            tileset: a tcod tileset
            rows: the number of console rows
            cols: the number of console columns
            settings: a settings object, containing customizable user settings
            vsync: whether to run in vsync or not
        """
        self._vsync: bool = vsync
        self._title: str = title
        self._tileset: Tileset = tileset
        self._rows: int = rows
        self._cols: int = cols
        self._settings: Settings = settings
        self._context: tcod.context.Context | None = None

    def _setup(self) -> None:
        """
        Setup critical services and dependencies for DI.
        """
        self._context = tcod.context.new_terminal(
            self._cols,
            self._rows,
            tileset=self._tileset,
            title=self._title,
            vsync=self._vsync)
        self._root_console = tcod.console.Console(self._cols, self._rows, order="F")
        self._event_handler = EventHandler(self._settings)
        self._world = World(self._rows, self._cols)
        self._engine = Engine(self._event_handler, self._world)

    def run(self) -> None:
        """
        Run the game. Will exit if engine returns false on handle events.
        """
        self._setup()
        running = True
        while running:
            self._engine.render(console=self._root_console, context=self._context)
            events = tcod.event.wait()
            running = self._engine.handle_events(events)
        self._context.close()
        raise SystemExit()
