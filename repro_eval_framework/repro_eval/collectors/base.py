from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Any

from ..schema import CollectorResult, DiscoveredFile, EvalConfig


class Collector(ABC):
    name = "collector"

    @abstractmethod
    def collect(self, config: EvalConfig, truth_spec: Any, discovered: list[DiscoveredFile]) -> CollectorResult:
        raise NotImplementedError

