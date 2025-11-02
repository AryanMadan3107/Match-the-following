import pygame

pygame.init()

WIDTH=800
HEIGHT=600

screen=pygame.display.set_mode((WIDTH,HEIGHT))
screen.fill("white")

score=0

cc=pygame.image.load("Lesson 6/images/candycrush.jpg")
l=pygame.image.load("Lesson 6/images/ludo.png")
ss=pygame.image.load("Lesson 6/images/subwaysurfer.png")
tr=pygame.image.load("Lesson 6/images/templerun.png")
rl=pygame.image.load("Lesson 6/images/rocket league.jpg")

font=pygame.font.SysFont("Arial",50)
cctext=font.render("Candy Crush",True,"black")
ltext=font.render("Ludo",True,"black")
sstext=font.render("Subway Surfer",True,"black")
trtext=font.render("Temple Run",True,"black")
rltext=font.render("Rocket League",True,"black")
scoretext=font.render("score = "+str(score),True,"blue")

cctextrect=pygame.Rect(500,285,250,50)
#pygame.draw.rect(screen,"red",cctextrect,1)
screen.blit(cctext,cctextrect)

ltextrect=pygame.Rect(500,385,250,50)
#pygame.draw.rect(screen,"red",ltextrect,1)
screen.blit(ltext,ltextrect)

sstextrect=pygame.Rect(500,85,250,50)
#pygame.draw.rect(screen,"red",sstextrect,1)
screen.blit(sstext,sstextrect)

trtextrect=pygame.Rect(500,485,250,50)
#pygame.draw.rect(screen,"red",trtextrect,1)
screen.blit(trtext,trtextrect)

rltextrect=pygame.Rect(500,185,250,50)
#pygame.draw.rect(screen,"red",rltextrect,1)
screen.blit(rltext,rltextrect)

screen.blit(scoretext,(20,20))

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

rlrect=pygame.Rect(100,470,93,93)
#pygame.draw.rect(screen,"red",rlrect,1)
rl=pygame.transform.scale(rl,(93,93))
screen.blit(rl,rlrect)




matches=[(ccrect,cctextrect),(lrect,ltextrect),(ssrect,sstextrect),(trrect,trtextrect),(rlrect,rltextrect)]
matchedrect=[]


startpos=None
endpos=None

startrect=None
endrect=None

run=True

while run: 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            startpos=pygame.mouse.get_pos()
            clicked_on_valid_area=False
            for irect,trect in matches:
                if irect.collidepoint(startpos) and irect not in matchedrect:
                    clicked_on_valid_area=True
                    startrect=irect
                    break
            if clicked_on_valid_area:
                pygame.draw.circle(screen,"blue",startpos,10,0)
                pygame.display.update()
        elif event.type == pygame.MOUSEBUTTONUP:
            endpos=pygame.mouse.get_pos()
            released_on_valid_area=False
            for irect,trect in matches:
                if trect.collidepoint(endpos):
                    released_on_valid_area=True
                    endrect=trect
                    break
            if released_on_valid_area and clicked_on_valid_area:
                pygame.draw.circle(screen,"blue",endpos,10,0)
                correct=False
                for irect,trect in matches:
                    if irect == startrect and trect == endrect:
                        matchedrect.append(irect)
                        pygame.draw.line(screen,"green",startpos,endpos,5)
                        correct=True
                        score+=1
                        pygame.draw.rect(screen,"white",pygame.Rect(20,20,200,50))
                        scoretext=font.render("score = "+str(score),True,"blue")
                        screen.blit(scoretext,(20,20))
                        pygame.display.update()
                        break
                if correct==False:
                    pygame.draw.line(screen,"red",startpos,endpos,5)
                    score-=1
                    pygame.draw.rect(screen,"white",pygame.Rect(20,20,200,50))
                    scoretext=font.render("score = "+str(score),True,"blue")
                    screen.blit(scoretext,(20,20))
                    pygame.display.update()
                pygame.display.update()
    pygame.display.update()

