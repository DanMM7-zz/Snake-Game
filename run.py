import pygame
import random


# Initialize pygame
pygame.init()


class Snake:
    def __init__(self):
        """
        Snake the game in Python made with pygame
        """

        # Set height and width of the application and set the background to white
        self.window = pygame.display.set_mode((550, 550))
        self.window.fill((255, 255, 255))

        # Set the caption of the game
        pygame.display.set_caption("Snake")

        # Start positions of the snake
        self.snake = [(88, 264, 20, 20), (66, 264, 20, 20)]

        # Tuple that will hold the position of the snake's food
        self.food = ()

        # The direction the snake is moving
        self.direction_of_movement = ""

    def draw_rectangle(self, color, position):
        """
        Draw a rectangle

        :param color: The color of the rectangle
        :param position: The position of the rectangle
        :return: none
        """

        # Draw a rectangle
        pygame.draw.rect(self.window, color, position)

    def draw_circle(self, color, position, radius):
        """
        Draw a circle

        :param color: The color of the circle
        :param position: The position of the circle
        :param radius: The radius of the circle
        :return: none
        """

        # Draw a circle
        pygame.draw.circle(self.window, color, position, radius)

    def draw_snake(self, positions, eyes=False):
        """
        Draw the snake

        :param positions: The positions of the snake's body
        :param eyes: True or False. Determines if the snake has eyes
        :return: none
        """

        for position in positions:
            self.draw_rectangle((0, 0, 255), position)

        # Draw the snake's eyes
        if eyes:
            # Check if the snake is facing horizontally
            if self.snake[0][1] == self.snake[1][1]:
                # Check if the snake is facing leftwards
                if self.snake[0][0] < self.snake[1][0]:
                    self.draw_circle((0, 0, 0), (positions[0][0] + 5, positions[0][1] + 5), 3)
                    self.draw_circle((0, 0, 0), (positions[0][0] + 5, positions[0][1] + 15), 3)
                # Check if the snake is facing rightwards
                elif self.snake[0][0] > self.snake[1][0]:
                    self.draw_circle((0, 0, 0), (positions[0][0] + 15, positions[0][1] + 5), 3)
                    self.draw_circle((0, 0, 0), (positions[0][0] + 15, positions[0][1] + 15), 3)

            # Check if the snake is facing vertically
            if self.snake[0][0] == self.snake[1][0]:
                # Check if the snake is facing downwards
                if self.snake[0][1] > self.snake[1][1]:
                    self.draw_circle((0, 0, 0), (positions[0][0] + 5, positions[0][1] + 15), 3)
                    self.draw_circle((0, 0, 0), (positions[0][0] + 15, positions[0][1] + 15), 3)
                # Check if the snake is facing upwards
                elif self.snake[0][1] < self.snake[1][1]:
                    self.draw_circle((0, 0, 0), (positions[0][0] + 5, positions[0][1] + 5), 3)
                    self.draw_circle((0, 0, 0), (positions[0][0] + 15, positions[0][1] + 5), 3)

    def move_snake(self, direction):
        """
        Updates the position of the snake

        :param direction: the direction in which the snake needs to move
        :return: none
        """

        if direction == "UP":
            # Check if the snake can move upwards
            if self.snake[0][0] == self.snake[1][0] and self.snake[0][1] > self.snake[1][1]:
                return self.reset_game()

            # Check if the snake hits the border of the board
            if self.snake[0][1] <= 0:
                return self.reset_game()

            # Check if snake hits itself
            for position in self.snake:
                if position == (self.snake[0][0], self.snake[0][1] - 22, self.snake[0][2], self.snake[0][3]):
                    return self.reset_game()

            for i in range(len(self.snake) - 1, 0, -1):
                self.snake[i] = self.snake[i - 1]
            self.snake[0] = (self.snake[0][0], self.snake[0][1] - 22, self.snake[0][2], self.snake[0][3])

        elif direction == "DOWN":
            # Check if the snake can move downwards
            if self.snake[0][0] == self.snake[1][0] and self.snake[0][1] < self.snake[1][1]:
                return self.reset_game()

            # Check if the snake hits the border of the board
            if self.snake[0][1] >= 528:
                return self.reset_game()

            # Check if snake hits itself
            for position in self.snake:
                if position == (self.snake[0][0], self.snake[0][1] + 22, self.snake[0][2], self.snake[0][3]):
                    return self.reset_game()

            for i in range(len(self.snake) - 1, 0, -1):
                self.snake[i] = self.snake[i - 1]
            self.snake[0] = (self.snake[0][0], self.snake[0][1] + 22, self.snake[0][2], self.snake[0][3])

        elif direction == "LEFT":
            # Check if the snake can move leftwards
            if self.snake[0][1] == self.snake[1][1] and self.snake[0][0] > self.snake[1][0]:
                return self.reset_game()

            # Check if the snake hits the border of the board
            if self.snake[0][0] <= 0:
                return self.reset_game()

            # Check if snake hits itself
            for position in self.snake:
                if position == (self.snake[0][0] - 22, self.snake[0][1], self.snake[0][2], self.snake[0][3]):
                    return self.reset_game()

            for i in range(len(self.snake) - 1, 0, -1):
                self.snake[i] = self.snake[i - 1]
            self.snake[0] = (self.snake[0][0] - 22, self.snake[0][1], self.snake[0][2], self.snake[0][3])

        elif direction == "RIGHT":
            # Check if the snake can move rightwards
            if self.snake[0][1] == self.snake[1][1] and self.snake[0][0] < self.snake[1][0]:
                return self.reset_game()

            # Check if the snake hits the border of the board
            if self.snake[0][0] >= 528:
                return self.reset_game()

            # Check if snake hits itself
            for position in self.snake:
                if position == (self.snake[0][0] + 22, self.snake[0][1], self.snake[0][2], self.snake[0][3]):
                    return self.reset_game()

            for i in range(len(self.snake) - 1, 0, -1):
                self.snake[i] = self.snake[i - 1]
            self.snake[0] = (self.snake[0][0] + 22, self.snake[0][1], self.snake[0][2], self.snake[0][3])

    def random_generate_food(self):
        """
        Randomly generate food for the snake
        """

        if not self.food:
            for position in self.snake:
                x_position = random.randrange(0, 550, 22)
                y_position = random.randrange(0, 550, 22)

                if position != (x_position, y_position, 20, 20):
                    self.food += (x_position, y_position, 20, 20)
                    self.draw_rectangle((255, 0, 0), (x_position, y_position, 20, 20))
                    break
        else:
            self.draw_rectangle((255, 0, 0), self.food)

    def check_if_snake_eats_food(self):
        """
        Check if the snake eats his food. If
        the snake eats his food than make the snake grow
        """

        if self.snake[0] == self.food:
            # Check if the snake is facing horizontally
            if self.snake[-2][1] == self.snake[-1][1]:
                if self.snake[-2][0] < self.snake[-1][0]:
                    self.snake.append((self.snake[-1][0] + 22, self.snake[-1][1], self.snake[-1][2], self.snake[-1][3]))
                if self.snake[-2][0] > self.snake[-1][0]:
                    self.snake.append((self.snake[-1][0] - 22, self.snake[-1][1], self.snake[-1][2], self.snake[-1][3]))

            # Check if the snake is facing vertically
            if self.snake[-2][0] == self.snake[-1][0]:
                if self.snake[-2][1] < self.snake[-1][1]:
                    self.snake.append((self.snake[-1][0], self.snake[-1][1] + 22, self.snake[-1][2], self.snake[-1][3]))
                if self.snake[-2][1] > self.snake[-1][1]:
                    self.snake.append((self.snake[-1][0], self.snake[-1][1] - 22, self.snake[-1][2], self.snake[-1][3]))

            self.food = ()
            self.random_generate_food()

    def initialize_game(self):
        """
        Initialize the game
        """

        # Draw black rectangles
        for i in range(0, 550, 22):
            for j in range(0, 550, 22):
                self.draw_rectangle((0, 0, 0), (i, j, 20, 20))

        # Generate food
        self.random_generate_food()

        # Draw snake
        self.draw_snake(self.snake, eyes=True)

    def reset_game(self):
        # Set the start positions of the snake
        self.snake = [(88, 264, 20, 20), (66, 264, 20, 20)]

        # Reset food coordinates
        self.food = ()

        # Reset the direction the snake is moving
        self.direction_of_movement = ""

    def play_game(self):
        """
        Play the snake game
        """

        clock = pygame.time.Clock()

        while True:
            pygame.time.delay(50)
            clock.tick(10)

            # Initialize game
            self.initialize_game()

            # Check if the snake eats food
            self.check_if_snake_eats_food()
            
            # Check for events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()

                # Check if one of the arrow keys was pressed
                if event.type == pygame.KEYDOWN:
                    # If a key was pressed then change the direction the snake is moving
                    if event.key == pygame.K_UP:
                        self.direction_of_movement = "UP"
                    elif event.key == pygame.K_DOWN:
                        self.direction_of_movement = "DOWN"
                    elif event.key == pygame.K_LEFT:
                        self.direction_of_movement = "LEFT"
                    elif event.key == pygame.K_RIGHT:
                        self.direction_of_movement = "RIGHT"

            # Move snake
            self.move_snake(self.direction_of_movement)

            # Update window
            pygame.display.flip()


snake = Snake()
snake.play_game()
