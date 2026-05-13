"""
Kronos - Time Series Prediction Library

A fork of shiyu-coder/Kronos with enhancements for Chinese and global
stock market prediction using transformer-based models.

Modules:
    model     - Core Kronos transformer model
    data      - Data loading and preprocessing utilities
    predict   - Prediction and forecasting utilities
    utils     - Helper functions and visualization tools
"""

__version__ = "0.2.0"
__author__ = "Kronos Contributors"
__license__ = "MIT"

from kronos.predict import KronosPredictor
from kronos.data import StockDataLoader

__all__ = [
    "KronosPredictor",
    "StockDataLoader",
    "__version__",
]
