# Autonomous Self-Driving Car using Python, NEAT, and Pygame 🚗🤖

Welcome to the **Self-Driving Car** project! This project demonstrates the creation of a simple autonomous vehicle from scratch using Python, the NEAT (NeuroEvolution of Augmenting Topologies) algorithm, and Pygame for simulation. The car learns to navigate a track autonomously, avoiding obstacles and improving its driving skills through evolutionary neural networks.

## Features 🎯
- **Neuroevolution:** Uses the NEAT algorithm to evolve neural networks for controlling the car.
- **Interactive Visualization:** Watch the car drive and improve its skills over generations.
- **Customizable Tracks:** Easily modify or create tracks to test the car's driving abilities.
- **Lightweight and Easy to Run:** Built with Python and Pygame, no heavy dependencies.

---

## Table of Contents 📋
1. [Getting Started](#getting-started)
2. [Installation](#installation)
3. [How It Works](#how-it-works)
4. [Usage](#usage)
5. [Customization](#customization)
6. [Roadmap](#roadmap)
7. [Acknowledgements](#acknowledgements)

---

## Getting Started 🚀

Clone this repository to your local machine and run the simulation to see the car in action! The project is beginner-friendly and great for learning about neural networks, evolution algorithms, and game simulation.

---

## Installation 🛠️

1. **Clone the Repository**  
   ```bash
   git clone <repository_url>
   cd <repository_directory>
   ```

2. **Install Dependencies**  
   Ensure you have Python 3.x installed. Then, install the required libraries:
   ```bash
   pip install neat-python pygame
   ```

3. **Run the Project**  
   ```bash
   python main.py
   ```

---

## How It Works ⚙️

1. **Simulation with Pygame**  
   Pygame provides a visual environment for the car to navigate a track. The track contains walls and obstacles that the car must avoid.

2. **Control with Neural Networks**  
   The car's behavior is controlled by a neural network that decides how to steer and accelerate based on inputs such as distance to walls and track edges.

3. **Learning with NEAT**  
   NEAT evolves the neural networks by simulating generations. Each generation creates multiple cars, evaluates their performance (fitness), and selects the best ones to "breed" the next generation.

4. **Fitness Function**  
   The fitness function rewards cars that stay on the track longer and reach farther distances.

---

## Usage 🕹️

1. **Run the Simulation**  
   Execute the main script to start the simulation:
   ```bash
   python main.py
   ```

2. **Watch the Evolution**  
   - The simulation starts with randomly generated networks.
   - Over generations, you'll notice the cars improving as they "learn" to navigate the track.

3. **Pause or Restart**  
   Use in-game commands (e.g., keyboard keys) to pause or restart the simulation if needed.

---

## Customization 🎨

- **Track:** Modify the track layout in the `track.png` file or update the logic in the `track` folder.
- **NEAT Configurations:** Tweak parameters in the `neat-config.txt` file to adjust the learning process, such as population size or mutation rates.
- **Car Physics:** Modify car speed, acceleration, or other physics parameters in the `car.py` script.

---

## Roadmap 🛣️

- Add support for multiple tracks.
- Improve visualization with real-time stats (e.g., generation number, best fitness score).
- Implement advanced fitness evaluation metrics.
- Add support for obstacles and dynamic environments.
- Integrate reinforcement learning for comparison with NEAT.

---

## Final Product 📸

This is a demo of my final product:

![Final Product Demo](Assets/FinalProductDemo.gif)

Feel free to explore the project and check out the functionality!

## Acknowledgements 🙏

This project is inspired by the **[YouTube tutorial](https://www.youtube.com/watch?v=JNAtyw_NENo)** on building a self-driving car with NEAT and Pygame. Special thanks to the tutorial creator for the guidance and inspiration.

Feel free to contribute, modify, and share your ideas! 🚗💨

---

## License 📄

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## Contact 📧

**Creator:** Yajur Vashisht  
📫 Feel free to reach out: yajur.vashisht@ucalgary.ca  

Happy coding! 🚀
