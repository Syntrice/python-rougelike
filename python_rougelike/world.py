from python_rougelike.entity import Entity

class World:
    def __init__(self, width: int, height: int) -> None:
        """
        Represents the game world
        Args:
            width: width of the world in tiles
            height: height of the world in tiles
        """
        self._width = width
        self._height = height
        self.player = Entity(int(width / 2), int(height / 2), "@", (255, 255, 255))
        self.npc = Entity(int(width / 2 - 5), int(height / 2), "@", (255, 255, 0))
        self.entities = {self.npc, self.player}
