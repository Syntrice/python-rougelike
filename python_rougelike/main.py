import tcod.tileset

from python_rougelike.game import Game


def main() -> None:
    game = Game()
    game.set_title("Python Rougelike")
    game.set_screen_size(80, 50)
    game.set_tileset(tcod.tileset.load_tilesheet("resources/cp437_8x8.png", 16, 16, tcod.tileset.CHARMAP_CP437))
    game.use_vsync()
    game.run()

if __name__ == "__main__":
    main()