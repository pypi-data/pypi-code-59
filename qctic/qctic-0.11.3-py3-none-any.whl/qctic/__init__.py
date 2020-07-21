import logging
import sys
import warnings

logger = logging.getLogger(__name__)
logger.addHandler(logging.NullHandler())

# Ignore IBMQ provider warnings
if not sys.warnoptions:
    warnings.filterwarnings(
        "ignore",
        message=r".*qiskit-ibmq-provider.*",
        category=RuntimeWarning)
