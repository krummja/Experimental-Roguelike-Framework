from __future__ import annotations

import math
from collections import deque
from functools import reduce
from typing import TYPE_CHECKING

from experimental.abstracts import AbstractManager

if TYPE_CHECKING:
    from experimental.core.game import Game


class FPSManager(AbstractManager):

    def __init__(self, game: Game) -> None:
        super().__init__(game)
        self.frame_count = 60
        self.fps = 0
        self.frames = deque([])
        for _ in range(self.frame_count):
            self.frames.append(0)

    def update(self, dt) -> None:
        self.frames.append(1000 / dt)
        self.frames.popleft()
        frame_sum = reduce((lambda s, v : s + v), self.frames)
        fps = math.trunc((frame_sum / self.frame_count) / 1000)
        self.fps = fps
