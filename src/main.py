"""
Smart Cat Door System
An AI-powered pet door controller using computer vision and multi-factor authentication
to selectively grant access to specific cats while keeping out unwanted animals.

This module serves as the central controller, orchestrating all subsystems including
authentication, sensors, hardware control, and notifications. It maintains the main
event loop and handles high-level system coordination.
"""

import logging
from auth import CatAuthenticator
from sensors import MotionDetector
from hardware import DoorController
from notifications import NotificationSystem

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class SmartDoorSystem:
    def __init__(self):
        self.auth = CatAuthenticator()
        self.sensors = MotionDetector()
        self.door = DoorController()
        self.notifier = NotificationSystem()

    def run(self):
        if self.sensors.detect_motion():
            logger.info("Motion detected, starting authentication")
            if self.auth.authenticate():
                self.door.open()
                self.notifier.send("Cat authenticated, door opened")
