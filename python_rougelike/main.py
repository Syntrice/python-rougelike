import tcod.tileset

from python_rougelike.game import Game
from python_rougelike.settings import Settings

def main() -> None:
    game = Game(
        title="Python Rougelike",
        rows=80,
        cols=80,
        tileset=tcod.tileset.load_tilesheet("resources/cp437_8x8.png", 16, 16, tcod.tileset.CHARMAP_CP437),
        vsync=True,
        settings=Settings("settings.json")
    )
    game.run()

if __name__ == "__main__":
    main()