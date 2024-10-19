import functools
import math


def get_turning_radius(wheelbase: float, steering_angle: float) -> float:
    """
    calculate the turning radius based on input
    :param wheelbase: wheelbase in meters of the vehicle
    :param steering_angle: vehicle steering angle in radian
    :return: turning radius in meters
    """
    return wheelbase / math.tan(steering_angle)


def get_circle_steering_angle(wheelbase: float, radius: float, clockwise: bool = True) -> float:
    """
    calculate the steering angle based on input, if the goal is to have the vehicle drive around in circle
    :param wheelbase: wheelbase in meters of the vehicle
    :param radius: ideal radius of the circle in meters
    :param clockwise: if the direction of the circle is clockwise, true by default
    :return: the steering angle in radians
    """
    if clockwise:
        return -math.atan(wheelbase / radius)
    return math.atan(wheelbase / radius)


def state_tracker(func):
    """
    decorator to track state of a simulator. Assumed that the simulator has x, y, v, and wheelbase
    members. It created a new dictionary field `state_tracker` for the class, which is used to keep
    track of the history of the state of the simulator.
    :param func: Callable. The method of the simulator class that will be wrapped by this decorator.
    :return: Callable. The decorated method that logs the state of the simulator.
    """
    @functools.wraps(func)
    def wrapper(self, *args, **kwargs):
        """
        wrapper function that logs the state of the simulator
        :param self: Simulator instance
        :param args: method arguments, expect to be nothing
        :param kwargs: method keyword arguments, expect to have:
                - a: The acceleration of the simulator.
                - wheel_angle: The angle of the wheels, used to calculate the lateral acceleration.
                - dt: The time increment since the last simulation step.
        """

        # call the wrapped method
        result = func(self, *args, **kwargs)

        # if state_tracker is not a field, add it to the instance
        if not hasattr(self, 'state_tracker'):
            self.state_tracker = {'timestamp': [], 'x': [], 'y': [], 'v': [], 'a': [], 'la': [], 'time_elapsed': 0.0}

        # gather inputs
        a = kwargs['a']
        wheel_angle = kwargs['wheel_angle']
        dt = kwargs['dt']

        # calculate lateral acceleration
        la = 0
        if wheel_angle != 0:
            la = self.v ** 2 / get_turning_radius(self.wheelbase, wheel_angle)

        # store state data into state_tracker
        self.state_tracker['time_elapsed'] += dt
        self.state_tracker['timestamp'].append(self.state_tracker['time_elapsed'])
        self.state_tracker['x'].append(self.x)
        self.state_tracker['y'].append(self.y)
        self.state_tracker['v'].append(self.v)
        self.state_tracker['a'].append(a)
        self.state_tracker['la'].append(la)

        return result

    return wrapper
