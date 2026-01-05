import pygame, random, sys 

pygame.init()

W, H = 500, 600
win = pygame.display.set_mode((W, H))
pygame.display.set_caption("Dodge The Blocks")
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 36)
big_font = pygame.font.SysFont(None, 60)

player = pygame.Rect(225, 540, 50, 50)
blocks = []
score = 0
game_active = False  # Start in the menu

# Difficulty Settings: (speed, spawn_rate)
# Lower spawn_rate number = more blocks
levels = {
    "Easy": (4, 40),
    "Hard": (8, 20),
    "Impossible": (12, 10)
}
current_setting = levels["Easy"]

def reset():
    global blocks, score, game_active
    blocks = []
    score = 0
    player.x = 225
    game_active = False

def draw_menu():
    win.fill((20, 20, 20))
    title = big_font.render("Select Difficulty", True, (255, 255, 255))
    e_txt = font.render("1: Easy", True, (100, 255, 100))
    h_txt = font.render("2: Hard", True, (255, 200, 100))
    i_txt = font.render("3: Impossible", True, (255, 50, 50))
    
    win.blit(title, (W//2 - 150, 150))
    win.blit(e_txt, (W//2 - 50, 250))
    win.blit(h_txt, (W//2 - 50, 300))
    win.blit(i_txt, (W//2 - 50, 350))
    pygame.display.update()

while True:
    if not game_active:
        draw_menu()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    current_setting = levels["Easy"]
                    game_active = True
                if event.key == pygame.K_2:
                    current_setting = levels["Hard"]
                    game_active = True
                if event.key == pygame.K_3:
                    current_setting = levels["Impossible"]
                    game_active = True
        continue # Skip the rest of the loop until a level is picked

    # --- GAMEPLAY LOOP ---
    clock.tick(60)
    win.fill((20, 20, 20))
    speed, spawn_rate = current_setting

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player.x > 0:
        player.x -= 7
    if keys[pygame.K_RIGHT] and player.x < W - 50:
        player.x += 7

    # Spawn blocks based on level setting
    if random.randint(1, spawn_rate) == 1:
        blocks.append(pygame.Rect(random.randint(0, W - 40), -40, 40, 40))

    for b in blocks[:]:
        b.y += speed
        if b.y > H:
            blocks.remove(b)
            score += 1
        
        if b.colliderect(player):
            reset()

    # Draw
    pygame.draw.rect(win, (100, 200, 255), player)
    for b in blocks:
        pygame.draw.rect(win, (255, 90, 90), b)

    txt = font.render(f"Score: {score}", True, (230, 230, 230))
    win.blit(txt, (10, 10))
    pygame.display.update()