"""階段三解答:防護罩 + 爆炸動畫(在階段二之上)。

⭐ 新增:
  - bunkers:畫面下方四座防護罩,由小方塊組成,被子彈打到會缺一塊
  - explosions:敵人被擊落時的爆炸特效(會擴散後消失)
  - 音效為選做,作法見 docs/space-invader-tutorial/stage3-bunkers.md
"""
import pygame
import random

pygame.init()
WIDTH, HEIGHT = 600, 700
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space Invader - Stage 3")
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 36)
big_font = pygame.font.SysFont(None, 72)

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 80, 80)
YELLOW = (255, 255, 0)
CYAN = (0, 200, 200)
ORANGE = (255, 160, 0)


def spawn_enemies():
    enemies = []
    for row in range(4):
        for col in range(8):
            enemies.append(pygame.Rect(60 + col * 60, 60 + row * 50, 40, 30))
    return enemies


def spawn_bunkers():                       # ⭐ 新增:生成四座防護罩
    blocks = []
    block = 10                             # 每個小方塊邊長
    for bunker in range(4):                # 四座,平均分布
        bx = 70 + bunker * 140
        by = HEIGHT - 150
        for row in range(3):               # 3 列 x 6 行的小方塊
            for col in range(6):
                blocks.append(pygame.Rect(bx + col * block, by + row * block, block, block))
    return blocks


def reset_game():
    player = pygame.Rect(WIDTH // 2 - 25, HEIGHT - 60, 50, 30)
    bullets = []
    enemy_bullets = []
    enemies = spawn_enemies()
    bunkers = spawn_bunkers()              # ⭐ 新增
    return player, bullets, enemy_bullets, enemies, bunkers


player, bullets, enemy_bullets, enemies, bunkers = reset_game()
enemy_dir = 1
enemy_speed = 1
score = 0
lives = 3
level = 1
explosions = []          # ⭐ 新增:每個元素是 [x, y, 半徑]
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
                player, bullets, enemy_bullets, enemies, bunkers = reset_game()
                enemy_dir = 1
                enemy_speed = 1
                score = 0
                lives = 3
                level = 1
                explosions = []
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

        # 玩家子彈擊中敵人 → 爆炸特效
        for b in bullets[:]:
            for e in enemies[:]:
                if b.colliderect(e):
                    if b in bullets:
                        bullets.remove(b)
                    explosions.append([e.centerx, e.centery, 2])   # ⭐ 新增
                    enemies.remove(e)
                    score += 10
                    break

        # ⭐ 新增:子彈打到防護罩會削掉一塊(玩家子彈、敵人子彈都會)
        for b in bullets[:]:
            for block in bunkers[:]:
                if b.colliderect(block):
                    bunkers.remove(block)
                    if b in bullets:
                        bullets.remove(b)
                    break
        for eb in enemy_bullets[:]:
            for block in bunkers[:]:
                if eb.colliderect(block):
                    bunkers.remove(block)
                    if eb in enemy_bullets:
                        enemy_bullets.remove(eb)
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

        if not enemies:
            level += 1
            enemy_speed += 1
            bullets.clear()
            enemy_bullets.clear()
            enemies = spawn_enemies()
            bunkers = spawn_bunkers()          # ⭐ 新關卡補回防護罩

        # ⭐ 新增:爆炸特效擴散,半徑超過 18 就消失
        for ex in explosions[:]:
            ex[2] += 2
            if ex[2] > 18:
                explosions.remove(ex)

    pygame.draw.rect(screen, GREEN, player)
    for b in bullets:
        pygame.draw.rect(screen, YELLOW, b)
    for eb in enemy_bullets:
        pygame.draw.rect(screen, RED, eb)
    for e in enemies:
        pygame.draw.rect(screen, WHITE, e)
    for block in bunkers:                       # ⭐ 新增:畫防護罩
        pygame.draw.rect(screen, CYAN, block)
    for ex in explosions:                       # ⭐ 新增:畫爆炸
        pygame.draw.circle(screen, ORANGE, (ex[0], ex[1]), ex[2])

    screen.blit(font.render(f"Score: {score}", True, WHITE), (10, 10))
    lives_text = font.render(f"Lives: {lives}", True, WHITE)
    screen.blit(lives_text, (WIDTH - lives_text.get_width() - 10, 10))
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
