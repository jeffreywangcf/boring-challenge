# Not-so-boring Challenge

In this challenge, I explored two fun assignments:

1. **Car Simulator**: I built a simple 2D car simulator that can accelerate, drive in straight lines, and turn in circles based on physics rules.
2. **Sequence Calculator**: I worked on calculating a series based on a recursive formula, focusing on efficiency and analyzing time complexity.

## Setting up

To get started with this project, follow these steps:

1. **Unzip the project**: Extract the contents of the project folder to your preferred directory.
2. **Install Python**: Ensure you have Python 3.8 or higher installed. If not, you can download it from [here](https://www.python.org/downloads/).
3. **Install dependencies**: Navigate to the project folder and run the following command to install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. **Run the simulations**:
   To execute the car simulator, run:
     ```bash
     ./main carsim
     ```
   To execute the sequence calculator, run:
     ```bash
     ./main sequence
     ```

## Results

### Car Simulator

The car simulator generates two types of visual output, saved in the `output` folder:

- **Trajectory Plot**: The trajectory of the car is visualized on an xy plane. In the graph (`trajectory.png`), you can observe the car accelerating in a straight line initially, then transitioning into a circular path.

- **Acceleration Plot**: This plot (`accelerations.png`) displays both the longitudinal and lateral accelerations over time. The longitudinal acceleration reflects the car speeding up, while the lateral acceleration shows how it changes direction during the circular phase.


### Sequence Calculator

a) Implemented a dynamic programming approach to compute the sequence $ S_n = 3 \times S_{n-1} - S_{n-2} $, ensuring that the computation is efficient.

b) I put my justification inside `sequence.py`.

c) I plotted the execution time for computing terms from 0 to 100,000. The graph shows that the time taken scales linearly with the size of $ n $. You can find this plot saved as `output/sequence_calculator_time.png`.

d) To verify the empirical time complexity, I performed a linear regression and computed the $ R^2 $ score with `scikit-learn`. From my analysis, the $ R^2 $ score is $85.81%$.

## Challenge & Strength

The first challenge I faced was understanding the physics of the car and how to calculate various radii and angles. It’s been a while since my AP Physics A class in high school. But with a quick refresher, I was able to figure out functions like `get_turning_radius` to calculate angular velocity from linear velocity and turning angles. The second challenge was figuring out how to keep a record of simulation data. Initially, I just kept a list inside the simulation functions, but that made the code clunky and tightly coupled. The purpose of the simulation step function should purely be to update the state! I solved this by using a decorator, which now neatly tracks the state without cluttering the simulation logic. This means I can apply it to other simulators too, like a Bike Simulator or a completely different system, without duplicating code.

A strength of my code is the way I’ve reduced coupling and separated concerns using different files. For example, the car simulation logic is in one file, the plotting functions are in another, and the data tracking logic is handled by a decorator in the utility module. This kind of design follows the Separation of Concerns pattern, making each part easier to manage and modify. Another strength is my use of pydoc. Not only does this help other developers understand the code quickly, but there are also tools like Sphinx that can automatically parse these docstrings and generate nice-looking documentation.

## Areas of Improvement & Extra Features

One area for improvement is actually the decorator. While it decouples the state tracking from the simulator, it adds an extra field, `state_tracker`, which might conflict if another simulator also has a field with the same name. To avoid this, I could introduce a `DataLogger` class. This way, the decorator can use the logger to store data, and users can pass an instance of `DataLogger` (which may already have some pre-existing data). This would be particularly useful in scenarios where the logger is shared across multiple simulators or has persistent data that needs to be accessed later.

An extra feature I’m thinking of is allowing users to control the simulation through a config file. Instead of hardcoding the car’s behavior (e.g., accelerating straight, then turning), I could allow users to input commands like `ACCELERATE: -2, TURNING_ANGLE: pi/4` in a text file. I could also integrate OpenAI's API to let users describe movements in natural language, which the assistant could then translate into the required format. I’ve already done something similar when developing [BirthdayFreebies.org](https://birthdayfreebies.org), where I fine-tuned OpenAI to research and summarize deals in `JSON` format based on company names.

## Thoughts

This challenge brought back memories of doing hackathons, where I have to build something from scratch and deliver a project in a short time frame. There’s something really satisfying about being able to say, "Here’s what I built," and seeing it come together at the end.

I can definitely see how this relates to what the Boring Company is doing with their tunnels and autonomous driving systems in Las Vegas. For example, controlling and tracking a car’s path in a tunnel shares some similarities with my car simulator, especially in terms of handling acceleration and sharp turns within limited space. The sequence problem, where I dealt with large numbers, shows me of the kinds of challenges I might face. Whether it's analyzing traffic patterns or handling huge datasets for autonomous systems, this type of problem-solving will definitely come in handy.

I’m really excited to chat more about this position and the role. I’d love to share more about my experience doing this challenge, my other projects, and my software engineering background. Thanks for giving me the opportunity to tackle this challenge (I really had nothing else to do on a Friday night. Guess I’m a boring person after all).
