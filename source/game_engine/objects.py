"""Pyhsics-related objects."""


# Arbitrary constants for testing
GRIP = 0.8  # to be expanded on


class Wheel:
    def __init__(self, grip=GRIP):
        """Class represents a car wheel"""
        self.grip = grip
    
class RearWheel(Wheel):
    def __init__(self, grip=GRIP, force_applied=None):
        super.__init__(self, grip)
        self.force_applied = force_applied
        
        

    # @property
    # def moment_of_inertia(self):
    #     """Moment of inertia (kg m^2).
    #      Calculated using 1/2 * m * r^2, where m = mass, r = radius."""
    #     return (10 * self.radius**2) / 2  # kg m^2
    #
    # @property
    # def angular_momentum(self):
    #     """Angular momentum ("""
    #     return
    #
    # @property
    # def angular_velocity(self):  # rad s^-1
    #     """Angular velocity (rad s^-1).
    #     Calculated using T * I"""
    #     return self.torque * self.moment_of_inertia

    @property
    def linear_velocity(self):  # m s^-1
        return self.radius * self.angular_velocity  # v = r w
