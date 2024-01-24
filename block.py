import pygame
import random
import sys

class Block(pygame.sprite.Sprite):
    def __init__(self, color, x, y):
        super().__init__()
        self.image = pygame.Surface((50, 20))
        self.image.fill(color)
        self.rect = self.image.get_rect(topleft=(x, y))

class Ball(pygame.sprite.Sprite):
    def __init__(self, color, x, y):
        super().__init__()
        self.image = pygame.Surface((20, 20), pygame.SRCALPHA)
        pygame.draw.circle(self.image, color, (10, 10), 10)
        self.rect = self.image.get_rect(center=(x, y))
        self.speed = [5, 5]

    def update(self):
        self.rect.move_ip(self.speed)

class Paddle(pygame.sprite.Sprite):
    def __init__(self, color, x, y):
        super().__init__()
        self.image = pygame.Surface((100, 20))
        self.image.fill(color)
        self.rect = self.image.get_rect(topleft=(x, y))

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.move_ip(-7, 0)
        if keys[pygame.K_RIGHT] and self.rect.right < 800:
            self.rect.move_ip(7, 0)

class BlockBreakerGame:
    def __init__(self):
        pygame.init()
        self.width, self.height = 800, 600
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("블록 깨기 게임")

        self.white = (255, 255, 255)
        self.black = (0, 0, 0)
        self.colors = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0), (255, 0, 255)]

        self.clock = pygame.time.Clock()
        self.running = True
        self.all_sprites = pygame.sprite.Group()

        self.paddle = Paddle(self.black, (self.width - 100) // 2, self.height - 30)
        self.ball = Ball(self.black, self.width // 2, self.height // 2)
        self.blocks = pygame.sprite.Group()

        for i in range(5):
            for j in range(10):
                color = random.choice(self.colors)
                block = Block(color, j * 80, i * 30)
                self.blocks.add(block)
                self.all_sprites.add(block)

        self.all_sprites.add(self.paddle, self.ball)

        self.ball_count = 1  # 추가: 공의 개수 초기화

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    sys.exit()

    def update(self):
        self.all_sprites.update()

        # Ball and paddle collision
        if pygame.sprite.collide_rect(self.ball, self.paddle):
            self.ball.speed[1] = -self.ball.speed[1]

        # Ball and block collision
        block_hit = pygame.sprite.spritecollide(self.ball, self.blocks, True)
        if block_hit:
            self.ball.speed[1] = -self.ball.speed[1]
            self.ball_count = min(self.ball_count + random.randint(1, 5), 5)

        # Ball and wall collision
        if self.ball.rect.left < 0 or self.ball.rect.right > self.width:
            self.ball.speed[0] = -self.ball.speed[0]
        if self.ball.rect.top < 0:
            self.ball.speed[1] = -self.ball.speed[1]

        # Ball falls below the paddle
        if self.ball.rect.top > self.height:
            self.ball_count -= 1
            if self.ball_count == 0:
                sys.exit()
            else:
                self.ball.rect.center = (self.width // 2, self.height // 2)
                self.ball.speed[1] = -self.ball.speed[1]

        # Check for victory
        if not self.blocks:
            sys.exit()

    def run_game(self):
        while self.running:
            self.handle_events()
            self.update()

            self.screen.fill(self.white)
            self.all_sprites.draw(self.screen)

            pygame.display.flip()
            self.clock.tick(60)

        pygame.quit()

if __name__ == "__main__":
    game = BlockBreakerGame()
    game.run_game()
