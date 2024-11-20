"""
Sensor Interface Module
Manages all physical sensors including motion detection, weight measurement,
and audio recording. Handles sensor calibration and provides cleaned data
to other modules.
"""

import logging
logger = logging.getLogger(__name__)

class MotionDetector:
    def detect_motion(self) -> bool:
        # Check PIR sensor
        return True
