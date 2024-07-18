try:
    from loguru import logger
except ImportError:
    from unittest.mock import Mock

    logger = Mock(trace=print, debug=print, info=print, warning=print, error=print)
