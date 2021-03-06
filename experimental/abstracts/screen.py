from __future__ import annotations
from typing import TYPE_CHECKING, Optional
from abc import ABC

from experimental.core.input import T, StateBreak

if TYPE_CHECKING:
    from experimental.core.screens import ScreenManager
    from experimental.core.game import Game


class AbstractScreen:

    name: str

    def __init__(self, manager: ScreenManager) -> None:
        self.manager = manager
        self.game: Game = manager.game

    def handle_input(self) -> None:
        command = self.game.input.handle_input()
        if not command:
            return
        command()

    def on_enter(self, *args):
        pass

    def on_leave(self):
        pass

    def on_draw(self, dt) -> None:
        pass

    def on_update(self, dt):
        pass

    def cmd_confirm(self) -> Optional[T]:
        """
        [ENTER]
        Context: DEFAULT
        """

    def cmd_escape(self) -> Optional[T]:
        """
        [ESCAPE]
        Context: DEFAULT
        """
        raise StateBreak()

    def cmd_move(self, x: int, y: int) -> Optional[T]:
        """
        Arrow Keys, Keypad
        Context: DEFAULT
        """

    def cmd_drop(self) -> Optional[T]:
        """
        Default: [D]
        Context: STAGE
        """

    def cmd_equipment(self) -> Optional[T]:
        """
        Default: [E]
        Context: STAGE
        """

    def cmd_examine(self) -> Optional[T]:
        """
        Default: [L]
        Context: STAGE
        """

    def cmd_inventory(self) -> Optional[T]:
        """
        Default: [I]
        Context: STAGE
        """

    def cmd_pickup(self) -> Optional[T]:
        """
        Default: [G]
        Context: STAGE
        """

    def cmd_quit(self) -> Optional[T]:
        """
        Default: [Q],
        Context: MAIN_MENU
        """
        raise SystemExit()
