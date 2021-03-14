from __future__ import annotations

import time

from experimental.core.renderer import RenderManager
from experimental.core.input import InputController
from experimental.core.screens import ScreenManager
from experimental.core.fps import FPSManager
from experimental.core.clock import ClockManager


class Game:

    _last_update: float

    def __init__(self) -> None:

        self.clock = ClockManager(self)
        self.renderer = RenderManager(self)
        self.screens = ScreenManager(self)
        self.input = InputController(self)
        self.fps = FPSManager(self)

    def start(self) -> None:
        self.renderer.setup()
        self._last_update = time.time()
        self.loop()
        self.renderer.teardown()

    def loop(self) -> None:
        while True:
            now = time.time()
            dt = now - self._last_update
            self.fps.update(dt)
            self.screens.update(dt)
            self.renderer.update(dt)
            self._last_update = now
