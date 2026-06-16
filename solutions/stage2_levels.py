"""階段二解答:關卡系統(在階段一之上)。

新增的部分都標了 ⭐:清空敵人後進入下一關、敵人加速、顯示關卡。
也順手把「生成敵人」抽成一個函式 spawn_enemies(),練習程式碼重用。
"""
import pygame
import random

pygame.init()
WIDTH, HEIGHT = 600, 700
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space Invader - Stage 2")
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 36)
big_font = pygame.font.SysFont(None, 72)

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 80, 80)
YELLOW = (255, 255, 0)


def spawn_enemies():                       # ⭐ 新增:把生成敵人獨立成函式
    enemies = []
    for row in range(4):
        for col in range(8):
            enemies.append(pygame.Rect(60 + col * 60, 60 + row * 50, 40, 30))
    return enemies


def reset_game():
    player = pygame.Rect(WIDTH // 2 - 25, HEIGHT - 60, 50, 30)
    bullets = []
    enemy_bullets = []
    enemies = spawn_enemies()              # ⭐ 改用 spawn_enemies()
    return player, bullets, enemy_bullets, enemies


player, bullets, enemy_bullets, enemies = reset_game()
enemy_dir = 1
enemy_speed = 1
score = 0
lives = 3
level = 1          # ⭐ 新增:目前關卡
game_over = False

running = True
while running:
    clock.tick(60)
    screen.fill(BLACK)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and not game_over:
                if len(bullets) < 5:
                    bullets.append(pygame.Rect(player.centerx - 2, player.top, 4, 12))
            elif event.key == pygame.K_r and game_over:
                player, bullets, enemy_bullets, enemies = reset_game()
                enemy_dir = 1
                enemy_speed = 1          # ⭐ 新增:重新開始時速度歸 1
                score = 0
                lives = 3
                level = 1                # ⭐ 新增:關卡歸 1
                game_over = False

    if not game_over:
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and player.left > 0:
            player.x -= 6
        if keys[pygame.K_RIGHT] and player.right < WIDTH:
            player.x += 6

        for b in bullets[:]:
            b.y -= 10
            if b.bottom < 0:
                bullets.remove(b)

        move_down = False
        for e in enemies:
            e.x += enemy_dir * enemy_speed
        for e in enemies:
            if e.right >= WIDTH or e.left <= 0:
                move_down = True
                break
        if move_down:
            enemy_dir *= -1
            for e in enemies:
                e.y += 20

        if enemies and random.random() < 0.02:
            shooter = random.choice(enemies)
            enemy_bullets.append(pygame.Rect(shooter.centerx - 2, shooter.bottom, 4, 12))

        for eb in enemy_bullets[:]:
            eb.y += 6
            if eb.top > HEIGHT:
                enemy_bullets.remove(eb)

        for b in bullets[:]:
            for e in enemies[:]:
                if b.colliderect(e):
                    if b in bullets:
                        bullets.remove(b)
                    enemies.remove(e)
                    score += 10
                    break

        for eb in enemy_bullets[:]:
            if eb.colliderect(player):
                enemy_bullets.remove(eb)
                lives -= 1
                if lives <= 0:
                    game_over = True

        for e in enemies:
            if e.bottom >= player.top:
                game_over = True

        # ⭐ 改寫:清空敵人 = 過關,而不是結束遊戲
        if not enemies:
            level += 1
            enemy_speed += 1          # 下一關敵人更快
            bullets.clear()
            enemy_bullets.clear()
            enemies = spawn_enemies()

    pygame.draw.rect(screen, GREEN, player)
    for b in bullets:
        pygame.draw.rect(screen, YELLOW, b)
    for eb in enemy_bullets:
        pygame.draw.rect(screen, RED, eb)
    for e in enemies:
        pygame.draw.rect(screen, WHITE, e)

    screen.blit(font.render(f"Score: {score}", True, WHITE), (10, 10))
    lives_text = font.render(f"Lives: {lives}", True, WHITE)
    screen.blit(lives_text, (WIDTH - lives_text.get_width() - 10, 10))
    # ⭐ 新增:正上方顯示關卡
    level_text = font.render(f"Level {level}", True, YELLOW)
    screen.blit(level_text, (WIDTH // 2 - level_text.get_width() // 2, 10))

    if game_over:
        text = big_font.render("GAME OVER", True, RED)
        screen.blit(text, (WIDTH // 2 - text.get_width() // 2, HEIGHT // 2 - 60))
        info = font.render(f"Reached Level {level}  Score {score}", True, WHITE)
        screen.blit(info, (WIDTH // 2 - info.get_width() // 2, HEIGHT // 2 + 10))
        hint = font.render("Press R to restart", True, WHITE)
        screen.blit(hint, (WIDTH // 2 - hint.get_width() // 2, HEIGHT // 2 + 50))

    pygame.display.flip()

pygame.quit()
