# The class CarSimulator is a simple 2D vehicle simulator.
# The vehicle states are:
# - x: is the position on the x axis on a xy plane
# - y: is the position on the y axis on a xy plane
# - v is the vehicle speed in the direction of travel of the vehicle
# - theta: is the angle wrt the x axis (0 rad means the vehicle
#   is parallel to the x axis, in the positive direction;
#   pi/2 rad means the vehicle is parallel
#   to the y axis, in the positive direction)
# - NOTE: all units are SI: meters (m) for distances, seconds (s) for
#   time, radians (rad) for angles...
#
# (1)
# Write the method "simulatorStep", which should update
# the vehicle states, given 3 inputs:
#  - a: commanded vehicle acceleration
#  - wheel_angle: steering angle, measured at the wheels;
#    0 rad means that the wheels are "straight" wrt the vehicle.
#    A positive value means that the vehicle is turning counterclockwise
#  - dt: duration of time after which we want to provide
#    a state update (time step)
#
# (2)
# Complete the function "main". This function should run the following simulation:
# - The vehicle starts at 0 m/s
# - The vehicle drives on a straight line and accelerates from 0 m/s to 10 m/s
#   at a constant rate of 0.4 m/s^2, then it proceeds at constant speed.
# - Once reached the speed of 10 m/s, the vehicle drives in a clockwise circle of
#   roughly 100 m radius
# - the simulation ends at 100 s
#
# (3)
# - plot the vehicle's trajectory on the xy plane
# - plot the longitudinal and lateral accelerations over time

import math
import matplotlib.pyplot as plt

import functools
import math


def record_simulation_data(func):
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


class CarSimulator():
    def __init__(self, wheelbase, v0, theta0):
        # INPUTS:
        # the wheel base is the distance between the front and the rear wheels
        self.wheelbase = wheelbase
        self.x = 0
        self.y = 0
        self.v = v0
        self.theta = theta0

    @record_simulation_data
    def simulatorStep(self, a, wheel_angle, dt):
        self.v += dt * a
        omega = 0
        if wheel_angle != 0:
            omega = self.v / (self.wheelbase / math.tan(wheel_angle))
        self.theta += omega * dt
        self.x += self.v * math.cos(self.theta) * dt
        self.y += self.v * math.sin(self.theta) * dt


def main():
    # Initialize simulation parameters
    wheelbase = 4  # arbitrary 4m wheelbase
    v0 = 0  # initial velocity
    theta0 = 0  # initial orientation
    simulator = CarSimulator(wheelbase, v0, theta0)
    dt = 0.1  # time step in seconds
    total_time = 100  # total simulation time
    acceleration = 0.4  # m/s^2
    max_speed = 10  # m/s, the target speed for straight-line driving
    wheel_angle_for_circle = -math.atan(wheelbase / 100)  # negative for clockwise circle of radius ~100m

    time = 0  # simulation time counter

    # Run simulation
    while time < total_time:
        if simulator.v < max_speed:
            # Phase 1: Accelerate in a straight line until reaching 10 m/s
            simulator.simulatorStep(a=acceleration, wheel_angle=0, dt=dt)
        else:
            # Phase 2: Once max speed is reached, drive in a clockwise circle
            simulator.simulatorStep(a=0, wheel_angle=wheel_angle_for_circle, dt=dt)

        # Increment time by the time step
        time += dt

    # Access recorded data from simulator's history
    times = [sum(simulator.history['time'][:i]) for i in range(len(simulator.history['time']))]
    x_positions = simulator.history['x']
    y_positions = simulator.history['y']
    longitudinal_accelerations = simulator.history['a']
    lateral_accelerations = simulator.history['lateral_acc']

    # Plot trajectory
    plt.figure(figsize=(10, 5))

    # Plot trajectory on XY plane
    plt.subplot(1, 2, 1)
    plt.plot(x_positions, y_positions, label='Trajectory')
    plt.xlabel('X position (m)')
    plt.ylabel('Y position (m)')
    plt.title('Vehicle Trajectory on XY Plane')
    plt.grid(True)
    plt.legend()

    # Plot longitudinal and lateral accelerations
    plt.subplot(1, 2, 2)
    plt.plot(times, longitudinal_accelerations, label='Longitudinal Acceleration (m/s²)')
    plt.plot(times, lateral_accelerations, label='Lateral Acceleration (m/s²)')
    plt.xlabel('Time (s)')
    plt.ylabel('Acceleration (m/s²)')
    plt.title('Longitudinal and Lateral Accelerations')
    plt.grid(True)
    plt.legend()

    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()

