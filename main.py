import pygame
import random

# Инициализация Pygame
pygame.init()

# Определение констант
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
CELL_SIZE = 20
FPS = 10

# Определение цветов
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# Загрузка изображений
head_img = pygame.image.load('1.png')
body_img = pygame.image.load('3.png')
apple_img = pygame.image.load('2.png')

# Функция отрисовки змеи и яблока
def draw_elements():
    screen.fill(WHITE)
    for segment in snake:
        screen.blit(body_img, (segment[0] * CELL_SIZE, segment[1] * CELL_SIZE))
    screen.blit(head_img, (snake[0][0] * CELL_SIZE, snake[0][1] * CELL_SIZE))
    screen.blit(apple_img, (apple_pos[0] * CELL_SIZE, apple_pos[1] * CELL_SIZE))

    # Отображение счета
    font = pygame.font.SysFont(None, 30)
    score_text = font.render("Score: " + str(score), True, BLACK)
    screen.blit(score_text, (10, 10))

    pygame.display.flip()


# Функция генерации новой позиции для яблока
def generate_apple_position():
    return random.randint(0, (SCREEN_WIDTH // CELL_SIZE) - 1), random.randint(0, (SCREEN_HEIGHT // CELL_SIZE) - 1)


# Создание экрана
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Змейка')

pygame.mixer.music.load("123.mp3")
pygame.mixer.music.set_volume(1)
pygame.mixer.music.play(-1)  # Зацикливание музыки

# Начальные значения
snake = [(5, 5)]
direction = (1, 0)
apple_pos = generate_apple_position()
score = 0

clock = pygame.time.Clock()

# Основной игровой цикл
running = True
while running:
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and direction != (0, 1):
                direction = (0, -1)
            elif event.key == pygame.K_DOWN and direction != (0, -1):
                direction = (0, 1)
            elif event.key == pygame.K_LEFT and direction != (1, 0):
                direction = (-1, 0)
            elif event.key == pygame.K_RIGHT and direction != (-1, 0):
                direction = (1, 0)

    # Движение змеи
    new_head = (snake[0][0] + direction[0], snake[0][1] + direction[1])
    snake.insert(0, new_head)

    # Проверка на столкновение с границами экрана
    if not (0 <= new_head[0] < SCREEN_WIDTH // CELL_SIZE) or not (0 <= new_head[1] < SCREEN_HEIGHT // CELL_SIZE):
        running = False

    # Проверка на столкновение с самой собой
    if len(snake) != len(set(snake)):
        running = False

    # Проверка на поедание яблока
    if new_head == apple_pos:
        apple_pos = generate_apple_position()
        score += 1
    else:
        snake.pop()

    # Отрисовка элементов
    draw_elements()

pygame.quit()
