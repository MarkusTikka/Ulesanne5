import pygame


pygame.init()

#Ekraani suurus
screen_width = 640
screen_height = 480
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Palli mäng")

#font
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 36)

#Värvid
bg_color = (200, 200, 255)
text_color = (0, 0, 0)

#pildid
paddle_img = pygame.image.load("pad.png")
ball_img = pygame.image.load("ball.png")


paddle_img = pygame.transform.scale(paddle_img, (120, 20))
ball_img = pygame.transform.scale(ball_img, (20, 20))

#Pall
ball_rect = ball_img.get_rect()
ball_rect.x = screen_width // 2
ball_rect.y = screen_height // 2
ball_speed_x = 4
ball_speed_y = 4

#Alus/palk
paddle_rect = paddle_img.get_rect()
paddle_rect.x = screen_width // 2 - paddle_rect.width // 2
paddle_rect.y = int(screen_height / 1.5)
paddle_speed = 3
paddle_direction = 1  # 1 paremale, -1 vasakule

#Punktid
score = 0

#Mängu tsükkel
running = True
while running:
    screen.fill(bg_color)

    # Sündmused
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    #pall liigub
    ball_rect.x += ball_speed_x
    ball_rect.y += ball_speed_y

    #Põrkab
    if ball_rect.left <= 0 or ball_rect.right >= screen_width:
        ball_speed_x *= -1
    if ball_rect.top <= 0:
        ball_speed_y *= -1
    if ball_rect.bottom >= screen_height:
        ball_speed_y *= -1
        score -= 1  #Negatiivne punkt kui puutub alumist serva

    #Liigutab alust/palki
    paddle_rect.x += paddle_speed * paddle_direction
    if paddle_rect.left <= 0 or paddle_rect.right >= screen_width:
        paddle_direction *= -1

    #Pall põrkub alusest ainult siis kui liigub alt üles
    if paddle_rect.colliderect(ball_rect) and ball_speed_y > 0:
        ball_speed_y *= -1
        score += 1   #Positiivne punkt aluse eest

    #Joonistab alus ja pall
    screen.blit(paddle_img, paddle_rect)
    screen.blit(ball_img, ball_rect)

    #Kuvab punktid
    score_text = font.render(f"Punktid: {score}", True, text_color)
    screen.blit(score_text, (10, 10))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
