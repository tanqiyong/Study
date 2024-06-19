import pygame
import random

# 初始化 pygame
pygame.init()

# 设置颜色常量
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)

# 设置屏幕大小和块大小
WIDTH, HEIGHT = 640, 480
BLOCK_SIZE = 10

# 创建屏幕对象
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('贪吃蛇游戏')

# 创建时钟对象来控制帧率
clock = pygame.time.Clock()

# 定义蛇和食物
snake = [(5, 5), (6, 5), (7, 5)]
food = (10, 10)
dx, dy = 1, 0


def handle_events():
    """处理游戏事件"""
    global dx, dy
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and dy == 0:
                dx, dy = 0, -1
            elif event.key == pygame.K_DOWN and dy == 0:
                dx, dy = 0, 1
            elif event.key == pygame.K_LEFT and dx == 0:
                dx, dy = -1, 0
            elif event.key == pygame.K_RIGHT and dx == 0:
                dx, dy = 1, 0
    return True


def draw_game():
    """绘制游戏画面"""
    screen.fill(WHITE)  # 清屏
    for segment in snake:
        pygame.draw.rect(screen, GREEN, (segment[0] * BLOCK_SIZE, segment[1] * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE))
    pygame.draw.rect(screen, RED, (food[0] * BLOCK_SIZE, food[1] * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE))
    pygame.display.flip()  # 更新屏幕显示


def game_loop():
    """游戏主循环"""
    global snake, food, dx, dy
    running = True
    while running:
        running = handle_events()
        if not running:
            break

        # 更新蛇头的位置
        head = snake[-1]
        new_head = (head[0] + dx) % (WIDTH // BLOCK_SIZE), (head[1] + dy) % (HEIGHT // BLOCK_SIZE)

        # 检查是否吃到食物
        if new_head == food:
            snake.append(new_head)
            food = (random.randint(0, (WIDTH // BLOCK_SIZE) - 1), random.randint(0, (HEIGHT // BLOCK_SIZE) - 1))
        else:
            snake.append(new_head)
            snake.pop(0)

        # 检查游戏结束条件
        if (new_head in snake[:-1] or
                new_head[0] < 0 or new_head[0] >= WIDTH // BLOCK_SIZE or
                new_head[1] < 0 or new_head[1] >= HEIGHT // BLOCK_SIZE):
            running = False

        draw_game()  # 渲染游戏画面
        clock.tick(10)
        pygame.time.delay(100)
        pygame.display.update()


game_loop()
