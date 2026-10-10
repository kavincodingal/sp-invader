import pygame
import random
pygame.init()
s=pygame.display.set_mode((600,400))
pygame.display.set_caption("catch the apple")
white=(255,255,255)
red=(255,0,0)
green=(0,255,0)
brown=(139,69,19)
black=(0,0,0)

bx=250
by=340
bwidth=100
bheight=30

ax=random.randint(20,500)
ay=0
asize=5

score=0
clock=pygame.time.Clock()

running=True
while running:

    # Check events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    keys=pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        bx=bx-5
    if keys[pygame.K_RIGHT]:
            bx=bx+5
    if bx<0:
         bx=0
    if bx>500:
         bx=500
    ay=ay+3
    if ay>=by:
         if bx<ax<bx+bwidth:
              score=score+1
              ax=random.randint(20,580)
              ay=0
    if ay>400:
         ax=random.randint(20,580)
         ay=0
    s.fill(white)
    b=pygame.Rect(bx,by,bwidth,bheight)
    pygame.draw.rect(s,brown,b)
    pygame.draw.circle(s,red,(ax,ay),asize)
    font=pygame.font.Font(None,36)
    scoretext=font.render("Score: "+str(score),True,black)
    s.blit(scoretext,(20,20))

    pygame.display.update()
    clock.tick(60)
pygame.quit()
    