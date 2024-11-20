"""
Hardware Control Module
Manages physical components including door servo motor, speakers, and LED indicators.
Handles fail-safe operations and emergency override functionality.
"""

from enum import Enum
import logging
logger = logging.getLogger(__name__)

class DoorState(Enum):
    OPEN = "open"
    CLOSED = "closed"

class DoorController:
    def open(self):
        logger.info("Opening door")
