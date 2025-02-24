from typing import Tuple


class Entity:

    def __init__(self, x: int, y: int, char: str, foreground: Tuple[int, int, int]):
        """
        Represents an entity in the game world
        Args:
            x: x coordinate
            y: y coordinate
            char: the char to when rendering the entity to the console
            foreground: the foreground color of the char to use when rendering the entity to the console
            TODO background: the background color of the char to use when rendering the entity to the console
        """
        self.x = x
        self.y = y
        self.char = char
        self.color = foreground

    def move(self, dx: int, dy: int) -> None:
        """
        Moves an entity by delta x and delta y
        Args:
            dx: distance to move in tiles in the x direction
            dy: distance to move in tiles in the y direction
        """
        self.x += dx
        self.y += dy