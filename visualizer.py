from typing import List
import matplotlib.pyplot as plt


def plot_trajectory(xs: List[float], ys: List[float], destination: str = "output/trajectory.png") -> None:
    """
    plot the trajectory of the x and y coordinates of a CarSimulator simulation and save it as an image.
    :param xs: a list of x coordinates
    :param ys: a list of y coordinates
    :param destination: file destination to save the plot. Default is "trajectory.png" in the current directory.
    """

    if len(xs) != len(ys):
        raise ValueError("xs and ys must have the same length")

    plt.figure()
    plt.clf()
    plt.plot(xs, ys, label='Trajectory', color='b')
    plt.xlabel('X position (m)')
    plt.ylabel('Y position (m)')
    plt.title('Car Trajectory on XY Plane')
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.savefig(destination)


def plot_accelerations(times: List[float], longs: List[float], lats: List[float],
                       destination: str = "output/accelerations.png") -> None:
    """
    plot the longitudinal and lateral accelerations of the car simulation and save it as an image.
    :param times: a list of timestamp
    :param longs: a list of longitudinal accelerations
    :param lats: a list of lateral accelerations
    :param destination: file destination to save the plot. Default is "accelerations.png" in the current directory.
    """
    if len(times) != len(longs) or len(times) != len(lats):
        raise ValueError("times, longs and lats must have the same length")

    plt.figure()
    plt.clf()
    plt.plot(times, longs, label='Longitudinal Acceleration (m/s²)', color='b')
    plt.plot(times, lats, label='Lateral Acceleration (m/s²)', color='r')
    plt.xlabel('Time (s)')
    plt.ylabel('Acceleration (m/s²)')
    plt.title('Longitudinal and Lateral Accelerations')
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.savefig(destination)
