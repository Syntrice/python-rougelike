import json
import os

from tcod import tcod

DEFAULT_SETTINGS = {
    "KEYMAP": {
        "MOVE_UP": [tcod.event.KeySym.UP, tcod.event.KeySym.w],
        "MOVE_DOWN": [tcod.event.KeySym.DOWN, tcod.event.KeySym.s],
        "MOVE_LEFT": [tcod.event.KeySym.LEFT, tcod.event.KeySym.a],
        "MOVE_RIGHT": [tcod.event.KeySym.RIGHT, tcod.event.KeySym.d],
        "QUIT": [tcod.event.KeySym.ESCAPE],
    }
}

class Settings:

    @property
    def keymap(self) -> dict[str, object]:
        return self._entries["KEYMAP"]

    def __init__(self, path: str):
        self._entries: dict[str, dict[str, object]] | None = None
        self._path = path
        self._load_settings()
        self._verify_settings()
        self._save_settings()

    def _load_settings(self) -> None:
        if os.path.exists(self._path):
            with open(self._path, "r") as file:
                self._entries = json.load(file)
        else:
            self._entries = {}

    def _verify_settings(self) -> None:
        for section in DEFAULT_SETTINGS.keys():
            if section not in self._entries:
                self._entries[section] = {}
            for key in DEFAULT_SETTINGS[section].keys():
                if key not in self._entries[section]:
                    self._entries[section][key] = DEFAULT_SETTINGS[section][key]


    def _save_settings(self) -> None:
        with open(self._path, "w") as file:
            file.write(json.dumps(self._entries, indent=4))