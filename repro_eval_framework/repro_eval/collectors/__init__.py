from .base import Collector
from .agent import AgentCollector
from .bnn_rds import BnnRdsCollector
from .figures import FigureCollector

DEFAULT_COLLECTORS = [BnnRdsCollector(), FigureCollector(), AgentCollector()]

__all__ = ["Collector", "AgentCollector", "BnnRdsCollector", "FigureCollector", "DEFAULT_COLLECTORS"]
