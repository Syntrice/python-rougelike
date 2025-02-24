from tcod.console import Console
from tcod.context import Context

from python_rougelike.actions import MoveAction, QuitAction
from python_rougelike.input_handlers import EventHandler
from python_rougelike.world import World
from typing import Iterable, Any


class Engine:
    def __init__(self, event_handler: EventHandler, world: World) -> None:
        """
        The main game engine class. It is responsible for processing events dispatched through EventHandler, and
        rendering to the console.
        Args:
            event_handler: event handler instance dependency injection
            world: world instance dependency injection
        """
        self._world = world
        self._event_handler = event_handler


    def handle_events(self, events: Iterable[Any]) -> bool:
        """
        Process events via first dispatching them to Actions via EventHandler
        Args:
            events: the list of tcod events to process

        Returns: a boolean indicating whether the game should continue running or not
        """
        for event in events:
            action = self._event_handler.dispatch(event)

            if action is None:
                continue

            if isinstance(action, MoveAction):
                self._world.player.move(action.dx, action.dy)

            elif isinstance(action, QuitAction):
                return False

        return True

    def render(self, console: Console, context: Context) -> None:
        """
        Render the world state to the specified console and context
        Args:
            console: the console to render to
            context: the context to render to
        """
        for entity in self._world.entities:
            console.print(entity.x, entity.y, entity.char, fg=entity.color)
        context.present(console)
        console.clear()