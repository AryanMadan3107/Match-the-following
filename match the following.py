import pygame

pygame.init()

WIDTH=800
HEIGHT=600

screen=pygame.display.set_mode((WIDTH,HEIGHT))
screen.fill("white")

cc=pygame.image.load("Lesson 6/images/candycrush.jpg")
l=pygame.image.load("Lesson 6/images/ludo.png")
ss=pygame.image.load("Lesson 6/images/subwaysurfer.png")
tr=pygame.image.load("Lesson 6/images/templerun.png")

font=pygame.font.SysFont("Arial",50)
cctext=font.render("Candy Crush",True,"black")
ltext=font.render("Ludo",True,"black")
sstext=font.render("Subway Surfer",True,"black")
trtext=font.render("Temple Run",True,"black")

cctextrect=pygame.Rect(500,285,250,50)
#pygame.draw.rect(screen,"red",cctextrect,1)
screen.blit(cctext,cctextrect)

ltextrect=pygame.Rect(500,385,250,50)
#pygame.draw.rect(screen,"red",ltextrect,1)
screen.blit(ltext,ltextrect)

sstextrect=pygame.Rect(500,85,250,50)
#pygame.draw.rect(screen,"red",sstextrect,1)
screen.blit(sstext,sstextrect)

trtextrect=pygame.Rect(500,185,250,50)
#pygame.draw.rect(screen,"red",trtextrect,1)
screen.blit(trtext,trtextrect)



ccrect=pygame.Rect(100,70,93,93)
#pygame.draw.rect(screen,"red",ccrect,1)

screen.blit(cc,ccrect)

lrect=pygame.Rect(100,170,93,93)
#pygame.draw.rect(screen,"red",lrect,1)

screen.blit(l,lrect)

ssrect=pygame.Rect(100,270,93,93)
#pygame.draw.rect(screen,"red",ssrect,1)

screen.blit(ss,ssrect)

trrect=pygame.Rect(100,370,93,93)
#pygame.draw.rect(screen,"red",trrect,1)

screen.blit(tr,trrect)





run=True

while run: 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    pygame.display.update()

