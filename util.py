import functools


def data_recorder(func):
    @functools.wraps(func)
    def wrapper(self, *args, **kwargs):
        # Call the original simulation method
        result = func(self, *args, **kwargs)

        # Ensure the history attribute exists
        if not hasattr(self, 'history'):
            self.history = {'time': [], 'x': [], 'y': [], 'v': [], 'a': [], 'lateral_acc': []}

        # Unpack inputs (assuming a, wheel_angle, and dt are passed to all simulation methods)
        a = kwargs['a']  # commanded acceleration
        wheel_angle = kwargs['wheel_angle']  # steering angle
        dt = kwargs['dt']  # time step

        # Calculate lateral acceleration (centripetal force)
        if wheel_angle != 0:
            turning_radius = self.wheelbase / math.tan(wheel_angle)
            lateral_acceleration = self.v ** 2 / turning_radius
        else:
            lateral_acceleration = 0

        # Append data to history
        self.history['time'].append(dt)
        self.history['x'].append(self.x)
        self.history['y'].append(self.y)
        self.history['v'].append(self.v)
        self.history['a'].append(a)
        self.history['lateral_acc'].append(lateral_acceleration)

        return result

    return wrapper