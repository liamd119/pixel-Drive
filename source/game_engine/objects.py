"""Pyhsics-related objects."""


# Arbitrary constants for testing
GRIP = 0.8  # to be expanded on


class Wheel:
    def __init__(self, grip=GRIP, radius=None, torque=None):
        self.grip = grip
        self.radius = radius  # m
        self.torque = torque  # N m


    @property
    def moment_of_inertia(self):
        return (10 * self.radius**2) / 2
    # 1/12 * mass * (height**2 + 3 * self.radius**2) perpendicular


    @property
    def angular_velocity(self):  # rad s^-1
        return self.torque * self.moment_of_inertia


    @property
    def linear_velocity(self):  # m s^-1
        return self.radius * self.angular_velocity  # v = r w
