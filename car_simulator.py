import math
import util


class CarSimulator:
    """
    represents a car simulator class that stores vehicle states such as coordinate and orientation.
    """

    def __init__(self, wheelbase: float, v0: float, theta0: float) -> None:
        """
        default constructor for a car simulator
        :param wheelbase: wheelbase of the vehicle, measured by the distance between the front and the rear wheels in m
        :param v0: the initial speed of the vehicle in the direction of travel, measured in m/s
        :param theta0: the initial orientation of the vehicle, measured in radian.
        """
        # x is the position on the x-axis on a xy plane
        self.x = 0
        # y is the position on the y-axis on a xy plane
        self.y = 0
        self.wheelbase = wheelbase
        # initially, the velocity is the initial speed
        self.v = v0
        self.theta = theta0

    @util.state_tracker
    def simulator_step(self, a: float, wheel_angle: float, dt: float) -> None:
        """
        perform a step in the simulator, and update the state of the car.
        :param a: commanded vehicle acceleration in m/s^2
        :param wheel_angle:steering angle, measured at the wheels in radian
        :param dt: duration of time after which we want to provide in seconds
        """
        if dt <= 0:
            raise ValueError("dt must be positive.")
        if wheel_angle < -math.pi / 2 or wheel_angle > math.pi / 2:
            raise ValueError("wheel_angle must be in radian form")

        self.v += dt * a

        # omega is the angular velocity
        omega = 0
        if wheel_angle != 0:
            omega = self.v / util.get_turning_radius(self.wheelbase, wheel_angle)

        # theta now should represent the direction the car is going
        self.theta += omega * dt

        # update x and y coordinate on their projection
        self.x += self.v * math.cos(self.theta) * dt
        self.y += self.v * math.sin(self.theta) * dt
