# Importing required modules
import pygame
import os
import sys
import math

# Initialize Pygame
pygame.init()
pygame.display.set_caption("Autonomous Car Simulation")

# Screen size
screen_width = 1244
screen_height = 1016
screen = pygame.display.set_mode((screen_width, screen_height))

# Loading track
track = pygame.image.load(os.path.join("Assets", "track.png"))

# Setting up car
class Car(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.original_image = pygame.image.load(os.path.join("Assets", "car.png"))
        self.image = self.original_image
        self.rect = self.image.get_rect(center=(490, 820))
        self.drive_state = False
        self.vel_vector = pygame.math.Vector2(0.8, 0)
        self.angle = 0
        self.rotation_vel = 5
        self.direction = 0

    def update(self):
        self.drive()
        self.rotate()
        self.radar()

    def drive(self):
        if self.drive_state:
            self.rect.center += self.vel_vector * 6

    def rotate(self):
        if self.direction == 1:
            self.angle -= self.rotation_vel
            self.vel_vector.rotate_ip(self.rotation_vel)
        if self.direction == -1:
            self.angle += self.rotation_vel
            self.vel_vector.rotate_ip(-self.rotation_vel)

        self.image = pygame.transform.rotozoom(self.original_image, self.angle, 1.0)
        self.rect = self.image.get_rect(center=self.rect.center)

    def radar(self):
        length = 0
        x = int(self.rect.center[0])
        y = int(self.rect.center[1])

        while not screen.get_at((x, y)) == pygame.Color(2, 105, 31, 255) and length < 200:
            length += 1
            x = int(self.rect.center[0] + math.cos(math.radians(self.angle)) * length)
            y = int(self.rect.center[1] - math.sin(math.radians(self.angle)) * length)

            # Draw Radar
            pygame.draw.line(screen, (255, 255, 255), self.rect.center, (x, y), 1)
            pygame.draw.circle(screen, (0, 255, 0), (x, y), 3)


car = pygame.sprite.GroupSingle(Car())

# Main execution block
clock = pygame.time.Clock()

def eval_genomes():
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        screen.blit(track, (0, 0))

        # User input
        user_input = pygame.key.get_pressed()
        if sum(user_input) <= 1:
            car.sprite.drive_state = False
            car.sprite.direction = 0
        if user_input[pygame.K_UP]:
            car.sprite.drive_state = True
        if user_input[pygame.K_RIGHT]:
            car.sprite.direction = 1
        if user_input[pygame.K_LEFT]:
            car.sprite.direction = -1

        # Update
        car.draw(screen)
        car.update()

        # Refresh display and control frame rate
        pygame.display.update()
        clock.tick(60)

eval_genomes()
