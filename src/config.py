"""
Configuration Module
Central location for all system settings including schedules,
cat profiles, sensor thresholds, and authentication parameters.
Supports runtime configuration updates.
"""

ALLOWED_TIMES = [
    ("05:00", "09:00"),
    ("14:00", "15:00"),
    ("22:00", "23:00")
]

CAT_PROFILE = {
    "name": "Mittens",
    "weight_range": (3.5, 5.0),
    "min_auth_score": 0.7
}
