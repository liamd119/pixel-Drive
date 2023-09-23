"""Collection of objects to represent and model a car."""
from math import pi, floor

MODULE_NAME = "car.py"
RADIANS_PER_SECOND = "rad s^-1"
RPM = "rpm"
SI = "si"
IMPERIAL = "imperial"
TORQUE = "torque"
POWER = "power"
POUND_FEET = "lb-ft"
NEWTON_METRES = "Nm"
HORSEPOWER = "hp"
WATTS = "W"


class UnitError(ValueError):
    """ Unsupported argument unit. """


class AngularVelocity:
    """Represents the physical quantity angular velocity."""

    def __init__(self, value: int | float, unit: str):
        if unit == RPM:
            self._rpm = value
        elif unit == RADIANS_PER_SECOND:
            self._rad_ps = value
        else:
            raise UnitError(f"Passed unit ({unit}) not in {RADIANS_PER_SECOND, RPM}")

    @property
    def rpm(self) -> float:
        """Angular velocity in rpm."""
        return (self._rad_ps * 60) / (2 * pi) if self._rad_ps else self._rpm

    @property
    def rad_ps(self) -> float:
        """Angular velocity in rad s^-1."""
        return (self._rpm * 2 * pi) / 60 if self._rpm else self._rad_ps

    @rpm.setter
    def rpm(self, value):
        self._rpm = value

    @rad_ps.setter
    def rad_ps(self, value):
        self._rad_ps = value


class Tyre:
    """Represents a tyre (grip characteristics of a wheel).
    :param grip: The grip of the tyre: 0 < grip <= 1
    """

    def __init__(self, grip: float):
        if not 0 < grip <= 1:
            raise ValueError("Positional attribute 'grip' is outside of allowed range:"
                             "0 < grip <= 1")
        self.grip = grip  # [no unit]


class Wheel:
    """Represents a car wheel."""

    def __init__(self, mass: float, max_braking_force: float, tyre: Tyre):
        self.mass = mass  # kg
        self.max_braking_force = max_braking_force  # N
        self.tyre = tyre
        self.velocity: float = 0.0  # m s^1
        self.force: float = 0.0  # N

    @property
    def acceleration(self) -> float:
        """Acceleration at that wheel."""
        return self.force / self.mass  # m s^-2

    def brake(self, braking_force_proportion: int) -> float:
        """Applies a braking force to that wheel."""
        self.force -= braking_force_proportion * self.max_braking_force
        return self.force


class DrivenWheel(Wheel):
    """Represents a driven car wheel."""

    def __init__(self, mass, max_braking_force, tyre):
        super().__init__(mass, max_braking_force, tyre)
        self.driving_force = 0


class TurningWheel(Wheel):
    """Represents a turning (usually front) wheel."""

    def __init__(self, mass, max_braking_force, tyre):
        super().__init__(mass, max_braking_force, tyre)
        self.steering_angle = 0


class TurningDrivenWheel(TurningWheel, DrivenWheel):
    """Represents a turning (usually front), driven wheel."""

    def __init__(self, mass, max_braking_force, tyre):
        super().__init__(mass, max_braking_force, tyre)


class Gearbox:
    """Represents a gearbox."""

    def __init__(self):
        ...


class Engine:
    """Represents an engine"""

    def __init__(self, idle_ang_vel: AngularVelocity, max_ang_vel: AngularVelocity):
        self.idle_ang_vel = idle_ang_vel
        self.max_ang_vel = max_ang_vel
        self.ang_vel: AngularVelocity = AngularVelocity(0, RPM)


# torque = radius * force
# power = torque * angular velocity
# torque = moment of inertia * angular acceleration


class DynoChart:
    """Represents the car's RPM/ Torque/ Power characteristics."""

    def __init__(self, raw_dict: dict[str: list[int], str: dict[str: str], str:list[list]]):
        rpm_start, rpm_increment, rpm_finish = raw_dict["rpm_values"]
        torque_unit, power_unit = raw_dict["units"]["torque"], raw_dict["units"]["power"]
        data = raw_dict["data"]

        self.rpm_interval = rpm_increment

        # read the data and split into the SI and Imperial lists, converting where necessary
        if torque_unit == POUND_FEET:
            si_data = map(lambda input_list: [input_list[0] * 1.356, input_list[1]], data)
            imp_data = data
        elif torque_unit == NEWTON_METRES:
            imp_data = map(lambda input_list: [input_list[0] / 1.356, input_list[1]], data)
            si_data = data
        else:
            raise UnitError(f"Unsupported unit '{torque_unit}' - unit of torque must be in "
                            f"{POUND_FEET, NEWTON_METRES}.")

        if power_unit == HORSEPOWER:
            si_data = map(lambda input_list: [input_list[0], input_list[1] * 745.7], data)
            imp_data = data
        elif power_unit == WATTS:
            imp_data = map(lambda input_list: [input_list[0], input_list[1] / 745.7], data)
            si_data = data
        else:
            raise UnitError(f"Unsupported unit '{power_unit}' - unit of power must be in "
                            f"{HORSEPOWER, WATTS}.")

        # read the raw dict into usable format, split into lists for si, imperial and power, torque
        si_torque_list = si_power_list = imp_torque_list = imp_power_list = {}
        # for loop: iterate through rpm vals generated from start, increment and end rpm vals, while concurrently
        # iterating through the Imperial and SI unit lists of torque and power values, for each creating a
        # dict[rpm value: torque/power value, ...], and assigning them to properties
        for rpm_val, (si_torque_val, si_power_val), (imp_torque_val, imp_power_val) \
                in zip(range(rpm_start, rpm_finish + rpm_increment, rpm_increment), si_data, imp_data):
            si_torque_list[rpm_val], si_power_list[rpm_val] = si_torque_val, si_power_val
            imp_torque_list[rpm_val], imp_power_list[rpm_val] = imp_torque_val, imp_power_val
        self.si_torque_list, self.si_power_list = si_torque_list, si_power_list
        self.imp_torque_list, imp_power_list = imp_torque_list, imp_power_list

    def get(self, ang_vel: AngularVelocity, quantity=TORQUE, unit=SI):
        rpm = ang_vel.rpm
        rpm_index = (rpm / self.rpm_interval) * self.rpm_interval  # gets rpm stored index below current value
        rpm_interval = self.rpm_interval
        if quantity == TORQUE:
            if unit == SI:
                val_list = self.si_torque_list
            elif unit == IMPERIAL:
                val_list = self.imp_torque_list
        elif quantity == POWER:
            if unit == SI:
                val_list = self.si_power_list
            elif unit == IMPERIAL:
                val_list = self.imp_power_list
        if not val_list:
            raise ValueError(
                f"Inappropriate argument 'quantity': {quantity} not in {TORQUE, POWER}" if quantity not in (TORQUE,
                                                                                                            POWER)
                else f"Inappropriate argument 'unit': {unit} not in {SI, IMPERIAL}")
        # return interpolated value for given rpm argument, using rpm index below given value, and gradient between
        # data point below and above given rpm value, to estimate 'y' value on graph
        return val_list[rpm_index] + (rpm - rpm_interval) * (val_list[rpm_index + rpm_interval] - val_list[
            rpm_index] / rpm_interval)




print(f"Loaded module {MODULE_NAME}")
