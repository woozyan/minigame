import pygame
import time
import random
from minigame.constants import X_SIZE, Y_SIZE, CAPTION, WHITE_COLOR
from minigame.snake import Snake
from minigame.egg import Egg


window = pygame.display.set_mode((X_SIZE, Y_SIZE))
pygame.display.set_caption(CAPTION)


def draw_window(window, snake, egg):
    window.fill(WHITE_COLOR)
    egg.draw(window)
    snake.draw(window)
    pygame.display.update()


def main():
    running = True
    snake = Snake(250, 250)
    egg = Egg(100, 100)
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()

        snake.move()
        if snake.eat_egg(egg):
            egg = Egg(random.randint(0, X_SIZE), random.randint(0, X_SIZE))
        # egg.move()
        draw_window(window, snake, egg)
        time.sleep(0.1)


if __name__ == "__main__":
    main()
