import pygame
import os
import math
import sys
import neat

SCREEN_WIDTH = 1244
SCREEN_HEIGHT = 1016
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

TRACK = pygame.image.load(os.path.join("Assets", "track.png"))


class Car(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.original_image = pygame.image.load(os.path.join("Assets", "car.png"))
        self.image = self.original_image
        self.rect = self.image.get_rect(center=(490, 820))
        self.vel_vector = pygame.math.Vector2(0.8, 0)
        self.angle = 0
        self.rotation_vel = 5
        self.direction = 0
        self.alive = True
        self.radars = []

    def update(self):
        self.radars.clear()  # Clear the radar data
        self.drive()  # Update car's movement
        self.rotate()  # Update car's rotation
        for radar_angle in (-60, -30, 0, 30, 60):  # Check radar angles
            self.radar(radar_angle)
        self.collision()  # Check for collisions
        self.data()  # Get radar distance data

    def drive(self):
        self.rect.center += self.vel_vector * 6  # Update car's position based on velocity

    def collision(self):
        length = 40
        # Calculate collision points for both right and left directions
        collision_point_right = [int(self.rect.center[0] + math.cos(math.radians(self.angle + 18)) * length),
                                 int(self.rect.center[1] - math.sin(math.radians(self.angle + 18)) * length)]
        collision_point_left = [int(self.rect.center[0] + math.cos(math.radians(self.angle - 18)) * length),
                                int(self.rect.center[1] - math.sin(math.radians(self.angle - 18)) * length)]

        # Die on Collision
        if SCREEN.get_at(collision_point_right) == pygame.Color(2, 105, 31, 255) \
                or SCREEN.get_at(collision_point_left) == pygame.Color(2, 105, 31, 255):
            self.alive = False

        # Draw Collision Points
        pygame.draw.circle(SCREEN, (0, 255, 255, 0), collision_point_right, 4)
        pygame.draw.circle(SCREEN, (0, 255, 255, 0), collision_point_left, 4)

    def rotate(self):
        # Rotation based on direction
        if self.direction == 1:
            self.angle -= self.rotation_vel
            self.vel_vector.rotate_ip(self.rotation_vel)
        if self.direction == -1:
            self.angle += self.rotation_vel
            self.vel_vector.rotate_ip(-self.rotation_vel)

        # Apply rotation to car image
        self.image = pygame.transform.rotozoom(self.original_image, self.angle, 0.1)
        self.rect = self.image.get_rect(center=self.rect.center)

    def radar(self, radar_angle):
        length = 0
        x = int(self.rect.center[0])
        y = int(self.rect.center[1])

        # Cast a ray in the radar's direction until a collision is detected
        while not SCREEN.get_at((x, y)) == pygame.Color(2, 105, 31, 255) and length < 200:
            length += 1
            x = int(self.rect.center[0] + math.cos(math.radians(self.angle + radar_angle)) * length)
            y = int(self.rect.center[1] - math.sin(math.radians(self.angle + radar_angle)) * length)

        # Draw Radar
        pygame.draw.line(SCREEN, (255, 255, 255, 255), self.rect.center, (x, y), 1)
        pygame.draw.circle(SCREEN, (0, 255, 0, 0), (x, y), 3)

        # Calculate distance from car center to radar hit point
        dist = int(math.sqrt(math.pow(self.rect.center[0] - x, 2)
                             + math.pow(self.rect.center[1] - y, 2)))

        # Store radar data (angle and distance)
        self.radars.append([radar_angle, dist])

    def data(self):
        # Convert radar distances into input data for the neural network
        input_data = [0, 0, 0, 0, 0]
        for i, radar in enumerate(self.radars):
            input_data[i] = int(radar[1])
        return input_data


def remove(index):
    # Remove the car, genome, and network from their respective lists
    cars.pop(index)
    ge.pop(index)
    nets.pop(index)


def eval_genomes(genomes, config):
    global cars, ge, nets

    cars = []
    ge = []
    nets = []

    for genome_id, genome in genomes:
        cars.append(pygame.sprite.GroupSingle(Car()))  # Create a new car sprite
        ge.append(genome)  # Store the genome
        net = neat.nn.FeedForwardNetwork.create(genome, config)  # Create the neural network
        nets.append(net)  # Store the network
        genome.fitness = 0  # Initialize fitness

    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        SCREEN.blit(TRACK, (0, 0))  # Draw track background

        if len(cars) == 0:  # If there are no cars left, end the loop
            break

        for i, car in enumerate(cars):
            ge[i].fitness += 1  # Increment fitness for each car
            if not car.sprite.alive:
                remove(i)  # Remove car if it is dead

        for i, car in enumerate(cars):
            output = nets[i].activate(car.sprite.data())  # Get output from the neural network

            # Update car direction based on neural network output
            if output[0] > 0.7:
                car.sprite.direction = 1  # Turn right
            if output[1] > 0.7:
                car.sprite.direction = -1  # Turn left
            if output[0] <= 0.7 and output[1] <= 0.7:
                car.sprite.direction = 0  # Move straight

        # Update and draw all cars
        for car in cars:
            car.draw(SCREEN)
            car.update()
        pygame.display.update()


# Setup NEAT Neural Network
def run(config_path):
    global pop
    config = neat.config.Config(
        neat.DefaultGenome,
        neat.DefaultReproduction,
        neat.DefaultSpeciesSet,
        neat.DefaultStagnation,
        config_path
    )

    pop = neat.Population(config)  # Create the NEAT population

    pop.add_reporter(neat.StdOutReporter(True))  # Add reporter to print stats
    stats = neat.StatisticsReporter()  # Track statistics of the population
    pop.add_reporter(stats)

    pop.run(eval_genomes, 50)  # Run the evolutionary process


if __name__ == '__main__':
    local_dir = os.path.dirname(__file__)
    config_path = os.path.join(local_dir, 'config.txt')
    run(config_path)
