from __future__ import annotations
from typing import TYPE_CHECKING, Optional

from experimental.abstracts import AbstractScreen, T

if TYPE_CHECKING:
    from experimental.core.screens import ScreenManager
    from experimental.core.game import Game


class BaseMenu(AbstractScreen):

    name: str = "BASE MENU"

    def __init__(self, manager: ScreenManager) -> None:
        super().__init__(manager)
        self.game: Game = manager.game
        self.panels = []

    def on_enter(self, *args) -> None:
        self.game.renderer.clear()
        self.game.renderer.refresh()

    def on_leave(self) -> None:
        pass

    def on_draw(self, dt) -> None:
        self.game.renderer.clear()
        self.game.renderer.print_big(5, 5, 0xFFFFFFFF, "Anathema")

    def on_update(self, dt) -> None:
        self.handle_input()

    def cmd_move(self, x: int, y: int) -> Optional[T]:
        pass

    def cmd_confirm(self):
        print("command confirm")

    def cmd_escape(self) -> None:
        raise SystemExit()

