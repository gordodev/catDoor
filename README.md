# catDoor
An AI-powered pet door system using computer vision and multi-factor authentication to selectively grant access to specific cats while keeping out unwanted visitors. Built with Python, OpenCV, and Raspberry Pi

Smart Cat Door Controller
An AI-powered pet door system using computer vision and multi-factor authentication to selectively grant access to specific cats while keeping out unwanted visitors. Built with Python, OpenCV, and Raspberry Pi.
Features

Facial recognition for cat identification
Weight verification system
Audio pattern matching for meow detection
Remote control via mobile app
Automated scheduling
Motion detection and night vision
Weather-resistant design
Real-time notifications
Entry logging and analytics

Tech Stack

Python 3.9+
OpenCV + TensorFlow
Raspberry Pi
Flask API
SQLite
GPIO Interface

Hardware Requirements
Listed in docs/hardware.md

Getting Started
Setup instructions in docs/setup.md


Proposed structure.
smart-cat-door/
├── README.md
├── LICENSE
├── requirements.txt
├── setup.py
├── docs/
│   ├── hardware.md
│   ├── setup.md
│   └── api.md
├── tests/
│   ├── __init__.py
│   ├── test_auth.py
│   ├── test_sensors.py
│   └── test_hardware.py
├── scripts/
│   ├── install.sh
│   └── calibrate.py
├── data/
│   ├── cat_profiles/
│   ├── training_images/
│   └── audio_samples/
├── logs/
│   └── .gitkeep
└── src/
    ├── __init__.py
    ├── main.py
    ├── auth.py
    ├── sensors.py
    ├── hardware.py
    ├── notifications.py
    ├── config.py
    └── utils/
        ├── __init__.py
        ├── logging.py
        └── validators.py
